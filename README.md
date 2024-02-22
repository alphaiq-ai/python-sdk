# AlphaIQ Python SDK
To get access to the API, [sign up here](https://alphaiq.ai).

Welcome to the AlphaIQ API! We offer Quantitative Linguistic Risk Indicators that enable investors to uncover hidden risks in forward-looking statements from management.

To learn more about AlphaIQ, [read about us](https://alphaiq.ai/about-faq).

Review the [Privacy Policy](https://alphaiq.ai/privacy-policy/) and [Terms of Service](https://alphaiq.ai/terms-of-service/) on our website.

# Installation
## Requirements.

Python 2.7 and 3.4+

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

## Installation via Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import openapi_client
```

# Getting Started

It is advised to setup a ```.env``` file the store credentials. Documentation can be found [here](https://pypi.org/project/python-dotenv/). To use the ```.env``` file to store credentials, install the ```python-dotenv``` package with pip:

```python
pip install python-dotenv
```

An example of the contents of the ```.env``` file are shown below:

```
EMAIL=example@emaildomain.com
PASSWORD=VGhpcyBpcyBteSBwYXNzd29yZCBlbmNvZGVkIHRvIEJhc2U2NCBmb3JtYXQ=
```

Please follow the [installation procedure](#installation) and then run the following to retrieve your bearer token for authentication to other API routes:

```python
import os

from dotenv import load_dotenv
import openapi_client

# Load the environment variables from the .env file
load_dotenv()

EMAIL = os.getenv('EMAIL')
PASSWORD = os.getenv('PASSWORD')

# Define the API configuration, client object and API instance
configuration = openapi_client.Configuration(
    host = 'https://eofipoxzab.execute-api.us-east-1.amazonaws.com/v1'
    )

api_client = openapi_client.ApiClient(configuration)

auth_api_instance = openapi_client.AlphaiqWebsiteAuthApi(api_client)

# Define the values needed to authenticate to the API
content_type = 'application/json' # str | 
inline_object = openapi_client.InlineObject(
    email = EMAIL,
    password = PASSWORD
)

# Authenticate using your credentials
auth_response = auth_api_instance.auth_gettoken_post(
    content_type = content_type,
    inline_object=inline_object
    )

# Extract your bearer token for authentication to other API paths
id_token = auth_response.data.id_token

```

## Documentation for API Endpoints

All URIs are relative to *https://data.app.alphaiq.ai/api/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*InvestmentResearchersApi* | [**auth_gettoken_post**](docs/InvestmentResearchersApi.md#auth_gettoken_post) | **POST** /auth/gettoken | GetToken
*InvestmentResearchersApi* | [**auth_refreshtoken_post**](docs/InvestmentResearchersApi.md#auth_refreshtoken_post) | **POST** /auth/refreshtoken | RefreshToken
*InvestmentResearchersApi* | [**company_mapping_company_to_security_get**](docs/InvestmentResearchersApi.md#company_mapping_company_to_security_get) | **GET** /company-mapping/company-to-security | CompanyToSecurity
*InvestmentResearchersApi* | [**company_spindex_get_latest_spindex_factors_get**](docs/InvestmentResearchersApi.md#company_spindex_get_latest_spindex_factors_get) | **GET** /company-spindex/getLatestSpindexFactors | GetLatestSpindexFactors
*InvestmentResearchersApi* | [**company_spindex_get_latest_spindex_overall_risk_get**](docs/InvestmentResearchersApi.md#company_spindex_get_latest_spindex_overall_risk_get) | **GET** /company-spindex/getLatestSpindexOverallRisk | GetLatestSpindexOverallRisk
*InvestmentResearchersApi* | [**company_spindex_get_timeseries_spindex_factors_get**](docs/InvestmentResearchersApi.md#company_spindex_get_timeseries_spindex_factors_get) | **GET** /company-spindex/getTimeseriesSpindexFactors | GetTimeseriesSpindexFactors
*InvestmentResearchersApi* | [**company_spindex_get_timeseries_spindex_overall_risk_get**](docs/InvestmentResearchersApi.md#company_spindex_get_timeseries_spindex_overall_risk_get) | **GET** /company-spindex/getTimeseriesSpindexOverallRisk | GetTimeseriesSpindexOverallRisk
*InvestmentResearchersApi* | [**factor_library_compass_questions_get**](docs/InvestmentResearchersApi.md#factor_library_compass_questions_get) | **GET** /factor-library/compass-questions | GetCompassQuestions
*InvestmentResearchersApi* | [**factor_library_spindex_factors_get**](docs/InvestmentResearchersApi.md#factor_library_spindex_factors_get) | **GET** /factor-library/spindex-factors | GetSpindexFactors
*InvestmentResearchersApi* | [**generative_company_compass_report_content_ticker_get**](docs/InvestmentResearchersApi.md#generative_company_compass_report_content_ticker_get) | **GET** /generative/company/compass/reportContent/{ticker} | GetCompassReportContent
*InvestmentResearchersApi* | [**generative_company_question_answer_ticker_get**](docs/InvestmentResearchersApi.md#generative_company_question_answer_ticker_get) | **GET** /generative/company/questionAnswer/{ticker} | GetCompassExplorerQuestionAnswer
*InvestmentResearchersApi* | [**generative_company_spinsights_explorer_ticker_get**](docs/InvestmentResearchersApi.md#generative_company_spinsights_explorer_ticker_get) | **GET** /generative/company/spinsights/explorer/{ticker} | GetSpinsightsExplorer
*InvestmentResearchersApi* | [**generative_company_spinsights_report_content_ticker_get**](docs/InvestmentResearchersApi.md#generative_company_spinsights_report_content_ticker_get) | **GET** /generative/company/spinsights/reportContent/{ticker} | GetSpinsightsReportContent


## Documentation For Models

 - [Category](docs/Category.md)
 - [InlineObject](docs/InlineObject.md)
 - [InlineObject1](docs/InlineObject1.md)
 - [InlineObject2](docs/InlineObject2.md)
 - [InlineObject3](docs/InlineObject3.md)
 - [InlineObject4](docs/InlineObject4.md)
 - [InlineResponse200](docs/InlineResponse200.md)
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
 - [InlineResponse20020](docs/InlineResponse20020.md)
 - [InlineResponse20020Data](docs/InlineResponse20020Data.md)
 - [InlineResponse20021](docs/InlineResponse20021.md)
 - [InlineResponse20021Data](docs/InlineResponse20021Data.md)
 - [InlineResponse20022](docs/InlineResponse20022.md)
 - [InlineResponse20022Data](docs/InlineResponse20022Data.md)
 - [InlineResponse20023](docs/InlineResponse20023.md)
 - [InlineResponse20023Data](docs/InlineResponse20023Data.md)
 - [InlineResponse20024](docs/InlineResponse20024.md)
 - [InlineResponse20024Data](docs/InlineResponse20024Data.md)
 - [InlineResponse20024DataSpinsightsContent](docs/InlineResponse20024DataSpinsightsContent.md)
 - [InlineResponse20025](docs/InlineResponse20025.md)
 - [InlineResponse20025Data](docs/InlineResponse20025Data.md)
 - [InlineResponse20025DataCompassContent](docs/InlineResponse20025DataCompassContent.md)
 - [InlineResponse20026](docs/InlineResponse20026.md)
 - [InlineResponse20026Data](docs/InlineResponse20026Data.md)
 - [InlineResponse20026DataQuestionAnswer](docs/InlineResponse20026DataQuestionAnswer.md)
 - [InlineResponse20027](docs/InlineResponse20027.md)
 - [InlineResponse20027Data](docs/InlineResponse20027Data.md)
 - [InlineResponse20028](docs/InlineResponse20028.md)
 - [InlineResponse20028Data](docs/InlineResponse20028Data.md)
 - [InlineResponse20029](docs/InlineResponse20029.md)
 - [InlineResponse20029Data](docs/InlineResponse20029Data.md)
 - [InlineResponse2002Data](docs/InlineResponse2002Data.md)
 - [InlineResponse2002DataQuestionContext](docs/InlineResponse2002DataQuestionContext.md)
 - [InlineResponse2002DataQuestions](docs/InlineResponse2002DataQuestions.md)
 - [InlineResponse2003](docs/InlineResponse2003.md)
 - [InlineResponse2003Data](docs/InlineResponse2003Data.md)
 - [InlineResponse2003DataSpinsightsExplorer](docs/InlineResponse2003DataSpinsightsExplorer.md)
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
 - [InlineResponse200Data](docs/InlineResponse200Data.md)
 - [InlineResponse405](docs/InlineResponse405.md)
 - [InlineResponse405Errors](docs/InlineResponse405Errors.md)
 - [Pet](docs/Pet.md)
 - [Tag](docs/Tag.md)
