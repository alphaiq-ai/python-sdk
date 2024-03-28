# alphaiq_sdk.InvestmentResearchersApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulk_mapping_get**](InvestmentResearchersApi.md#bulk_mapping_get) | **GET** /bulk/mapping | BulkFileMapping
[**bulk_models_get**](InvestmentResearchersApi.md#bulk_models_get) | **GET** /bulk/models | BulkFileModels
[**bulk_signals_get**](InvestmentResearchersApi.md#bulk_signals_get) | **GET** /bulk/signals | BulkFileSignals
[**bulk_signals_yearly_get**](InvestmentResearchersApi.md#bulk_signals_yearly_get) | **GET** /bulk/signals/yearly | BulkFileSignalsYearly
[**company_compass_report_pdf_ticker_get**](InvestmentResearchersApi.md#company_compass_report_pdf_ticker_get) | **GET** /company/compass/reportPDF/{ticker} | CompassReportPDF
[**company_spinsights_report_pdf_ticker_get**](InvestmentResearchersApi.md#company_spinsights_report_pdf_ticker_get) | **GET** /company/spinsights/reportPDF/{ticker} | SpinsightsReportPDF
[**generative_company_compass_question_content_ticker_get**](InvestmentResearchersApi.md#generative_company_compass_question_content_ticker_get) | **GET** /generative/company/compass/questionContent/{ticker} | GetCompassExplorerQuestionAnswer
[**generative_company_compass_report_content_ticker_get**](InvestmentResearchersApi.md#generative_company_compass_report_content_ticker_get) | **GET** /generative/company/compass/reportContent/{ticker} | GetCompassReportContent
[**generative_company_spinsights_explorer_content_ticker_get**](InvestmentResearchersApi.md#generative_company_spinsights_explorer_content_ticker_get) | **GET** /generative/company/spinsights/explorerContent/{ticker} | GetSpinsightsExplorer
[**generative_company_spinsights_report_content_ticker_get**](InvestmentResearchersApi.md#generative_company_spinsights_report_content_ticker_get) | **GET** /generative/company/spinsights/reportContent/{ticker} | GetSpinsightsReportContent
[**mapping_company_identifier_mapping_get**](InvestmentResearchersApi.md#mapping_company_identifier_mapping_get) | **GET** /mapping/companyIdentifierMapping | MappingCompanyIdentifiers
[**mapping_compass_questions_get**](InvestmentResearchersApi.md#mapping_compass_questions_get) | **GET** /mapping/compassQuestions | MappingCompassQuestions
[**mapping_spindex_factors_get**](InvestmentResearchersApi.md#mapping_spindex_factors_get) | **GET** /mapping/spindexFactors | MappingSpindexFactors
[**models_spindex_get**](InvestmentResearchersApi.md#models_spindex_get) | **GET** /models/spindex | ModelsSpindex
[**signals_quant_linguistics_get**](InvestmentResearchersApi.md#signals_quant_linguistics_get) | **GET** /signals/quantLinguistics | SignalsQuantLinguistics


# **bulk_mapping_get**
> BulkMappingGet200Response bulk_mapping_get()

BulkFileMapping

Delivers gzipped csv file containing company mapping information (ConsilienceId, CIK, LEI, Ticker, Company Name)

### Example

* Bearer Authentication (bearer):

```python
import alphaiq_sdk
from alphaiq_sdk.models.bulk_mapping_get200_response import BulkMappingGet200Response
from alphaiq_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = alphaiq_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer
configuration = alphaiq_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with alphaiq_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = alphaiq_sdk.InvestmentResearchersApi(api_client)

    try:
        # BulkFileMapping
        api_response = api_instance.bulk_mapping_get()
        print("The response of InvestmentResearchersApi->bulk_mapping_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvestmentResearchersApi->bulk_mapping_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**BulkMappingGet200Response**](BulkMappingGet200Response.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_models_get**
> FileDownloadModel1 bulk_models_get(raw_smooth_flag, model_name)

BulkFileModels

Delivers historical model data files (2013-2023) as a gzipped csv file. Delivered as a temporary download link.

### Example

* Bearer Authentication (bearer):

```python
import alphaiq_sdk
from alphaiq_sdk.models.file_download_model1 import FileDownloadModel1
from alphaiq_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = alphaiq_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer
configuration = alphaiq_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with alphaiq_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = alphaiq_sdk.InvestmentResearchersApi(api_client)
    raw_smooth_flag = 'raw' # str | Flag for raw or smooth version of the model (\"raw\", \"smooth\")
    model_name = 'spindex' # str | Name of the model (\"spindex\")

    try:
        # BulkFileModels
        api_response = api_instance.bulk_models_get(raw_smooth_flag, model_name)
        print("The response of InvestmentResearchersApi->bulk_models_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvestmentResearchersApi->bulk_models_get: %s\n" % e)
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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_signals_get**
> FileDownloadModel1 bulk_signals_get(strategy_type)

BulkFileSignals

Delivers historical signal data files (2013-2023) as a zipped folder of gzipped csv files. Delivered as a temporary download link. Files determined based on signal strategy type (long, short, longshort).

### Example

* Bearer Authentication (bearer):

```python
import alphaiq_sdk
from alphaiq_sdk.models.file_download_model1 import FileDownloadModel1
from alphaiq_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = alphaiq_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer
configuration = alphaiq_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with alphaiq_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = alphaiq_sdk.InvestmentResearchersApi(api_client)
    strategy_type = 'long' # str | Type of strategy signals are used for (\"long\", \"short\", \"longshort\")

    try:
        # BulkFileSignals
        api_response = api_instance.bulk_signals_get(strategy_type)
        print("The response of InvestmentResearchersApi->bulk_signals_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvestmentResearchersApi->bulk_signals_get: %s\n" % e)
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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_signals_yearly_get**
> FileDownloadModel1 bulk_signals_yearly_get(strategy_type=strategy_type, alpha_horizon=alpha_horizon, year=year)

BulkFileSignalsYearly

Delivers yearly signal files as a gzipped csv files. Delivered as a temporary download link. Files determined based on year, alpha horizon (4 week increments between 4 and 52 weeks) and signal strategy type (long, short, longshort).

### Example

* Bearer Authentication (bearer):

```python
import alphaiq_sdk
from alphaiq_sdk.models.file_download_model1 import FileDownloadModel1
from alphaiq_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = alphaiq_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer
configuration = alphaiq_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with alphaiq_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = alphaiq_sdk.InvestmentResearchersApi(api_client)
    strategy_type = 'long' # str | Type of strategy signals are used for (\"long\", \"short\", \"longshort\") (optional)
    alpha_horizon = '4-week' # str | 4-week investment horizon intervals from 4-week to 52-week (e.g. \"4-week\", \"8-week\", \"12-week\") (optional)
    year = '2014' # str | Year of historical signals between 2014-2023 (optional)

    try:
        # BulkFileSignalsYearly
        api_response = api_instance.bulk_signals_yearly_get(strategy_type=strategy_type, alpha_horizon=alpha_horizon, year=year)
        print("The response of InvestmentResearchersApi->bulk_signals_yearly_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvestmentResearchersApi->bulk_signals_yearly_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **strategy_type** | **str**| Type of strategy signals are used for (\&quot;long\&quot;, \&quot;short\&quot;, \&quot;longshort\&quot;) | [optional] 
 **alpha_horizon** | **str**| 4-week investment horizon intervals from 4-week to 52-week (e.g. \&quot;4-week\&quot;, \&quot;8-week\&quot;, \&quot;12-week\&quot;) | [optional] 
 **year** | **str**| Year of historical signals between 2014-2023 | [optional] 

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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **company_compass_report_pdf_ticker_get**
> FileDownloadModel company_compass_report_pdf_ticker_get(ticker)

CompassReportPDF

Get pre-signed URL for a company's generative COMPASS PDF report

### Example

* Bearer Authentication (bearer):

```python
import alphaiq_sdk
from alphaiq_sdk.models.file_download_model import FileDownloadModel
from alphaiq_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = alphaiq_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer
configuration = alphaiq_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with alphaiq_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = alphaiq_sdk.InvestmentResearchersApi(api_client)
    ticker = 'TSLA' # str | Ticker identifier corresponding to a security or company

    try:
        # CompassReportPDF
        api_response = api_instance.company_compass_report_pdf_ticker_get(ticker)
        print("The response of InvestmentResearchersApi->company_compass_report_pdf_ticker_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvestmentResearchersApi->company_compass_report_pdf_ticker_get: %s\n" % e)
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
**404** | InsufficientPermissions |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **company_spinsights_report_pdf_ticker_get**
> FileDownloadModel company_spinsights_report_pdf_ticker_get(ticker)

SpinsightsReportPDF

Get pre-signed URL for a company's generative SPINSIGHTS PDF report

### Example

* Bearer Authentication (bearer):

```python
import alphaiq_sdk
from alphaiq_sdk.models.file_download_model import FileDownloadModel
from alphaiq_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = alphaiq_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer
configuration = alphaiq_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with alphaiq_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = alphaiq_sdk.InvestmentResearchersApi(api_client)
    ticker = 'TSLA' # str | Ticker identifier corresponding to a security or company

    try:
        # SpinsightsReportPDF
        api_response = api_instance.company_spinsights_report_pdf_ticker_get(ticker)
        print("The response of InvestmentResearchersApi->company_spinsights_report_pdf_ticker_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvestmentResearchersApi->company_spinsights_report_pdf_ticker_get: %s\n" % e)
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
**404** | InsufficientPermissions |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generative_company_compass_question_content_ticker_get**
> GenerativeCompanyQuestionAnswerModel generative_company_compass_question_content_ticker_get(ticker)

GetCompassExplorerQuestionAnswer

Get the COMPASS Explorer Question & Answer results.

### Example

* Bearer Authentication (bearer):

```python
import alphaiq_sdk
from alphaiq_sdk.models.generative_company_question_answer_model import GenerativeCompanyQuestionAnswerModel
from alphaiq_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = alphaiq_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer
configuration = alphaiq_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with alphaiq_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = alphaiq_sdk.InvestmentResearchersApi(api_client)
    ticker = 'WMT' # str | 

    try:
        # GetCompassExplorerQuestionAnswer
        api_response = api_instance.generative_company_compass_question_content_ticker_get(ticker)
        print("The response of InvestmentResearchersApi->generative_company_compass_question_content_ticker_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvestmentResearchersApi->generative_company_compass_question_content_ticker_get: %s\n" % e)
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

# **generative_company_compass_report_content_ticker_get**
> GenerativeCompanyCompassReportContentModel generative_company_compass_report_content_ticker_get(ticker)

GetCompassReportContent



### Example

* Bearer Authentication (bearer):

```python
import alphaiq_sdk
from alphaiq_sdk.models.generative_company_compass_report_content_model import GenerativeCompanyCompassReportContentModel
from alphaiq_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = alphaiq_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer
configuration = alphaiq_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with alphaiq_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = alphaiq_sdk.InvestmentResearchersApi(api_client)
    ticker = 'WMT' # str | 

    try:
        # GetCompassReportContent
        api_response = api_instance.generative_company_compass_report_content_ticker_get(ticker)
        print("The response of InvestmentResearchersApi->generative_company_compass_report_content_ticker_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvestmentResearchersApi->generative_company_compass_report_content_ticker_get: %s\n" % e)
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

# **generative_company_spinsights_explorer_content_ticker_get**
> GenerativeCompanySpinsightsExplorerModel generative_company_spinsights_explorer_content_ticker_get(ticker)

GetSpinsightsExplorer

Get the most recent generative SPINSIGHTS Explorer data for a company. This content explains the underlying drivers of the 9 SPINDEX Factors.

### Example

* Bearer Authentication (bearer):

```python
import alphaiq_sdk
from alphaiq_sdk.models.generative_company_spinsights_explorer_model import GenerativeCompanySpinsightsExplorerModel
from alphaiq_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = alphaiq_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer
configuration = alphaiq_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with alphaiq_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = alphaiq_sdk.InvestmentResearchersApi(api_client)
    ticker = 'TSLA' # str | Ticker identifier corresponding to a security or company

    try:
        # GetSpinsightsExplorer
        api_response = api_instance.generative_company_spinsights_explorer_content_ticker_get(ticker)
        print("The response of InvestmentResearchersApi->generative_company_spinsights_explorer_content_ticker_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvestmentResearchersApi->generative_company_spinsights_explorer_content_ticker_get: %s\n" % e)
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

# **generative_company_spinsights_report_content_ticker_get**
> GenerativeCompanySpinsightsReportContentModel generative_company_spinsights_report_content_ticker_get(ticker)

GetSpinsightsReportContent

Get the most recent SPINSIGHTS report content for a company. This report content specifically highlights the company's language which is more prominent than peers.  Note: the \"SPINDEX Summary\" is present in this report endpoint but not the GetCompassReportContent. This should avoid duplicate information.

### Example

* Bearer Authentication (bearer):

```python
import alphaiq_sdk
from alphaiq_sdk.models.generative_company_spinsights_report_content_model import GenerativeCompanySpinsightsReportContentModel
from alphaiq_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = alphaiq_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer
configuration = alphaiq_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with alphaiq_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = alphaiq_sdk.InvestmentResearchersApi(api_client)
    ticker = 'WMT' # str | 

    try:
        # GetSpinsightsReportContent
        api_response = api_instance.generative_company_spinsights_report_content_ticker_get(ticker)
        print("The response of InvestmentResearchersApi->generative_company_spinsights_report_content_ticker_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvestmentResearchersApi->generative_company_spinsights_report_content_ticker_get: %s\n" % e)
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

# **mapping_company_identifier_mapping_get**
> CompanyMappingCompanyToSecurityModel mapping_company_identifier_mapping_get(ticker=ticker, cik=cik, consilience_id=consilience_id, lei=lei, isin=isin, cusip=cusip, sedol=sedol)

MappingCompanyIdentifiers

Delivers mapping data for company based on variety of potential identifiers (ConsilienceID, Ticker, CIK, LEI, ISIN, CUSIP, SEDOL)

### Example

* Bearer Authentication (bearer):

```python
import alphaiq_sdk
from alphaiq_sdk.models.company_mapping_company_to_security_model import CompanyMappingCompanyToSecurityModel
from alphaiq_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = alphaiq_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer
configuration = alphaiq_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with alphaiq_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = alphaiq_sdk.InvestmentResearchersApi(api_client)
    ticker = 'TSLA' # str | Ticker of the company/security (optional)
    cik = '0001318605' # str | Central indexing key (CIK) used by SEC's EDGAR database (optional)
    consilience_id = '96e723789d1ca1b6652b326ebf9c34ff' # str | Internal custom company identifier (optional)
    lei = '54930043XZGB27CTOV49' # str | Legal entity identifier (LEI) (optional)
    isin = 'US88160R1014' # str | International Securities Identification Number (ISIN) (optional)
    cusip = '88160R101' # str | Committee on Uniform Securities Identification Procedures (CUSIP) (optional)
    sedol = 'B616C79' # str | Stock exchange daily official list (SEDOL) (optional)

    try:
        # MappingCompanyIdentifiers
        api_response = api_instance.mapping_company_identifier_mapping_get(ticker=ticker, cik=cik, consilience_id=consilience_id, lei=lei, isin=isin, cusip=cusip, sedol=sedol)
        print("The response of InvestmentResearchersApi->mapping_company_identifier_mapping_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvestmentResearchersApi->mapping_company_identifier_mapping_get: %s\n" % e)
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

[**CompanyMappingCompanyToSecurityModel**](CompanyMappingCompanyToSecurityModel.md)

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

# **mapping_compass_questions_get**
> FactorLibraryCompassQuestionsModel mapping_compass_questions_get(question_id=question_id)

MappingCompassQuestions

Delivers descriptions of COMPASS Explorer questions

### Example

* Bearer Authentication (bearer):

```python
import alphaiq_sdk
from alphaiq_sdk.models.factor_library_compass_questions_model import FactorLibraryCompassQuestionsModel
from alphaiq_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = alphaiq_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer
configuration = alphaiq_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with alphaiq_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = alphaiq_sdk.InvestmentResearchersApi(api_client)
    question_id = 1 # int | Question number 1 - 18 (optional)

    try:
        # MappingCompassQuestions
        api_response = api_instance.mapping_compass_questions_get(question_id=question_id)
        print("The response of InvestmentResearchersApi->mapping_compass_questions_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvestmentResearchersApi->mapping_compass_questions_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **question_id** | **int**| Question number 1 - 18 | [optional] 

### Return type

[**FactorLibraryCompassQuestionsModel**](FactorLibraryCompassQuestionsModel.md)

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

# **mapping_spindex_factors_get**
> FactorLibrarySpindexFactorsModel mapping_spindex_factors_get(spindex_id=spindex_id)

MappingSpindexFactors

Delivers descriptions of SPINDEX factors

### Example

* Bearer Authentication (bearer):

```python
import alphaiq_sdk
from alphaiq_sdk.models.factor_library_spindex_factors_model import FactorLibrarySpindexFactorsModel
from alphaiq_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = alphaiq_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer
configuration = alphaiq_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with alphaiq_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = alphaiq_sdk.InvestmentResearchersApi(api_client)
    spindex_id = 'uncertain' # str | Spindex factor name (optional)

    try:
        # MappingSpindexFactors
        api_response = api_instance.mapping_spindex_factors_get(spindex_id=spindex_id)
        print("The response of InvestmentResearchersApi->mapping_spindex_factors_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvestmentResearchersApi->mapping_spindex_factors_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **spindex_id** | **str**| Spindex factor name | [optional] 

### Return type

[**FactorLibrarySpindexFactorsModel**](FactorLibrarySpindexFactorsModel.md)

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

# **models_spindex_get**
> ModelsSpindexModel models_spindex_get(raw_smooth_flag, start_date, end_date, consilience_id=consilience_id, ticker=ticker, cik=cik, lei=lei, isin=isin, cusip=cusip, sedol=sedol)

ModelsSpindex

Delivers SPINDEX scores for a variety of company identifiers (ConsilienceId, Ticker, CIK, LEI, ISIN, CUSIP, SEDOL). Provides the raw or smooth version of the model.

### Example

* Bearer Authentication (bearer):

```python
import alphaiq_sdk
from alphaiq_sdk.models.models_spindex_model import ModelsSpindexModel
from alphaiq_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = alphaiq_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer
configuration = alphaiq_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with alphaiq_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = alphaiq_sdk.InvestmentResearchersApi(api_client)
    raw_smooth_flag = 'smooth' # str | Flag for raw or smooth version of the model (\"raw\", \"smooth\")
    start_date = '2024-01-01' # str | Starting date of desired timeseries (YYYY-MM-DD)
    end_date = '2024-02-01' # str | Ending date of desired timeseries (YYYY-MM-DD)
    consilience_id = '96e723789d1ca1b6652b326ebf9c34ff' # str | Internal custom company identifier (optional)
    ticker = 'TSLA' # str | Ticker of the company/security (optional)
    cik = '0001318605' # str | Central indexing key (CIK) used by SEC's EDGAR database (optional)
    lei = '54930043XZGB27CTOV49' # str | Legal entity identifier (LEI) (optional)
    isin = 'US88160R1014' # str | International Securities Identification Number (ISIN) (optional)
    cusip = '88160R101' # str | Committee on Uniform Securities Identification Procedures (CUSIP) (optional)
    sedol = 'B616C79' # str | Stock exchange daily official list (SEDOL) (optional)

    try:
        # ModelsSpindex
        api_response = api_instance.models_spindex_get(raw_smooth_flag, start_date, end_date, consilience_id=consilience_id, ticker=ticker, cik=cik, lei=lei, isin=isin, cusip=cusip, sedol=sedol)
        print("The response of InvestmentResearchersApi->models_spindex_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvestmentResearchersApi->models_spindex_get: %s\n" % e)
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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **signals_quant_linguistics_get**
> SignalsQuantLinguisticsModel signals_quant_linguistics_get(start_date, end_date, consilience_id=consilience_id, ticker=ticker, cik=cik, lei=lei, isin=isin, cusip=cusip, sedol=sedol)

SignalsQuantLinguistics

Provides a signal for each of the Quantitative Linguistics signal groupings. These signals represent the aggregation of all the underlying signals. Query using one and only one nof the company identifiers (ConsilienceId, Ticker, CIK, LEI, ISIN, CUSIP, SEDOL). Note: currently a sample dataset for 2023 only.

### Example

* Bearer Authentication (bearer):

```python
import alphaiq_sdk
from alphaiq_sdk.models.signals_quant_linguistics_model import SignalsQuantLinguisticsModel
from alphaiq_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = alphaiq_sdk.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearer
configuration = alphaiq_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with alphaiq_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = alphaiq_sdk.InvestmentResearchersApi(api_client)
    start_date = '2023-03-01' # str | Starting date of desired timeseries (YYYY-MM-DD)
    end_date = '2023-05-01' # str | Ending date of desired timeseries (YYYY-MM-DD)
    consilience_id = '08f4462943bb8ec4173dec55f0e368f9' # str | Internal custom company identifier (optional)
    ticker = 'UFPT' # str | Ticker of the company/security (optional)
    cik = '0000914156' # str | Central indexing key (CIK) used by SEC's EDGAR database (optional)
    lei = '549300RJ8LY41HS70C91' # str | Legal entity identifier (LEI) (optional)
    isin = ['[\"US9026731029\"]'] # List[str] | International Securities Identification Number (ISIN) (optional)
    cusip = '902673102' # str | Committee on Uniform Securities Identification Procedures (CUSIP) (optional)
    sedol = '2908652' # str | Stock exchange daily official list (SEDOL) (optional)

    try:
        # SignalsQuantLinguistics
        api_response = api_instance.signals_quant_linguistics_get(start_date, end_date, consilience_id=consilience_id, ticker=ticker, cik=cik, lei=lei, isin=isin, cusip=cusip, sedol=sedol)
        print("The response of InvestmentResearchersApi->signals_quant_linguistics_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvestmentResearchersApi->signals_quant_linguistics_get: %s\n" % e)
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

[**SignalsQuantLinguisticsModel**](SignalsQuantLinguisticsModel.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

