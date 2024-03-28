# openapi_client.InvestmentResearchersApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_quant_linguistics_signals**](InvestmentResearchersApi.md#get_quant_linguistics_signals) | **GET** /signals/quantLinguistics | SignalsQuantLinguistics
[**get_bulk_signals**](InvestmentResearchersApi.md#get_bulk_signals) | **GET** /bulk/signals | BulkFileSignals
[**get_bulk_signals_yearly**](InvestmentResearchersApi.md#get_bulk_signals_yearly) | **GET** /bulk/signals/yearly | BulkFileSignalsYearly
[**get_models_spindex**](InvestmentResearchersApi.md#get_models_spindex) | **GET** /models/spindex | ModelsSpindex
[**get_bulk_model**](InvestmentResearchersApi.md#get_bulk_model) | **GET** /bulk/models | BulkFileModels
[**get_company_identifiers**](InvestmentResearchersApi.md#get_company_identifiers) | **GET** /mapping/companyIdentifierMapping | MappingCompanyIdentifiers
[**get_compass_questions**](InvestmentResearchersApi.md#get_compass_questions) | **GET** /mapping/compassQuestions | MappingCompassQuestions
[**get_spindex_factors**](InvestmentResearchersApi.md#get_spindex_factors) | **GET** /mapping/spindexFactors | MappingSpindexFactors
[**get_bulk_mapping**](InvestmentResearchersApi.md#get_bulk_mapping) | **GET** /bulk/mapping | BulkFileMapping
[**get_spinsights_explorer_spindex_summary**](InvestmentResearchersApi.md#get_spinsights_explorer_spindex_summary) | **GET** /generative/company/spinsights/explorerContent/{ticker} | GetSpinsightsExplorerSpindexSummary
[**get_spinsights_report_content**](InvestmentResearchersApi.md#get_spinsights_report_content) | **GET** /generative/company/spinsights/reportContent/{ticker} | GetSpinsightsReportContent
[**get_spinsights_report_pdf**](InvestmentResearchersApi.md#get_spinsights_report_pdf) | **GET** /company/spinsights/reportPDF/{ticker} | SpinsightsReportPDF
[**get_compass_explorer_question_answer**](InvestmentResearchersApi.md#get_compass_explorer_question_answer) | **GET** /generative/company/compass/questionContent/{ticker} | GetCompassExplorerQuestionAnswer
[**get_compass_report_content**](InvestmentResearchersApi.md#get_compass_report_content) | **GET** /generative/company/compass/reportContent/{ticker} | GetCompassReportContent
[**get_compass_report_pdf**](InvestmentResearchersApi.md#get_compass_report_pdf) | **GET** /company/compass/reportPDF/{ticker} | CompassReportPDF

# **get_quant_linguistics_signals**
> SignalsQuantLinguisticsModelRoot get_quant_linguistics_signals(start_date, end_date, consilience_id=consilience_id, ticker=ticker, cik=cik, lei=lei, isin=isin, cusip=cusip, sedol=sedol)

SignalsQuantLinguistics

Provides a signal for each of the Quantitative Linguistics signal groupings. These signals represent the aggregation of all the underlying signals. Query using one and only one nof the company identifiers (ConsilienceId, Ticker, CIK, LEI, ISIN, CUSIP, SEDOL). Note: currently a sample dataset for 2023 only.

### Example

* Bearer Authentication (bearer):

```python
import os
from dotenv import load_dotenv
import alphaiq_sdk

# Load the environment variables from the .env file
load_dotenv()
APIKEY = os.getenv('APIKEY')
client = alphaiq_sdk.client(APIKEY)

ticker='TSLA'
startDate='2023-03-01'
endDate='2023-05-01'

response = client.get_quant_linguistics_signals(startDate,endDate,ticker=ticker)

print(response)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**| Starting date of desired timeseries (YYYY-MM-DD) | 
 **end_date** | **str**| Ending date of desired timeseries (YYYY-MM-DD) | 
 **consilience_id** | **str**| Internal custom company identifier | [optional] 
 **ticker** | **str**| Ticker of the company/security | [optional] 
 **cik** | **str**| Central indexing key (CIK) used by SEC&#39;s EDGAR database | [optional] 
 **lei** | **str**| Legal entity identifier (LEI) | [optional] 
 **isin** | [**List[str]**](str.md)| International Securities Identification Number (ISIN) | [optional] 
 **cusip** | **str**| Committee on Uniform Securities Identification Procedures (CUSIP) | [optional] 
 **sedol** | **str**| Stock exchange daily official list (SEDOL) | [optional] 

### Return type

[**SignalsQuantLinguisticsModelRoot**](SignalsQuantLinguisticsModelRoot.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)



# **get_bulk_signals**
> FileDownloadModel1 get_bulk_signals(strategy_type)

BulkFileSignals

Delivers historical signal data files (2013-2023) as a zipped folder of gzipped csv files. Delivered as a temporary download link. Files determined based on signal strategy type (long, short, longshort).

### Example

* Bearer Authentication (bearer):

```python
import os
from dotenv import load_dotenv
import alphaiq_sdk

# Load the environment variables from the .env file
load_dotenv()
APIKEY = os.getenv('APIKEY')
client = alphaiq_sdk.client(APIKEY)

strategyType = 'long'

response = client.get_bulk_signals(strategyType)

print(response)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **strategy_type** | **str**| Type of strategy signals are used for (\&quot;long\&quot;, \&quot;short\&quot;, \&quot;longshort\&quot;) | 

### Return type

[**FileDownloadModel1**](FileDownloadModel1.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# **get_bulk_signals_yearly**
> FileDownloadModel1 get_bulk_signals_yearly(strategy_type, alpha_horizon, year)

BulkFileSignalsYearly

Delivers yearly signal files as a gzipped csv files. Delivered as a temporary download link. Files determined based on year, alpha horizon (4 week increments between 4 and 52 weeks) and signal strategy type (long, short, longshort).

### Example

* Bearer Authentication (bearer):

```python
import os
from dotenv import load_dotenv
import alphaiq_sdk

# Load the environment variables from the .env file
load_dotenv()
APIKEY = os.getenv('APIKEY')
client = alphaiq_sdk.client(APIKEY)

strategyType = 'long'
alphaHorizon = '4-week'
year=2023

response = client.get_bulk_signals_yearly(strategyType, alphaHorizon, year)
print(response)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **strategy_type** | **str**| Type of strategy signals are used for (\&quot;long\&quot;, \&quot;short\&quot;, \&quot;longshort\&quot;) | 
 **alpha_horizon** | **str**| 4-week investment horizon intervals from 4-week to 52-week (e.g. \&quot;4-week\&quot;, \&quot;8-week\&quot;, \&quot;12-week\&quot;) | 
 **year** | **str**| Year of historical signals between 2014-2023 | 

### Return type

[**FileDownloadModel1**](FileDownloadModel1.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# **get_models_spindex**
> ModelsSpindexModel get_models_spindex(raw_smooth_flag, start_date, end_date, consilience_id=consilience_id, ticker=ticker, cik=cik, lei=lei, isin=isin, cusip=cusip, sedol=sedol)

ModelsSpindex

Delivers SPINDEX scores for a variety of company identifiers (ConsilienceId, Ticker, CIK, LEI, ISIN, CUSIP, SEDOL). Provides the raw or smooth version of the model.

### Example

* Bearer Authentication (bearer):

```python
import os
from dotenv import load_dotenv
import alphaiq_sdk

# Load the environment variables from the .env file
load_dotenv()
APIKEY = os.getenv('APIKEY')
client = alphaiq_sdk.client(APIKEY)

ticker='TSLA'
rawSmoothFlag = 'raw'
startDate='2023-03-01'
endDate='2023-05-01'

response = client.get_models_spindex(rawSmoothFlag,startDate,endDate,ticker=ticker)
print(response)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **raw_smooth_flag** | **str**| Flag for raw or smooth version of the model (\&quot;raw\&quot;, \&quot;smooth\&quot;) | 
 **start_date** | **str**| Starting date of desired timeseries (YYYY-MM-DD) | 
 **end_date** | **str**| Ending date of desired timeseries (YYYY-MM-DD) | 
 **consilience_id** | **str**| Internal custom company identifier | [optional] 
 **ticker** | **str**| Ticker of the company/security | [optional] 
 **cik** | **str**| Central indexing key (CIK) used by SEC&#39;s EDGAR database | [optional] 
 **lei** | **str**| Legal entity identifier (LEI) | [optional] 
 **isin** | **str**| International Securities Identification Number (ISIN) | [optional] 
 **cusip** | **str**| Committee on Uniform Securities Identification Procedures (CUSIP) | [optional] 
 **sedol** | **str**| Stock exchange daily official list (SEDOL) | [optional] 

### Return type

[**ModelsSpindexModel**](ModelsSpindexModel.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)



# **get_bulk_model**
> FileDownloadModel1 get_bulk_model(raw_smooth_flag, model_name)

BulkFileModels

Delivers historical model data files (2013-2023) as a gzipped csv file. Delivered as a temporary download link.

### Example

* Bearer Authentication (bearer):

```python
import os
from dotenv import load_dotenv
import alphaiq_sdk

# Load the environment variables from the .env file
load_dotenv()
APIKEY = os.getenv('APIKEY')
client = alphaiq_sdk.client(APIKEY)

rawSmoothFlag = 'raw'
modelName = 'spindex'

response = client.get_bulk_model(rawSmoothFlag,modelName)


print(response)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **raw_smooth_flag** | **str**| Flag for raw or smooth version of the model (\&quot;raw\&quot;, \&quot;smooth\&quot;) | 
 **model_name** | **str**| Name of the model (\&quot;spindex\&quot;) | 

### Return type

[**FileDownloadModel1**](FileDownloadModel1.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# **get_company_identifiers**
> MappingCompanyIdentifierMappingModel get_company_identifiers(ticker=ticker, cik=cik, consilience_id=consilience_id, lei=lei, isin=isin, cusip=cusip, sedol=sedol)

MappingCompanyIdentifiers

Delivers mapping data for company based on variety of potential identifiers (ConsilienceID, Ticker, CIK, LEI, ISIN, CUSIP, SEDOL)

### Example

* Bearer Authentication (bearer):

```python
import os
from dotenv import load_dotenv
import alphaiq_sdk

# Load the environment variables from the .env file
load_dotenv()
APIKEY = os.getenv('APIKEY')
client = alphaiq_sdk.client(APIKEY)

ticker = 'TSLA'

response = client.get_company_identifiers(ticker)
print(response)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ticker** | **str**| Ticker of the company/security | [optional] 
 **cik** | **str**| Central indexing key (CIK) used by SEC&#39;s EDGAR database | [optional] 
 **consilience_id** | **str**| Internal custom company identifier | [optional] 
 **lei** | **str**| Legal entity identifier (LEI) | [optional] 
 **isin** | **str**| International Securities Identification Number (ISIN) | [optional] 
 **cusip** | **str**| Committee on Uniform Securities Identification Procedures (CUSIP) | [optional] 
 **sedol** | **str**| Stock exchange daily official list (SEDOL) | [optional] 

### Return type

[**MappingCompanyIdentifierMappingModel**](MappingCompanyIdentifierMappingModel.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# **get_bulk_mapping**
> FileDownloadModel1 get_bulk_mapping()

BulkFileMapping

Delivers gzipped csv file containing company mapping information (ConsilienceId, CIK, LEI, Ticker, Company Name)

### Example

* Bearer Authentication (bearer):

```python
import os
from dotenv import load_dotenv
import alphaiq_sdk

# Load the environment variables from the .env file
load_dotenv()
APIKEY = os.getenv('APIKEY')
client = alphaiq_sdk.client(APIKEY)

response = client.get_bulk_mapping()
print(response)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**FileDownloadModel1**](FileDownloadModel1.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# **get_spindex_factors**
> MappingSpindexFactorsModel get_spindex_factors(spindex_id=spindex_id)

MappingSpindexFactors

Delivers descriptions of SPINDEX factors

### Example

* Bearer Authentication (bearer):

```python
import os
from dotenv import load_dotenv
import alphaiq_sdk

# Load the environment variables from the .env file
load_dotenv()
APIKEY = os.getenv('APIKEY')
client = alphaiq_sdk.client(APIKEY)

response = client.get_spindex_factors()
print(response)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **spindex_id** | **str**| Spindex factor name | [optional] 

### Return type

[**MappingSpindexFactorsModel**](MappingSpindexFactorsModel.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# **get_compass_questions**
> MappingCompassQuestionsModel get_compass_questions(question_id=question_id)

MappingCompassQuestions

Delivers descriptions of COMPASS Explorer questions

### Example

* Bearer Authentication (bearer):

```python
import os
from dotenv import load_dotenv
import alphaiq_sdk

# Load the environment variables from the .env file
load_dotenv()
APIKEY = os.getenv('APIKEY')
client = alphaiq_sdk.client(APIKEY)

response = client.get_compass_questions()

print(response)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **question_id** | **int**| Question number 1 - 18 | [optional] 

### Return type

[**MappingCompassQuestionsModel**](MappingCompassQuestionsModel.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_spinsights_explorer_spindex_summary**
> GenerativeCompanySpinsightsExplorerModel get_spinsights_explorer_spindex_summary(ticker)

GetSpinsightsExplorerSpindexSummary

Get the most recent generative SPINSIGHTS Explorer data for a company. This content explains the underlying drivers of the 9 SPINDEX Factors.

### Example

* Bearer Authentication (bearer):

```python
import os
from dotenv import load_dotenv
import alphaiq_sdk

# Load the environment variables from the .env file
load_dotenv()
APIKEY = os.getenv('APIKEY')
client = alphaiq_sdk.client(APIKEY)

ticker = 'TSLA'

response = client.get_spinsights_explorer_spindex_summary(ticker)

print(response)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ticker** | **str**| Ticker identifier corresponding to a security or company | 

### Return type

[**GenerativeCompanySpinsightsExplorerModel**](GenerativeCompanySpinsightsExplorerModel.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_spinsights_report_content**
> GenerativeCompanySpinsightsReportContentModel get_spinsights_report_content(ticker)

GetSpinsightsReportContent

Get the most recent SPINSIGHTS report content for a company. This report content specifically highlights the company's language which is more prominent than peers.  Note: the \"SPINDEX Summary\" is present in this report endpoint but not the GetCompassReportContent. This should avoid duplicate information.

### Example

* Bearer Authentication (bearer):

```python
import os
from dotenv import load_dotenv
import alphaiq_sdk

# Load the environment variables from the .env file
load_dotenv()
APIKEY = os.getenv('APIKEY')
client = alphaiq_sdk.client(APIKEY)

ticker = 'TSLA'

response = client.get_spinsights_report_content(ticker)

print(response)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ticker** | **str**|  | 

### Return type

[**GenerativeCompanySpinsightsReportContentModel**](GenerativeCompanySpinsightsReportContentModel.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# **get_spinsights_report_pdf**
> FileDownloadModel get_spinsights_report_pdf(ticker)

SpinsightsReportPDF

Get pre-signed URL for a company's generative SPINSIGHTS PDF report

### Example

* Bearer Authentication (bearer):

```python
import os
from dotenv import load_dotenv
import alphaiq_sdk

# Load the environment variables from the .env file
load_dotenv()
APIKEY = os.getenv('APIKEY')
client = alphaiq_sdk.client(APIKEY)
ticker = 'TSLA'

response = client.get_spinsights_report_pdf(ticker)
print(response)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ticker** | **str**| Ticker identifier corresponding to a security or company | 

### Return type

[**FileDownloadModel**](FileDownloadModel.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_compass_explorer_question_answer**
> GenerativeCompanyQuestionAnswerModel get_compass_explorer_question_answer(ticker)

GetCompassExplorerQuestionAnswer

Get the COMPASS Explorer Question & Answer results.

### Example

* Bearer Authentication (bearer):

```python
import os
from dotenv import load_dotenv
import alphaiq_sdk

# Load the environment variables from the .env file
load_dotenv()
APIKEY = os.getenv('APIKEY')
client = alphaiq_sdk.client(APIKEY)

ticker = 'TSLA'

response = client.get_compass_explorer_question_answer(ticker)

print(response)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ticker** | **str**|  | 

### Return type

[**GenerativeCompanyQuestionAnswerModel**](GenerativeCompanyQuestionAnswerModel.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_compass_report_content**
> GenerativeCompanyCompassReportContentModel get_compass_report_content(ticker)

GetCompassReportContent



### Example

* Bearer Authentication (bearer):

```python
import os
from dotenv import load_dotenv
import alphaiq_sdk

# Load the environment variables from the .env file
load_dotenv()
APIKEY = os.getenv('APIKEY')
client = alphaiq_sdk.client(APIKEY)

ticker = 'TSLA'

response = client.get_compass_report_content(ticker)

print(response)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ticker** | **str**|  | 

### Return type

[**GenerativeCompanyCompassReportContentModel**](GenerativeCompanyCompassReportContentModel.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_compass_report_pdf**
> FileDownloadModel get_compass_report_pdf(ticker)

CompassReportPDF

Get pre-signed URL for a company's generative COMPASS PDF report

### Example

* Bearer Authentication (bearer):

```python
import os
from dotenv import load_dotenv
import alphaiq_sdk

# Load the environment variables from the .env file
load_dotenv()
APIKEY = os.getenv('APIKEY')
client = alphaiq_sdk.client(APIKEY)

ticker = 'TSLA'

response = client.get_compass_report_pdf(ticker)

print(response)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ticker** | **str**| Ticker identifier corresponding to a security or company | 

### Return type

[**FileDownloadModel**](FileDownloadModel.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

