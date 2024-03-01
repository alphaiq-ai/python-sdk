# AlphaIQ Python SDK
To get access to the API, [sign up here](https://alphaiq.ai).

Welcome to the AlphaIQ API! We offer Quantitative Linguistic Risk Indicators that enable investors to uncover hidden risks in forward-looking statements from management.

To learn more about AlphaIQ, [read about us](https://alphaiq.ai/about-faq).

Review the [Privacy Policy](https://alphaiq.ai/privacy-policy/) and [Terms of Service](https://alphaiq.ai/terms-of-service/) on our website.

# Installation
## Requirements.

Python 3.9+

## Installation via Pip

```sh
pip install alphaiq-sdk
```

Then import the package:

```python
import alphaiq_sdk 
```

## Installation via GitHub

```sh
pip install git+https://github.com/alphaiq-ai/python-sdk.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/alphaiq-ai/python-sdk.git`)

Then import the package:
```python
import alphaiq_sdk
```

# Getting Started

It is advised to setup a ```.env``` file the store credentials. Documentation can be found [here](https://pypi.org/project/python-dotenv/). To use the ```.env``` file to store credentials, install the ```python-dotenv``` package with pip:

```python
pip install python-dotenv
```

An example of the contents of the ```.env``` file are shown below:
Note: The password should be Base64 encoded. Encoder can be found [here](https://www.base64encode.org/). 

```
EMAIL=example@emaildomain.com
PASSWORD=VGhpcyBpcyBteSBwYXNzd29yZCBlbmNvZGVkIHRvIEJhc2U2NCBmb3JtYXQ=
```

Please follow the [installation procedure](#installation) and then run the following to retrieve your bearer token for authentication to other API routes:

```python
import os

from dotenv import load_dotenv
import alphaiq_sdk
from alphaiq_sdk.rest import ApiException

# Load the environment variables from the .env file
load_dotenv()

EMAIL = os.getenv('EMAIL')
PASSWORD = os.getenv('PASSWORD')

# Define the API configuration, client object and API instance
configuration = alphaiq_sdk.Configuration(
    host = 'https://data.app.alphaiq.ai/api/v1'
    )

with alphaiq_sdk.ApiClient(configuration) as api_client:

    # Make an instance of the API class
    api_instance = alphaiq_sdk.InvestmentResearchersApi(api_client)

    # Define the values needed to authenticate to the API
    content_type = 'application/json' # str | 
    inline_object = alphaiq_sdk.InlineObject(
        email = EMAIL,
        password = PASSWORD
    )

    try:

        # Authenticate using your credentials
        api_response = api_instance.auth_gettoken_post(
            content_type = content_type,
            inline_object=inline_object
            )

    except ApiException as e:

        # Log an exception if it occurs
        print("Exception when calling the API: %s\n" % e)

    # Extract your bearer token for authentication to other API paths
    id_token = api_response.data.id_token

    # Add the bearer token to the configuration for authenticating other routes
    setattr(configuration, 'access_token', id_token)
```

## Documentation for API Endpoints

All URIs are relative to *https://data.app.alphaiq.ai/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**company_spindex_get_latest_spindex_overall_risk_get**](docs/InvestmentResearchersApi.md#company_spindex_get_latest_spindex_overall_risk_get) | **GET** /company-spindex/getLatestSpindexOverallRisk | Get Latest Spindex Overall Risk
[**company_spindex_get_timeseries_spindex_overall_risk_get**](docs/InvestmentResearchersApi.md#company_spindex_get_timeseries_spindex_overall_risk_get) | **GET** /company-spindex/getTimeseriesSpindexOverallRisk | Get Timeseries Spindex Overall Risk
[**company_spindex_get_latest_spindex_factors_get**](docs/InvestmentResearchersApi.md#company_spindex_get_latest_spindex_factors_get) | **GET** /company-spindex/getLatestSpindexFactors | Get Latest Spindex Factors
[**company_spindex_get_timeseries_spindex_factors_get**](docs/InvestmentResearchersApi.md#company_spindex_get_timeseries_spindex_factors_get) | **GET** /company-spindex/getTimeseriesSpindexFactors | Get Timeseries Spindex Factors
[**generative_company_spinsights_explorer_ticker_get**](docs/InvestmentResearchersApi.md#generative_company_spinsights_explorer_ticker_get) | **GET** /generative/company/spinsights/explorer/{ticker} | Get Spinsights Explorer
[**generative_company_question_answer_ticker_get**](docs/InvestmentResearchersApi.md#generative_company_question_answer_ticker_get) | **GET** /generative/company/questionAnswer/{ticker} | Get Compass Explorer Question Answer
[**generative_company_spinsights_report_content_ticker_get**](docs/InvestmentResearchersApi.md#generative_company_spinsights_report_content_ticker_get) | **GET** /generative/company/spinsights/reportContent/{ticker} | Get Spinsights Report Content
[**generative_company_compass_report_content_ticker_get**](docs/InvestmentResearchersApi.md#generative_company_compass_report_content_ticker_get) | **GET** /generative/company/compass/reportContent/{ticker} | Get Compass Report Content
[**company_spinsights_report_ticker_get**](docs/InvestmentResearchersApi.md#company_spinsights_report_ticker_get) | **GET** /company/spinsights/report/{ticker} | Spinsights Report PDF
[**company_compass_report_ticker_get**](docs/InvestmentResearchersApi.md#company_compass_report_ticker_get) | **GET** /company/compass/report/{ticker} | Compass Report PDF
[**factor_library_spindex_factors_get**](docs/InvestmentResearchersApi.md#factor_library_spindex_factors_get) | **GET** /factor-library/spindex-factors | Get Spindex Factors
[**factor_library_compass_questions_get**](docs/InvestmentResearchersApi.md#factor_library_compass_questions_get) | **GET** /factor-library/compass-questions | Get Compass Questions
[**company_mapping_company_to_security_get**](docs/InvestmentResearchersApi.md#company_mapping_company_to_security_get) | **GET** /company-mapping/company-to-security | Company To Security
[**auth_gettoken_post**](docs/InvestmentResearchersApi.md#auth_gettoken_post) | **POST** /auth/gettoken | Get Token

## Documentation For Models

 - [Category](docs/Category.md)
 - [InlineObject](docs/InlineObject.md)
 - [InlineObject1](docs/InlineObject1.md)
 - [InlineObject2](docs/InlineObject2.md)
 - [InlineObject3](docs/InlineObject3.md)
 - [InlineObject4](docs/InlineObject4.md)
 - [CompanyCompassReport](docs/CompanyCompassReport.md)
 - [InlineResponse2001](docs/InlineResponse2001.md)
 - [InlineResponse20010](docs/InlineResponse20010.md)
 - [InlineResponse20010Data](docs/InlineResponse20010Data.md)
 - [InlineResponse20011](docs/InlineResponse20011.md)
 - [InlineResponse20011Data](docs/InlineResponse20011Data.md)
 - [InlineResponse20011DataLvl2IndustriesWithLatestAvgOverallrisk](docs/InlineResponse20011DataLvl2IndustriesWithLatestAvgOverallrisk.md)
 - [InlineResponse20011DataLvl3IndustriesWithLatestAvgOverallrisk](docs/InlineResponse20011DataLvl3IndustriesWithLatestAvgOverallrisk.md)
 - [InlineResponse20012](docs/InlineResponse20012.md)
 - [InlineResponse20012ConsumerProductsAndServices](docs/InlineResponse20012ConsumerProductsAndServices.md)
 - [InlineResponse20012Data](docs/InlineResponse20012Data.md)
 - [InlineResponse20012Energy](docs/InlineResponse20012Energy.md)
 - [InlineResponse20012Financials](docs/InlineResponse20012Financials.md)
 - [InlineResponse20012Food](docs/InlineResponse20012Food.md)
 - [InlineResponse20012Healthcare](docs/InlineResponse20012Healthcare.md)
 - [InlineResponse20012Industrials](docs/InlineResponse20012Industrials.md)
 - [InlineResponse20012Information](docs/InlineResponse20012Information.md)
 - [InlineResponse20012InformationTools](docs/InlineResponse20012InformationTools.md)
 - [InlineResponse20013](docs/InlineResponse20013.md)
 - [InlineResponse20013Data](docs/InlineResponse20013Data.md)
 - [InlineResponse20014](docs/InlineResponse20014.md)
 - [InlineResponse20014Data](docs/InlineResponse20014Data.md)
 - [InlineResponse20015](docs/InlineResponse20015.md)
 - [InlineResponse20015Data](docs/InlineResponse20015Data.md)
 - [InlineResponse20016](docs/InlineResponse20016.md)
 - [InlineResponse20016Company1](docs/InlineResponse20016Company1.md)
 - [InlineResponse20016Data](docs/InlineResponse20016Data.md)
 - [InlineResponse20017](docs/InlineResponse20017.md)
 - [InlineResponse20017Data](docs/InlineResponse20017Data.md)
 - [InlineResponse20018](docs/InlineResponse20018.md)
 - [InlineResponse20018Data](docs/InlineResponse20018Data.md)
 - [InlineResponse20018DataChevronCorpCVX](docs/InlineResponse20018DataChevronCorpCVX.md)
 - [InlineResponse20019](docs/InlineResponse20019.md)
 - [InlineResponse2001Data](docs/InlineResponse2001Data.md)
 - [InlineResponse2002](docs/InlineResponse2002.md)
 - [CompanySpinsightsReport](docs/CompanySpinsightsReport.md)
 - [CompanySpinsightsReportData](docs/CompanySpinsightsReportData.md)
 - [InlineResponse20021](docs/InlineResponse20021.md)
 - [InlineResponse20021Data](docs/InlineResponse20021Data.md)
 - [TimeseriesCompanySpindex](docs/TimeseriesCompanySpindex.md)
 - [TimeseriesCompanySpindexData](docs/TimeseriesCompanySpindexData.md)
 - [InlineRecentCompanySpindex](docs/InlineRecentCompanySpindex.md)
 - [InlineRecentCompanySpindexData](docs/InlineRecentCompanySpindexData.md)
 - [CompanySpinsightsReportContent](docs/CompanySpinsightsReportContent.md)
 - [CompanySpinsightsReportContentData](docs/CompanySpinsightsReportContentData.md)
 - [CompanySpinsightsReportContentDataSpinsightsContent](docs/CompanySpinsightsReportContentDataSpinsightsContent.md)
 - [CompanyCompassReportContent](docs/CompanyCompassReportContent.md)
 - [CompanyCompassReportContentData](docs/CompanyCompassReportContentData.md)
 - [CompanyCompassReportContentDataCompassContent](docs/CompanyCompassReportContentDataCompassContent.md)
 - [CompanyQuestionAnswer](docs/CompanyQuestionAnswer.md)
 - [CompanyQuestionAnswerData](docs/CompanyQuestionAnswerData.md)
 - [CompanyQuestionAnswerDataQuestionAnswer](docs/CompanyQuestionAnswerDataQuestionAnswer.md)
 - [CompanyMappingCompanyToSecurity](docs/CompanyMappingCompanyToSecurity.md)
 - [CompanyMappingCompanyToSecurityData](docs/CompanyMappingCompanyToSecurityData.md)
 - [FactorLibrarySpindexFactors](docs/FactorLibrarySpindexFactors.md)
 - [FactorLibrarySpindexFactorsData](docs/FactorLibrarySpindexFactorsData.md)
 - [FactorLibraryCompassQuestions](docs/FactorLibraryCompassQuestions.md)
 - [FactorLibraryCompassQuestionsData](docs/FactorLibraryCompassQuestionsData.md)
 - [InlineResponse2002Data](docs/InlineResponse2002Data.md)
 - [InlineResponse2002DataQuestionContext](docs/InlineResponse2002DataQuestionContext.md)
 - [InlineResponse2002DataQuestions](docs/InlineResponse2002DataQuestions.md)
 - [CompanySpinsightsExplorer](docs/CompanySpinsightsExplorer.md)
 - [CompanySpinsightsExplorerData](docs/CompanySpinsightsExplorerData.md)
 - [CompanySpinsightsExplorerDataSpinsightsExplorer](docs/CompanySpinsightsExplorerDataSpinsightsExplorer.md)
 - [InlineResponse2004](docs/InlineResponse2004.md)
 - [InlineResponse2005](docs/InlineResponse2005.md)
 - [InlineResponse2005Data](docs/InlineResponse2005Data.md)
 - [InlineResponse2006](docs/InlineResponse2006.md)
 - [InlineResponse2007](docs/InlineResponse2007.md)
 - [InlineResponse2007Data](docs/InlineResponse2007Data.md)
 - [InlineResponse2007DataHighRiskCompanies](docs/InlineResponse2007DataHighRiskCompanies.md)
 - [InlineResponse2008](docs/InlineResponse2008.md)
 - [InlineResponse2008Data](docs/InlineResponse2008Data.md)
 - [InlineResponse2008DataFinancials](docs/InlineResponse2008DataFinancials.md)
 - [InlineResponse2008DataFinancialsDrillDownIndustriesDetails](docs/InlineResponse2008DataFinancialsDrillDownIndustriesDetails.md)
 - [InlineResponse2008DataFinancialsRealEstate](docs/InlineResponse2008DataFinancialsRealEstate.md)
 - [InlineResponse2008DataFinancialsRealEstateDrillDownIndustriesDetails](docs/InlineResponse2008DataFinancialsRealEstateDrillDownIndustriesDetails.md)
 - [InlineResponse2008DataFinancialsRealEstateRealEstateRental](docs/InlineResponse2008DataFinancialsRealEstateRealEstateRental.md)
 - [InlineResponse2008DataFinancialsRealEstateRealEstateRentalHighRiskCompanies](docs/InlineResponse2008DataFinancialsRealEstateRealEstateRentalHighRiskCompanies.md)
 - [InlineResponse2008DataIndustriesDetails](docs/InlineResponse2008DataIndustriesDetails.md)
 - [InlineResponse2009](docs/InlineResponse2009.md)
 - [InlineResponse2009Data](docs/InlineResponse2009Data.md)
 - [InlineResponse2009DataHighriskIndustries](docs/InlineResponse2009DataHighriskIndustries.md)
 - [CompanyCompassReportData](docs/CompanyCompassReportData.md)
 - [InlineResponse405](docs/InlineResponse405.md)
 - [InlineResponse405Errors](docs/InlineResponse405Errors.md)
