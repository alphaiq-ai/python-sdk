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

It is advised to setup a ```.env``` file the store API key. Documentation can be found [here](https://pypi.org/project/python-dotenv/). To use the ```.env``` file to store credentials, install the ```python-dotenv``` package with pip:

```python
pip install python-dotenv
```

An example of the contents of the ```.env``` file are shown below:

```
APIKEY=keytoken123
```

Please follow the [installation procedure](#installation) and then you are ready to get started.

```python
import os
from dotenv import load_dotenv
import alphaiq_sdk

# Load the environment variables from the .env file
load_dotenv()
APIKEY = os.getenv('APIKEY')
client = alphaiq_sdk.client(APIKEY)

## get_quant_linguistics_signals
def get_quant_linguistics_signals():
    client = alphaiq_sdk.client(APIKEY)
    ticker='TSLA'
    startDate='2023-03-01'
    endDate='2023-05-01'

    response = client.get_quant_linguistics_signals(startDate,endDate,ticker=ticker)

    return response
```

## Documentation for API Endpoints

All URIs are relative to *https://data.app.alphaiq.ai/api/v1/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_quant_linguistics_signals**](docs/InvestmentResearchersApi.md#get_quant_linguistics_signals) | **GET** /signals/quantLinguistics | SignalsQuantLinguistics
[**get_bulk_signals**](docs/InvestmentResearchersApi.md#get_bulk_signals) | **GET** /bulk/signals | BulkFileSignals
[**get_bulk_signals_yearly**](docs/InvestmentResearchersApi.md#get_bulk_signals_yearly) | **GET** /bulk/signals/yearly | BulkFileSignalsYearly
[**get_models_spindex**](docs/InvestmentResearchersApi.md#get_models_spindex) | **GET** /models/spindex | ModelsSpindex
[**get_bulk_model**](docs/InvestmentResearchersApi.md#get_bulk_model) | **GET** /bulk/models | BulkFileModels
[**get_company_identifiers**](docs/InvestmentResearchersApi.md#get_company_identifiers) | **GET** /mapping/companyIdentifierMapping | MappingCompanyIdentifiers
[**get_compass_questions**](docs/InvestmentResearchersApi.md#get_compass_questions) | **GET** /mapping/compassQuestions | MappingCompassQuestions
[**get_spindex_factors**](docs/InvestmentResearchersApi.md#get_spindex_factors) | **GET** /mapping/spindexFactors | MappingSpindexFactors
[**get_bulk_mapping**](docs/InvestmentResearchersApi.md#get_bulk_mapping) | **GET** /bulk/mapping | BulkFileMapping
[**get_spinsights_explorer_spindex_summary**](docs/InvestmentResearchersApi.md#get_spinsights_explorer_spindex_summary) | **GET** /generative/company/spinsights/explorerContent/{ticker} | GetSpinsightsExplorerSpindexSummary
[**get_spinsights_report_content**](docs/InvestmentResearchersApi.md#get_spinsights_report_content) | **GET** /generative/company/spinsights/reportContent/{ticker} | GetSpinsightsReportContent
[**get_spinsights_report_pdf**](docs/InvestmentResearchersApi.md#get_spinsights_report_pdf) | **GET** /company/spinsights/reportPDF/{ticker} | SpinsightsReportPDF
[**get_compass_explorer_question_answer**](docs/InvestmentResearchersApi.md#get_compass_explorer_question_answer) | **GET** /generative/company/compass/questionContent/{ticker} | GetCompassExplorerQuestionAnswer
[**get_compass_report_content**](docs/InvestmentResearchersApi.md#get_compass_report_content) | **GET** /generative/company/compass/reportContent/{ticker} | GetCompassReportContent
[**get_compass_report_pdf**](docs/InvestmentResearchersApi.md#get_compass_report_pdf) | **GET** /company/compass/reportPDF/{ticker} | CompassReportPDF

## Documentation For Models

 - [CompanyInfoModel](docs/CompanyInfoModel.md)
 - [CompanyInfoModel1](docs/CompanyInfoModel1.md)
 - [FactorLibrarySpindexFactorsDataItems](docs/FactorLibrarySpindexFactorsDataItems.md)
 - [FileDownloadModel](docs/FileDownloadModel.md)
 - [FileDownloadModel1](docs/FileDownloadModel1.md)
 - [FileDownloadModelData](docs/FileDownloadModelData.md)
 - [FileDownloadModelData1](docs/FileDownloadModelData1.md)
 - [GenerativeCompanyCompassReportContentModel](docs/GenerativeCompanyCompassReportContentModel.md)
 - [GenerativeCompanyCompassReportContentModelData](docs/GenerativeCompanyCompassReportContentModelData.md)
 - [GenerativeCompanyCompassReportContentModelDataCompassContent](docs/GenerativeCompanyCompassReportContentModelDataCompassContent.md)
 - [GenerativeCompanyQuestionAnswerModel](docs/GenerativeCompanyQuestionAnswerModel.md)
 - [GenerativeCompanyQuestionAnswerModelData](docs/GenerativeCompanyQuestionAnswerModelData.md)
 - [GenerativeCompanyQuestionAnswerModelDataQuestionAnswerItems](docs/GenerativeCompanyQuestionAnswerModelDataQuestionAnswerItems.md)
 - [GenerativeCompanySpinsightsExplorerModel](docs/GenerativeCompanySpinsightsExplorerModel.md)
 - [GenerativeCompanySpinsightsExplorerModelData](docs/GenerativeCompanySpinsightsExplorerModelData.md)
 - [GenerativeCompanySpinsightsExplorerModelDataSpinsightsExplorerItems](docs/GenerativeCompanySpinsightsExplorerModelDataSpinsightsExplorerItems.md)
 - [GenerativeCompanySpinsightsReportContentModel](docs/GenerativeCompanySpinsightsReportContentModel.md)
 - [GenerativeCompanySpinsightsReportContentModelData](docs/GenerativeCompanySpinsightsReportContentModelData.md)
 - [GenerativeCompanySpinsightsReportContentModelDataSpinsightsContent](docs/GenerativeCompanySpinsightsReportContentModelDataSpinsightsContent.md)
 - [MappingCompanyIdentifierMappingModel](docs/MappingCompanyIdentifierMappingModel.md)
 - [MappingCompanyIdentifierMappingModelDataItems](docs/MappingCompanyIdentifierMappingModelDataItems.md)
 - [MappingCompassQuestionsModel](docs/MappingCompassQuestionsModel.md)
 - [MappingCompassQuestionsModelDataItems](docs/MappingCompassQuestionsModelDataItems.md)
 - [MappingSpindexFactorsModel](docs/MappingSpindexFactorsModel.md)
 - [ModelsSpindexModel](docs/ModelsSpindexModel.md)
 - [ModelsSpindexModelData](docs/ModelsSpindexModelData.md)
 - [ModelsSpindexModelItems](docs/ModelsSpindexModelItems.md)
 - [SignalsQuantLinguisticsModelData](docs/SignalsQuantLinguisticsModelData.md)
 - [SignalsQuantLinguisticsModelRoot](docs/SignalsQuantLinguisticsModelRoot.md)
 - [SignalsQuantLinguisticsSignalsModel2](docs/SignalsQuantLinguisticsSignalsModel2.md)

# bearer

Authorization is a bearer token. That bearer token is your API key.