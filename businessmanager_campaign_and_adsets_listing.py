# Regex, for name search (Campaigns, Ad Sets, Ads)
# import regex

# Importing my_facebook_access.py file where I store my private informations:
import sys
sys.path.append('/Users/kevinqz/Desktop')
from my_facebook_access import my_app_id, my_app_secret, my_access_token, my_business_id, campaigns_group

from datetime import date

from facebookads.api import FacebookAdsApi
from facebookads.adobjects.business import Business
from facebookads.adobjects.campaign import Campaign
from facebookads.adobjects.adset import AdSet
from facebookads.adobjects.ad import Ad
from facebookads.adobjects.adsinsights import AdsInsights

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

# Use the code bellow to list all Campaigns in your selected Ad Account (selected_account):
"""
all_campaigns = list(selected_account.get_campaigns())
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

# Here I'm importing a selected list of Campaigns' Id, please create yours by listing your Campaign Ids:
selected_campaigns = campaigns_group

for each_campaign in selected_campaigns:
    selected_campaign = Campaign(fbid=each_campaign)

    # Use the code bellow to do changes in the Campaign (selected_campaign):
    """
    print("Before:", selected_campaign.api_get(fields=campaign_fields))

    selected_campaign.api_update(params={
    'status': Campaign.Status.paused
    })

    print("After:", selected_campaign.api_get(fields=campaign_fields))
    """

    selected_adsets = selected_campaign.get_ad_sets([
        AdSet.Field.name,
        AdSet.Field.status,
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
