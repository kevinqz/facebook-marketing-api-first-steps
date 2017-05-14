from facebookads.api import FacebookAdsApi
from facebookads.adobjects.business import Business
from facebookads.adobjects.campaign import Campaign
from facebookads.adobjects.adset import AdSet
from facebookads.adobjects.ad import Ad
from facebookads.adobjects.adsinsights import AdsInsights

from datetime import date

# Import getpass module to automatically discover my user:
import getpass
user = getpass.getuser()
path = '/Users/' + user + '/Desktop/'
print('Selected path for your my_facebook_access.py:', path)

# Import my_facebook_access.py file, located on your Desktop,
# where you have to store your Facebook private information (see README.md):
import sys
sys.path.append(path)
from my_facebook_access import my_app_id, my_app_secret, my_access_token, my_business_id, campaigns_group

# print("my_app_id:", my_app_id)
# print("my_app_secret:", my_app_secret)
# print("my_access_token:", my_access_token)
FacebookAdsApi.init(my_app_id, my_app_secret, my_access_token)
my_business = Business(fbid=my_business_id)
# print("my_business:", my_business)
my_accounts = list(my_business.get_assigned_ad_accounts())
# print("All accounts:", my_accounts)
selected_account = my_accounts[1]
# print("Selected account:", selected_account)

campaign_fields = [
    Campaign.Field.id,
    Campaign.Field.name,
    Campaign.Field.objective,
    Campaign.Field.status
]

# Importing a list of Campaigns' Id.
# Create your list by listing your Campaign Ids
# in the campaigns_group var located on your my_facebook_access.py,
# which should be located on your Desktop (see README.md).
# Also, you can just create a list var of Campaign Ids directly here.
selected_campaigns = campaigns_group

for each_campaign in selected_campaigns:
    selected_campaign = Campaign(fbid=each_campaign)
    print(selected_campaign.api_get(fields=campaign_fields))

    selected_adsets = selected_campaign.get_ad_sets([
        AdSet.Field.id,
        AdSet.Field.name,
        AdSet.Field.status
    ])
    print(selected_adsets)
