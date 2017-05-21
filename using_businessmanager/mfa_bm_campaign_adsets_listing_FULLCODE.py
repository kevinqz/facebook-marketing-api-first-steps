from facebookads.api import FacebookAdsApi
from facebookads.adobjects.business import Business
from facebookads.adobjects.campaign import Campaign
from facebookads.adobjects.adset import AdSet
from facebookads.adobjects.ad import Ad
from facebookads.adobjects.adsinsights import AdsInsights

from datetime import date

# Regex, for name search (Campaigns, Ad Sets, Ads):
# import regex

# Import getpass module to automatically discover your user:
import getpass
user = getpass.getuser()
path = '/Users/' + user + '/Desktop/'
print('Selected path for your my_facebook_access.py:', path)

# Import my_facebook_access.py file, located on your Desktop,
# where you have to store your Facebook private information (see README.md):
import sys
sys.path.append(path)
# sys.path.insert(0,'..')
from my_facebook_access import my_app_id, my_app_secret, my_access_token, my_business_id, campaigns_group

# print("my_app_id:", my_app_id)
# print("my_app_secret:", my_app_secret)
# print("my_access_token:", my_access_token)
FacebookAdsApi.init(my_app_id, my_app_secret, my_access_token)
my_business = Business(fbid=my_business_id)
# print("my_business:", my_business)
my_accounts = list(my_business.get_assigned_ad_accounts())
# print("All accounts:", my_accounts)
selected_adaccount = my_accounts[1]
# print("Selected Ad Account:", selected_adaccount)

# Use the code bellow to list all Campaigns in your selected Ad Account (selected_account):
"""
all_campaigns = list(selected_adaccount.get_campaigns())
print("All campaigns:", all_campaigns[])
"""

# Use the code bellow for Insights:
"""
insights_fields = [
    AdsInsights.Field.campaign_name,
    AdsInsights.Field.cpc,
    AdsInsights.Field.cpm,
    AdsInsights.Field.ctr,
    AdsInsights.Field.impressions,
    AdsInsights.Field.frequency,
    AdsInsights.Field.spend
]

insights_params = {
    'time_range': {'since': str(date(2017, 1, 1)), 'until': str(date.today())},
    'level': 'campaign',
    'limit': 1000,
    'configured_status': 'ACTIVE'
}

insights = selected_account.get_insights(fields=insights_fields, params=insights_params)
print(insights)
"""

campaign_fields = [
    Campaign.Field.id,
    Campaign.Field.name,
    Campaign.Field.objective,
    Campaign.Field.status
]

# Import a list of Campaigns' Id.
# Create your list by listing your Campaign Ids
# in the campaigns_group var located in your my_facebook_access.py,
# which should be located on your Desktop (see README.md).
# Also, you can just create a list var of Campaign Ids directly here, in this file.
selected_campaigns = campaigns_group

for each_campaign in selected_campaigns:
    selected_campaign = Campaign(fbid=each_campaign)
    print(selected_campaign.api_get(fields=campaign_fields))

    # Use the code bellow to do changes in the Campaign (selected_campaign):
    """
    print("Before:", selected_campaign.api_get(fields=campaign_fields))

    selected_campaign.api_update(params={
    'status': Campaign.Status.paused
    })

    print("After:", selected_campaign.api_get(fields=campaign_fields))
    """

    selected_adsets = selected_campaign.get_ad_sets([
        AdSet.Field.id,
        AdSet.Field.name,
        AdSet.Field.status
    ])
    print(selected_adsets)

# Use the code bellow to get Active Campaigns in your selected Ad Account (selected_account):
"""
selected_campaigns_param_types = {
    'effective_status': ['ACTIVE']
}

selected_campaigns_fields = [
    Campaign.Field.id ='6062669447834']

selected_campaigns = selected_account.get_campaigns(fields=selected_campaigns_fields, params={
    'status': Campaign.Status.active,
})

print(selected_campaigns)
"""

# Facebook reference code: https://developers.facebook.com/docs/marketing-api/reference/ad-campaign-group
"""
adcampaign = AdCampaign('<AD_CAMPAIGN_GROUP_ID>')
adsets = adcampaign.get_ad_sets([
    AdSet.Field.name,
    AdSet.Field.status,
])

# This will output the name of all fetched ad sets.
for adset in adsets:
    print adset[AdSet.Field.name]
"""
