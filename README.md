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

All URIs are relative to *http://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*InvestmentResearchersApi* | [**bulk_mapping_get**](docs/InvestmentResearchersApi.md#bulk_mapping_get) | **GET** /bulk/mapping | BulkFileMapping
*InvestmentResearchersApi* | [**bulk_models_get**](docs/InvestmentResearchersApi.md#bulk_models_get) | **GET** /bulk/models | BulkFileModels
*InvestmentResearchersApi* | [**bulk_signals_get**](docs/InvestmentResearchersApi.md#bulk_signals_get) | **GET** /bulk/signals | BulkFileSignals
*InvestmentResearchersApi* | [**bulk_signals_yearly_get**](docs/InvestmentResearchersApi.md#bulk_signals_yearly_get) | **GET** /bulk/signals/yearly | BulkFileSignalsYearly
*InvestmentResearchersApi* | [**company_compass_report_pdf_ticker_get**](docs/InvestmentResearchersApi.md#company_compass_report_pdf_ticker_get) | **GET** /company/compass/reportPDF/{ticker} | CompassReportPDF
*InvestmentResearchersApi* | [**company_spinsights_report_pdf_ticker_get**](docs/InvestmentResearchersApi.md#company_spinsights_report_pdf_ticker_get) | **GET** /company/spinsights/reportPDF/{ticker} | SpinsightsReportPDF
*InvestmentResearchersApi* | [**generative_company_compass_question_content_ticker_get**](docs/InvestmentResearchersApi.md#generative_company_compass_question_content_ticker_get) | **GET** /generative/company/compass/questionContent/{ticker} | GetCompassExplorerQuestionAnswer
*InvestmentResearchersApi* | [**generative_company_compass_report_content_ticker_get**](docs/InvestmentResearchersApi.md#generative_company_compass_report_content_ticker_get) | **GET** /generative/company/compass/reportContent/{ticker} | GetCompassReportContent
*InvestmentResearchersApi* | [**generative_company_spinsights_explorer_content_ticker_get**](docs/InvestmentResearchersApi.md#generative_company_spinsights_explorer_content_ticker_get) | **GET** /generative/company/spinsights/explorerContent/{ticker} | GetSpinsightsExplorer
*InvestmentResearchersApi* | [**generative_company_spinsights_report_content_ticker_get**](docs/InvestmentResearchersApi.md#generative_company_spinsights_report_content_ticker_get) | **GET** /generative/company/spinsights/reportContent/{ticker} | GetSpinsightsReportContent
*InvestmentResearchersApi* | [**mapping_company_identifier_mapping_get**](docs/InvestmentResearchersApi.md#mapping_company_identifier_mapping_get) | **GET** /mapping/companyIdentifierMapping | MappingCompanyIdentifiers
*InvestmentResearchersApi* | [**mapping_compass_questions_get**](docs/InvestmentResearchersApi.md#mapping_compass_questions_get) | **GET** /mapping/compassQuestions | MappingCompassQuestions
*InvestmentResearchersApi* | [**mapping_spindex_factors_get**](docs/InvestmentResearchersApi.md#mapping_spindex_factors_get) | **GET** /mapping/spindexFactors | MappingSpindexFactors
*InvestmentResearchersApi* | [**models_spindex_get**](docs/InvestmentResearchersApi.md#models_spindex_get) | **GET** /models/spindex | ModelsSpindex
*InvestmentResearchersApi* | [**signals_quant_linguistics_get**](docs/InvestmentResearchersApi.md#signals_quant_linguistics_get) | **GET** /signals/quantLinguistics | SignalsQuantLinguistics


## Documentation For Models

 - [BulkMappingGet200Response](docs/BulkMappingGet200Response.md)
 - [BulkMappingGet200ResponseData](docs/BulkMappingGet200ResponseData.md)
 - [CompanyInfoModel](docs/CompanyInfoModel.md)
 - [CompanyMappingCompanyToSecurityModel](docs/CompanyMappingCompanyToSecurityModel.md)
 - [CompanySpinsightsReportPDFTickerGet404Response](docs/CompanySpinsightsReportPDFTickerGet404Response.md)
 - [CompanySpinsightsReportPDFTickerGet404ResponseErrorsInner](docs/CompanySpinsightsReportPDFTickerGet404ResponseErrorsInner.md)
 - [FactorLibraryCompassQuestionsModel](docs/FactorLibraryCompassQuestionsModel.md)
 - [FactorLibrarySpindexFactorsModel](docs/FactorLibrarySpindexFactorsModel.md)
 - [FileDownloadModel](docs/FileDownloadModel.md)
 - [FileDownloadModel1](docs/FileDownloadModel1.md)
 - [GenerativeCompanyCompassReportContentModel](docs/GenerativeCompanyCompassReportContentModel.md)
 - [GenerativeCompanyCompassReportContentModelCompassContent](docs/GenerativeCompanyCompassReportContentModelCompassContent.md)
 - [GenerativeCompanyQuestionAnswerModel](docs/GenerativeCompanyQuestionAnswerModel.md)
 - [GenerativeCompanyQuestionAnswerModelQuestionAnswerInner](docs/GenerativeCompanyQuestionAnswerModelQuestionAnswerInner.md)
 - [GenerativeCompanySpinsightsExplorerModel](docs/GenerativeCompanySpinsightsExplorerModel.md)
 - [GenerativeCompanySpinsightsExplorerModelSpinsightsExplorerInner](docs/GenerativeCompanySpinsightsExplorerModelSpinsightsExplorerInner.md)
 - [GenerativeCompanySpinsightsReportContentModel](docs/GenerativeCompanySpinsightsReportContentModel.md)
 - [GenerativeCompanySpinsightsReportContentModelSpinsightsContent](docs/GenerativeCompanySpinsightsReportContentModelSpinsightsContent.md)
 - [ModelsSpindexModel](docs/ModelsSpindexModel.md)
 - [ModelsSpindexSpindexModelInner](docs/ModelsSpindexSpindexModelInner.md)
 - [SignalsQuantLinguisticsModel](docs/SignalsQuantLinguisticsModel.md)
 - [SignalsQuantLinguisticsSignalsModelInner](docs/SignalsQuantLinguisticsSignalsModelInner.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="bearer"></a>
### bearer

- **Type**: Bearer authentication


## Author
