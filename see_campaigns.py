from facebookads.api import FacebookAdsApi
from facebookads.adobjects.business import Business
from facebookads.adobjects.campaign import Campaign
from facebookads.adobjects.adset import AdSet
from facebookads.adobjects.ad import Ad
from facebookads.adobjects.adsinsights import AdsInsights
from datetime import date

my_app_id = 'INSERT_YOUR_APP_ID'
my_app_secret = 'INSERT_YOUR_APP_SECRET'
my_access_token = 'INSERT_YOUR_ACESS_TOKEN'
print("my_app_id:", my_app_id)
print("my_app_secret:", my_app_secret)
print("my_access_token:", my_access_token)

FacebookAdsApi.init(my_app_id, my_app_secret, my_access_token)

my_business = Business(fbid='INSERT_YOUR_BUSINESS_MANAGER_ID')
print("my_business:", my_business)

my_accounts = list(my_business.get_assigned_ad_accounts())
print("All accounts:", list(my_business.get_assigned_ad_accounts()))

my_account = my_accounts[0]
print("my_account:", my_account)

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

insights = my_account.get_insights(fields=fields, params=params)
print(insights)
