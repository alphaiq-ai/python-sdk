# alphaiq_sdk.InvestmentResearchersApi

All URIs are relative to *https://data.app.alphaiq.ai/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_signal_explanations**](InvestmentResearchersApi.md#get_signal_explanations) | **GET** /generative/company/signal_explanation/{ticker} | GetSignalExplanations
[**get_trending_content**](InvestmentResearchersApi.md#get_trending_content) | **GET** /generative/company/compass/reportContent/{ticker} | GetTrendingGenerative
[**get_question_answer**](InvestmentResearchersApi.md#get_question_answer) | **GET** /generative/company/compass/questionContent/{ticker} | GetQuestionAnswer
[**get_compass_report_pdf**](InvestmentResearchersApi.md#get_compass_report_pdf) | **GET** /pdf/compass/{ticker} | CompassReportPDF
[**get_quant_linguistics_signals**](InvestmentResearchersApi.md#get_quant_linguistics_signals) | **GET** /signals/quantLinguistics | SignalsQuantLinguistics
[**get_bulk_signals_all**](InvestmentResearchersApi.md#get_bulk_signals_all) | **GET** /bulk/signals/all | BulkFileSignalsAll
[**get_bulk_signals_top_level**](InvestmentResearchersApi.md#get_bulk_signals_top_level) | **GET** /bulk/signals/topLevel | BulkFileSignalsTopLevel
[**get_models_corporate_transparency**](InvestmentResearchersApi.md#get_models_corporate_transparency) | **GET** /models/corporateTransparency | ModelsCorporateTransparency
[**get_bulk_model**](InvestmentResearchersApi.md#get_bulk_model) | **GET** /bulk/models | BulkFileModels
[**get_company_identifiers_map**](InvestmentResearchersApi.md#get_company_identifiers_map) | **GET** /mapping/companyIdentifierMapping | MappingCompanyIdentifiers
[**get_bulk_mapping**](InvestmentResearchersApi.md#get_bulk_mapping) | **GET** /bulk/mapping | BulkFileMapping

# **get_signal_explanations**
> GenerativeSignalExplanationsModel get_signal_explanations(ticker)

GetSignalExplanations

Get the generative explanations for each signal.

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

response = client.get_signal_explanations(ticker)

print(response)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ticker** | **str**|  | 

### Return type

[**GenerativeSignalExplanationsModel**](GenerativeSignalExplanationsModel.md)

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


# **get_trending_content**
> GenerativeTrendingContentModel get_trending_content(ticker)

GetTrendingGenerative

Get the COMPASS Report generative content, containing 'most prevalent', 'increasing trend', and 'decreasing trend' content.

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

response = client.get_trending_content(ticker)

print(response)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ticker** | **str**|  | 

### Return type

[**GenerativeCompanyTrendingContentModel**](GenerativeCompanyTrendingContentModel.md)

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

# **get_question_answer**
> GenerativeCompanyQuestionAnswerModel get_question_answer(ticker)

GetQuestionAnswer

Get the Question & Answer generative content.

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

response = client.get_question_answer(ticker)

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

# **get_quant_linguistics_signals**
> SignalsQuantLinguisticsModelRoot get_quant_linguistics_signals(start_date, end_date, consilience_id=consilience_id, ticker=ticker, cik=cik, lei=lei, isin=isin, cusip=cusip)

SignalsQuantLinguistics

Provides a signal for each of the Quantitative Linguistics signal groupings. These signals represent the aggregation of all the underlying signals. Query using one and only one nof the company identifiers (ConsilienceId, Ticker, CIK, LEI, ISIN, CUSIP). Note: currently a sample dataset for 2023 only.

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



# **get_bulk_signals_all**
> FileDownloadModel1 get_bulk_signals_all()

BulkFileSignalsAll

Delivers historical signal data files (2013-2023) as a zipped folder of gzipped csv files. Delivered as a temporary download link. Files reflect all Top Level and Sub-Level signals for each of the Text Signal categories.

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

response = client.get_bulk_signals_all()

print(response)

```



### Parameters

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


# **get_bulk_signals_top_level**
> FileDownloadModel1 get_bulk_signals_top_level()

BulkFileSignalsTopLevel

Delivers top level signal files as a zip folder of gzipped csv files. Delivered as a temporary download link. Files reflect five variations (RAW, CHANGE, ROC, WH, MR) of each Top Level signal.

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

response = client.get_bulk_signals_top_level()
print(response)

```



### Parameters


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


# **get_models_corporate_transparency**
> ModelsCorporateTransparencyModel get_models_corporate_transparency(modelVariation, startDate, endDate, consilience_id=consilience_id, ticker=ticker, cik=cik, lei=lei, isin=isin, cusip=cusip)

ModelsCorporateTransparency

Delivers Corporate Transparency Scores for a variety of company identifiers (ConsilienceId, Ticker, CIK, LEI, ISIN, CUSIP). Provides variations of the model (RAW, CHANGE, WH, ROC, MR).

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
modelVariation = 'CHANGE'
startDate='2023-03-01'
endDate='2023-05-01'

response = client.get_models_corporate_transparency(modelVariation,startDate,endDate,ticker=ticker)
print(response)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **modelVariation** | **str**| Timeseries variation of the model (\&quot;RAW\&quot;, \&quot;CHANGE\&quot;, \&quot;ROC\&quot;, \&quot;WH\&quot;, \&quot;MR\&quot;) | 
 **startDate** | **str**| Starting date of desired timeseries (YYYY-MM-DD) | 
 **endDate** | **str**| Ending date of desired timeseries (YYYY-MM-DD) | 
 **consilience_id** | **str**| Internal custom company identifier | [optional] 
 **ticker** | **str**| Ticker of the company/security | [optional] 
 **cik** | **str**| Central indexing key (CIK) used by SEC&#39;s EDGAR database | [optional] 
 **lei** | **str**| Legal entity identifier (LEI) | [optional] 
 **isin** | **str**| International Securities Identification Number (ISIN) | [optional] 
 **cusip** | **str**| Committee on Uniform Securities Identification Procedures (CUSIP) | [optional] 
 
### Return type

[**ModelsCorporateTransparencyModel**](ModelsCorporateTransparencyModel.md)

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
> FileDownloadModel1 get_bulk_model(model_name)

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

modelName = 'transparency_score'

response = client.get_bulk_model(modelName)


print(response)

```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
**model_name** | **str**| Name of the model (\&quot;transparency_score\&quot;) | 

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


# **get_company_identifiers_map**
> MappingCompanyIdentifierMappingModel get_company_identifiers_map(ticker=ticker, cik=cik, consilience_id=consilience_id, lei=lei, isin=isin, cusip=cusip)

MappingCompanyIdentifiers

Delivers mapping data for company based on variety of potential identifiers (ConsilienceID, Ticker, CIK, LEI, ISIN, CUSIP)

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

response = client.get_company_identifiers_map(ticker)
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



