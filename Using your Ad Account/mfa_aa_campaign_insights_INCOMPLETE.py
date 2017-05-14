from facebookads.api import FacebookAdsApi
from facebookads.adobjects.business import Business
from facebookads.adobjects.adaccount import AdAccount
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
from my_facebook_access import my_app_id, my_app_secret, my_access_token, my_adaccount_id, campaigns_group

# print("my_app_id:", my_app_id)
# print("my_app_secret:", my_app_secret)
# print("my_access_token:", my_access_token)
FacebookAdsApi.init(my_app_id, my_app_secret, my_access_token)

selected_adaccount = AdAccount(fbid=my_adaccount_id)
print("Selected Ad Account:", selected_adaccount)

fields = [
    AdsInsights.Field.campaign_name,
    AdsInsights.Field.cpc,
    AdsInsights.Field.cpm,
    AdsInsights.Field.ctr,
    AdsInsights.Field.impressions,
    AdsInsights.Field.frequency,
    AdsInsights.Field.spend
]

params = {
    'time_range': {'since': str(date(2017, 1, 1)), 'until': str(date.today())},
    'level': 'campaign',
    'limit': 1000,
    'configured_status': 'ACTIVE'
}

insights = selected_adaccount.get_insights(fields=fields, params=params)
print(insights)
