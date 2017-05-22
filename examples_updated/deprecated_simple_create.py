# Copyright 2014 Facebook, Inc.

# You are hereby granted a non-exclusive, worldwide, royalty-free license to
# use, copy, modify, and distribute this software in source code or binary
# form for use in connection with the web services and APIs provided by
# Facebook.

# As with any software that integrates with the Facebook platform, your use
# of this software is subject to the Facebook Developer Principles and
# Policies [http://developers.facebook.com/policy/]. This copyright notice
# shall be included in all copies or substantial portions of the software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.

"""
Creates an ad through a utility function.
"""
# Import getpass module to automatically discover my user:

import getpass
user = getpass.getuser()
path = '/Users/' + user + '/Desktop/'
print('Selected path for your my_facebook_access.py:', path)

# Import my_facebook_access.py file, located on your Desktop,
# where you have to store your Facebook private information (see README.md):

import sys
sys.path.append(path)
from my_facebook_access import my_app_id, my_app_secret, my_access_token, my_business_id, campaigns_group, my_conversion_id, my_adaccount_id

from facebookads import FacebookAdsApi
from facebookads import FacebookSession
from facebookads.adobjects.business import Business
from facebookads.adobjects.adaccount import AdAccount
from facebookads.adobjects.adpreview import AdPreview
from facebookads.adobjects.adset import AdSet
from facebookads.adobjects.adpromotedobject import AdPromotedObject

import ad_creation_utils
import json
import os

this_dir = os.path.dirname(__file__)
"""
config_filename = os.path.join(this_dir, 'config.json')

config_file = open(config_filename)
config = json.load(config_file)
config_file.close()
"""

### Setup session and api objects
session = FacebookSession(
    my_app_id,
    my_app_secret,
    my_access_token,
)
api = FacebookAdsApi(session)

if __name__ == '__main__':
    FacebookAdsApi.set_default_api(api)

    my_business = Business(fbid=my_business_id)
    # print("my_business:", my_business)
    my_accounts = list(my_business.get_assigned_ad_accounts())
    # print("All accounts:", my_accounts)

    selected_adaccount = my_accounts[1]

    # Get my account (first account associated with the user associated with the
    #                 session of the default api)
    # my_account = AdAccount.get_my_account()

    print('**** Creating ad...')

    # Create my ad
    my_ad = ad_creation_utils.create_website_clicks_ad(
        account=my_adaccount_id,
        app_id=my_app_id,

        name="Visit Seattle",
        country='US',

        title="Visit Seattle",                             # How it looks
        body="Beautiful Puget Sound.",
        url="http://www.seattle.gov/visiting/",
        image_path=os.path.join(
            path,
            path + '/test_image.jpg'
        ),

        optimization_goal=AdSet.OptimizationGoal.offsite_conversions,
        promoted_object=my_conversion_id,


        billing_event=AdSet.BillingEvent.impressions,
        bid_amount=300,  # $3.00 / thousand, cpm
        daily_budget=5000,  # $50.00 per day

        age_min=18,
        age_max=30,

        campaign=campaigns_group,
        status=AdSet.Status.paused,  # Default is False but let's keep this test ad paused
    )
    print('**** Done!')

    # Get the preview and write an html file
    preview = my_ad.get_previews(params={
        'ad_format':  AdPreview.AdFormat.right_column_standard,
    })
    preview_filename = os.path.join(this_dir, 'preview_ad.html')
    preview_file = open(preview_filename, 'w')
    preview_file.write(
        "<html><head><title>Facebook Ad Preview</title><body>%s</body></html>"
    )
    for each_ad in preview:
        preview_file.write(each_ad.get_html())

    preview_file.close()
    print('**** %s has been created!' % preview_filename)
