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

