# AlphaIQ Python SDK
To get access to the API, [sign up here](https://alphaiq.ai).

Welcome to the AlphaIQ API! We offer Quantitative Linguistic Risk Indicators that enable investors to uncover hidden risks in forward-looking statements from management.

To learn more about AlphaIQ, [read about us](https://alphaiq.ai/about-us).

View our [privacy policy](https://alphaiq.ai/privacy-policy/) and [Terms of Service](https://alphaiq.ai/terms-of-service/) on our website.

## Requirements

Python >=3.7

## Installation

```
pip install alphaiq-sdk
```
Then import the package:
```python
import alphaiq_sdk
```
## Installation from GitHub
```
pip install git+https://github.com/alphaiq-ai/python-sdk.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/alphaiq-ai/python-sdk.git`
Then import the package:
```python
import alphaiq_sdk
```
## SDK Code Examples

A jupyter notebook and other code examples for the Alpha IQ SDK are available in our [Getting Started folder](alphaiq_sdk/get_started)

## Getting Started

Please follow the [installation instructions](#installation) and then run the following:

```python
import alphaiq_sdk

# Set user credentials
email = 'bob.ross@gmail.com' #str | The email you signed up with AlphaIQ. To sign up for an account, go to our website: https://alphaiq.ai
base64_password = 'AB23sdf34$=' #str | This is the password for your AlphaIQ account with Base64 encryption applied. Copy your password into this base64 encryption tool to get the encrypted version of your password: https://www.base64encode.org/

# Retrieve user token    
token_details = alphaiq_sdk.get_token(email, base64_password)
token = token_details["data"]["IdToken"]

# Connect to the AlphaIQ client
client = alphaiq_sdk.client(token)

# Get example data, a list of identifiers available to the users
identifiers = client.get_identifiers()
print(identifiers)

# Get example summary information for a particular company, Godaddy Inc
summary = client.get_identifier_details(identifier="Godaddy Inc (GDDY)")
print(summary)

# Get example list of high-risk companies
companies = client.get_high_risk_companies_across_all_industries(view_change='1q')
print(companies)

```

## Documentation for API Endpoints


Method | Description | HTTP Request
--- | --- | ---
gettoken | Get user token [requires email & base64 encrypted password] | POST/auth/gettoken
get_identifiers()   | Get List of all identifiers | GET/identifiers
search_identifier(query="Health")   | Query for any string | GET/identifiers/search?q={query}
get_all_companies_name()   | Get all companies names | GET/identifiers/companies
get_all_lvl4_industries_name()   | Get all lvl4_industries_names | GET/identifiers/industries
get_high_risk_industries(view_change='recent')   | Get high risk industries [view_change can be either recent/1m/1q] | GET/identifiers/industries/highrisk/{view_change}
get_low_risk_industries(view_change='1m')   | Get low risk industries [view_change can be either recent/1m/1q] | GET/identifiers/industries/lowrisk/{view_change}
get_high_risk_companies_across_all_industries(view_change='recent')   | Get high risk companies across all industries [view_change can be either recent/1m/1q] | GET/identifiers/companies/highrisk/{view_change}
get_high_risk_companies_of_particular_lvl2_industry(view_change='recent', lvl2_industry_name="Industrials")   | Get high risk companies of particular lvl2_industry | GET/identifiers/companies/highrisk/{view_change}?lvl2IndustryName={lvl2_industry_name}
get_high_risk_companies_of_particular_lvl3_industry(view_change='recent', lvl3_industry_name="Software")   | Get high risk companies of particular lvl3_industry | GET/identifiers/companies/highrisk/{view_change}?lvl3IndustryName={lvl3_industry_name}
get_high_risk_companies_of_particular_lvl4_industry(view_change='recent', lvl4_industry_name="Healthcare Insurance")   | Get high risk companies of particular lvl4_industry | GET/identifiers/companies/highrisk/{view_change}?lvl4IndustryName={lvl4_industry_name}
get_low_risk_companies_across_all_industries(view_change='recent')   | Get low risk companies across all industries [view_change can be either recent/1m/1q] | GET/identifiers/companies/lowrisk/{view_change}
get_low_risk_companies_of_particular_lvl2_industry(view_change='recent', lvl2_industry_name="Industrials")   | Get low risk companies of particular lvl2_industry | GET/identifiers/companies/lowrisk/{view_change}?lvl2IndustryName={lvl2_industry_name}
get_low_risk_companies_of_particular_lvl3_industry(view_change='recent', lvl3_industry_name="Software")   | Get low risk companies of particular lvl3_industry | GET/identifiers/companies/lowrisk/{view_change}?lvl3IndustryName={lvl3_industry_name}
get_low_risk_companies_of_particular_lvl4_industry(view_change='recent', lvl4_industry_name="Healthcare Insurance")   | Get low risk companies of particular lvl4_industry | GET/identifiers/companies/lowrisk/{view_change}?lvl4IndustryName={lvl4_industry_name}
get_identifier_details(identifier="Metals")   | Get basic details about identifier | GET/identifiers/details/{identifier}
get_identifier_latest_spindex_score(identifier="Godaddy Inc (GDDY)")   | Get latest SPINDEX score of identifier | GET/identifiers/scores/{identifier}
get_company_latest_six_weeks_spindex_scores(company_name="Godaddy Inc (GDDY)"   | Get company 6 weeks SPINDEX score | GET/identifiers/company/{company_name}
get_identifier_compared_scores(identifiers="Godaddy Inc (GDDY)")   | Get compared scores for identifier | GET/identifiers/comparedscore/{identifier}
get_constituents_companies_with_latest_overallrisk(lvl4_industry_name="Metals")   | Get all companies with its current overallrisk for a particular lvl4_industry | GET/identifiers/industry/{lvl4_industry_name}
get_identifier_timeseries_overallrisk(identifier="Metals")   | Get whole timeseries overallrisk of identifier and group average | GET/identifiers/timeseries/overallrisk/{identifier}
get_industries_overview()   | Get overview of industry | GET/identifiers/industries/overview
get_companies_overview()   | Get overview of company | GET/companies/overview
get_all_level_industries_names()   | Get all level industries names | GET/industries/names

