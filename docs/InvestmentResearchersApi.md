# openapi_client.InvestmentResearchersApi

All URIs are relative to *https://data.app.alphaiq.ai/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**auth_gettoken_post**](InvestmentResearchersApi.md#auth_gettoken_post) | **POST** /auth/gettoken | GetToken
[**auth_refreshtoken_post**](InvestmentResearchersApi.md#auth_refreshtoken_post) | **POST** /auth/refreshtoken | RefreshToken
[**company_mapping_company_to_security_get**](InvestmentResearchersApi.md#company_mapping_company_to_security_get) | **GET** /company-mapping/company-to-security | CompanyToSecurity
[**company_spindex_get_latest_spindex_factors_get**](InvestmentResearchersApi.md#company_spindex_get_latest_spindex_factors_get) | **GET** /company-spindex/getLatestSpindexFactors | GetLatestSpindexFactors
[**company_spindex_get_latest_spindex_overall_risk_get**](InvestmentResearchersApi.md#company_spindex_get_latest_spindex_overall_risk_get) | **GET** /company-spindex/getLatestSpindexOverallRisk | GetLatestSpindexOverallRisk
[**company_spindex_get_timeseries_spindex_factors_get**](InvestmentResearchersApi.md#company_spindex_get_timeseries_spindex_factors_get) | **GET** /company-spindex/getTimeseriesSpindexFactors | GetTimeseriesSpindexFactors
[**company_spindex_get_timeseries_spindex_overall_risk_get**](InvestmentResearchersApi.md#company_spindex_get_timeseries_spindex_overall_risk_get) | **GET** /company-spindex/getTimeseriesSpindexOverallRisk | GetTimeseriesSpindexOverallRisk
[**company_spinsights_report_ticker_get**](InvestmentResearchersApi.md#company_spinsights_report_ticker_get) | **GET** /company/spinsights/report/{ticker} | SpinsightsReportPDF
[**factor_library_compass_questions_get**](InvestmentResearchersApi.md#factor_library_compass_questions_get) | **GET** /factor-library/compass-questions | GetCompassQuestions
[**factor_library_spindex_factors_get**](InvestmentResearchersApi.md#factor_library_spindex_factors_get) | **GET** /factor-library/spindex-factors | GetSpindexFactors
[**generative_company_compass_report_content_ticker_get**](InvestmentResearchersApi.md#generative_company_compass_report_content_ticker_get) | **GET** /generative/company/compass/reportContent/{ticker} | GetCompassReportContent
[**generative_company_question_answer_ticker_get**](InvestmentResearchersApi.md#generative_company_question_answer_ticker_get) | **GET** /generative/company/questionAnswer/{ticker} | GetCompassExplorerQuestionAnswer
[**generative_company_spinsights_explorer_ticker_get**](InvestmentResearchersApi.md#generative_company_spinsights_explorer_ticker_get) | **GET** /generative/company/spinsights/explorer/{ticker} | GetSpinsightsExplorer
[**generative_company_spinsights_report_content_ticker_get**](InvestmentResearchersApi.md#generative_company_spinsights_report_content_ticker_get) | **GET** /generative/company/spinsights/reportContent/{ticker} | GetSpinsightsReportContent
[**company_compass_report_ticker_get**](InvestmentResearchersApi.md#company_compass_report_ticker_get) | **GET** /company/compass/report/{ticker} | CompassReportPDF

# **auth_gettoken_post**
> InlineResponse200 auth_gettoken_post(content_type, inline_object=inline_object)

GetToken

Get token with username and base64_encoded password  

### Example

Most API routes are authenticated via a bearer token. The ```auth_gettoken_post``` API allows you to retrieve this token using your email and password. The example below demonstrates this process:

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
    host = 'https://data.app.alphaiq.ai/api/v1'
    )

with openapi_client.ApiClient(configuration) as api_client:

    # Make an instance of the API class
    api_instance = openapi_client.InvestmentResearchersApi(api_client)

    # Define the values needed to authenticate to the API
    content_type = 'application/json'
    inline_object = openapi_client.InlineObject(
        email = EMAIL,
        password = PASSWORD
    )

    # Authenticate using your credentials
    api_response = api_instance.auth_gettoken_post(
        content_type = content_type,
        inline_object=inline_object
        )

    # Extract your bearer token for authentication to other API paths
    id_token = api_response.data.id_token

    # Add the bearer token to the configuration for authenticating other routes
    setattr(configuration, 'access_token', id_token)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**|  | 
 **inline_object** | [**InlineObject**](InlineObject.md)|  | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **company_compass_report_ticker_get**
> InlineResponse200 company_compass_report_ticker_get(ticker)

CompassReportPDF

Get pre-signed URL for a company's generative COMPASS PDF report

### Example

This API allows the user to retrieve a download link for the COMPASS PDF report for a company. An example is provided below:
```python
import os

from dotenv import load_dotenv
import openapi_client
from openapi_client.rest import ApiException

# Load the environment variables from the .env file
load_dotenv()

EMAIL = os.getenv('EMAIL')
PASSWORD = os.getenv('PASSWORD')

# Define the API configuration, client object and API instance
configuration = openapi_client.Configuration(
    host = 'https://data.app.alphaiq.ai/api/v1'
    )

with openapi_client.ApiClient(configuration) as api_client:

    # Make an instance of the API class
    api_instance = openapi_client.InvestmentResearchersApi(api_client)

    # Define the values needed to authenticate to the API
    content_type = 'application/json' # str | 
    inline_object = openapi_client.InlineObject(
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

with openapi_client.ApiClient(configuration) as api_client:

    # Make an instance of the API class
    api_instance = openapi_client.InvestmentResearchersApi(api_client)
    ticker = 'TSLA' 

    try:

        # Query the API to get a link to the CompassReportPDF for a given company
        api_response = api_instance.company_compass_report_ticker_get(
            ticker=ticker
            )
        print(api_response)

    except ApiException as e:

        # Log an exception if it occurs
        print("Exception when calling the API: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ticker** | **str**| Ticker identifier corresponding to a security or company | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**404** | InsufficientPermissions |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **company_mapping_company_to_security_get**
> InlineResponse20027 company_mapping_company_to_security_get(ticker=ticker, cik=cik, body=body)

CompanyToSecurity

### Example

The company to security API allows us to get the company name, ticker and CIK identifiers for a company. We can supply either a ticker or a CIK value to retrieve mapping information. An example is shown below:
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
    host = 'https://data.app.alphaiq.ai/api/v1'
    )

with openapi_client.ApiClient(configuration) as api_client:

    # Make an instance of the API class
    api_instance = openapi_client.InvestmentResearchersApi(api_client)

    # Define the values needed to authenticate to the API
    content_type = 'application/json' # str | 
    inline_object = openapi_client.InlineObject(
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

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:

    # Make an instance of the API class
    api_instance = openapi_client.InvestmentResearchersApi(api_client)
    ticker = 'TSLA' # str |  (optional)
    cik = '0001318605' # str |  (optional)
    body = '' # str |  (optional)

    try:

        # Query the company to security API with a ticker
        api_response = api_instance.company_mapping_company_to_security_get(
            ticker=ticker,
            body=body
            )
        print(api_response)

    except ApiException as e:

        # Log an exception if it occurs
        print("Exception when calling the API: %s\n" % e)
    try:

        # Query the company to security API with a CIK instead and do not provide a body
        api_response = api_instance.company_mapping_company_to_security_get(
            cik=cik
            )
        print(api_response)

    except ApiException as e:

        # Log an exception if it occurs
        print("Exception when calling the API: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ticker** | **str**|  | [optional] 
 **cik** | **str**|  | [optional] 
 **body** | **str**|  | [optional] 

### Return type

[**InlineResponse20027**](InlineResponse20027.md)

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **company_spindex_get_latest_spindex_factors_get**
> InlineResponse20023 company_spindex_get_latest_spindex_factors_get(ticker=ticker, signal_id=signal_id)

GetLatestSpindexFactors

### Example

The company_spindex_get_latest_spindex_factors API allows us to get all of the latest spindex factors for a company using the company ticker. Alternatively, we can filter down to a single spindex factor as well. An example is shown below:
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
    host = 'https://data.app.alphaiq.ai/api/v1'
    )

with openapi_client.ApiClient(configuration) as api_client:

    # Make an instance of the API class
    api_instance = openapi_client.InvestmentResearchersApi(api_client)

    # Define the values needed to authenticate to the API
    content_type = 'application/json' # str | 
    inline_object = openapi_client.InlineObject(
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

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:

    # Make an instance of the API class
    api_instance = openapi_client.InvestmentResearchersApi(api_client)
    ticker = 'TSLA' # str |  (optional)
    signal_id = 'UNCERTAIN-VALUE' # str |  (optional)

    try:

        # Query the API to get all of the most recent spindex factors for Tesla
        api_response = api_instance.company_spindex_get_latest_spindex_factors_get(
            ticker=ticker
            )
        print(api_response)

    except ApiException as e:

        # Log an exception if it occurs
        print("Exception when calling the API: %s\n" % e)

    try:

        # Query the API to get the most recent "uncertain" score for Tesla
        api_response = api_instance.company_spindex_get_latest_spindex_factors_get(
            ticker=ticker,
            signal_id=signal_id
            )
        print(api_response)

    except ApiException as e:

        # Log an exception if it occurs
        print("Exception when calling the API: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ticker** | **str**|  | [optional] 
 **signal_id** | **str**|  | [optional] 

### Return type

[**InlineResponse20023**](InlineResponse20023.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **company_spindex_get_latest_spindex_overall_risk_get**
> InlineResponse20023 company_spindex_get_latest_spindex_overall_risk_get(ticker)

GetLatestSpindexOverallRisk

### Example

This API allows the user to get the latest overall risk score for a company using the company's ticker. An example is shown below:
```python
import os

from dotenv import load_dotenv
import openapi_client
from openapi_client.rest import ApiException

# Load the environment variables from the .env file
load_dotenv()

EMAIL = os.getenv('EMAIL')
PASSWORD = os.getenv('PASSWORD')

# Define the API configuration, client object and API instance
configuration = openapi_client.Configuration(
    host = 'https://data.app.alphaiq.ai/api/v1'
    )

with openapi_client.ApiClient(configuration) as api_client:

    # Make an instance of the API class
    api_instance = openapi_client.InvestmentResearchersApi(api_client)

    # Define the values needed to authenticate to the API
    content_type = 'application/json' # str | 
    inline_object = openapi_client.InlineObject(
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

with openapi_client.ApiClient(configuration) as api_client:

    # Make an instance of the API class
    api_instance = openapi_client.InvestmentResearchersApi(api_client)
    ticker = 'TSLA' 

    try:
        # Get the latest overall risk score from the API
        api_response = api_instance.company_spindex_get_latest_spindex_overall_risk_get(
            ticker=ticker
            )
        print(api_response)

    except ApiException as e:

        # Log an exception if it occurs
        print("Exception when calling the API: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ticker** | **str**| The ticker that corresponds to the company that you want to pull the latest overall risk score for. | 

### Return type

[**InlineResponse20023**](InlineResponse20023.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **company_spindex_get_timeseries_spindex_factors_get**
> InlineResponse20022 company_spindex_get_timeseries_spindex_factors_get(ticker, start_date, end_date, signal_id=signal_id)

GetTimeseriesSpindexFactors

### Example

The company_spindex_get_timeseries_spindex_factors API allows us to get a timeseries of the spindex factors for a given company. We can get all spindex factors or filter to only a single factor by providing a signal ID. An example is shown below:
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
    host = 'https://data.app.alphaiq.ai/api/v1'
    )

with openapi_client.ApiClient(configuration) as api_client:

    # Make an instance of the API class
    api_instance = openapi_client.InvestmentResearchersApi(api_client)

    # Define the values needed to authenticate to the API
    content_type = 'application/json' # str | 
    inline_object = openapi_client.InlineObject(
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

with openapi_client.ApiClient(configuration) as api_client:

    # Make an instance of the API class
    api_instance = openapi_client.InvestmentResearchersApi(api_client)

    ticker = 'AAPL'
    start_date = '2024-01-01'
    end_date = '2024-02-09'
    signal_id = 'CONSTRAINED-VALUE'

    try:

        # Query the API to get the timeseries of constrained spindex factors from 2024-01-01 to 2024-02-09 for Apple
        api_response = api_instance.company_spindex_get_timeseries_spindex_factors_get(
            ticker=ticker,
            start_date=start_date,
            end_date=end_date,
            signal_id=signal_id
            )
        print(api_response)

    except ApiException as e:

        # Log an exception if it occurs
        print("Exception when calling the API: %s\n" % e)

    try:

        # Query the API to get the timeseries of ALL spindex factors from 2024-01-01 to 2024-02-09 for Apple
        api_response = api_instance.company_spindex_get_timeseries_spindex_factors_get(
            ticker=ticker,
            start_date=start_date,
            end_date=end_date
            )
        print(api_response)

    except ApiException as e:

        # Log an exception if it occurs
        print("Exception when calling the API: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ticker** | **str**| The ticker that corresponds to the company that you want to pull time series data for. | 
 **start_date** | **str**| The start date for the time series you wish to pull (in the format YYYY-MM-DD). | 
 **end_date** | **str**| The end date for the time series you wish to pull (in the format YYYY-MM-DD).. | 
 **signal_id** | **str**| The signal ID that you want to filter to. If not provided, all available signals will be returned by the API. | [optional] 

### Return type

[**InlineResponse20022**](InlineResponse20022.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **company_spindex_get_timeseries_spindex_overall_risk_get**
> InlineResponse20022 company_spindex_get_timeseries_spindex_overall_risk_get(ticker, start_date, end_date)

GetTimeseriesSpindexOverallRisk

### Example

The company_spindex_get_timeseries_spindex_overall_risk API allows us to get a timeseries of the overall risk spindex factor for a company using the company's ticker. An example is shown below:
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
    host = 'https://data.app.alphaiq.ai/api/v1'
    )

with openapi_client.ApiClient(configuration) as api_client:

    # Make an instance of the API class
    api_instance = openapi_client.InvestmentResearchersApi(api_client)

    # Define the values needed to authenticate to the API
    content_type = 'application/json' # str | 
    inline_object = openapi_client.InlineObject(
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

with openapi_client.ApiClient(configuration) as api_client:

    # Make an instance of the API class
    api_instance = openapi_client.InvestmentResearchersApi(api_client)

    ticker = 'TSLA'
    start_date = '2024-01-01'
    end_date = '2024-01-20'

    try:

        # Query the API to get the timeseries of the overall risk spindex factor from 2024-01-01 to 2024-01-20 for Tesla
        api_response = api_instance.company_spindex_get_timeseries_spindex_overall_risk_get(
            ticker=ticker,
            start_date=start_date,
            end_date=end_date
            )
        print(api_response)

    except ApiException as e:

        # Log an exception if it occurs
        print("Exception when calling the API: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ticker** | **str**| The ticker that corresponds to the company that you want to pull time series data for. | 
 **start_date** | **str**| The start date for the time series you wish to pull (in the format YYYY-MM-DD). | 
 **end_date** | **str**| The end date for the time series you wish to pull (in the format YYYY-MM-DD). | 

### Return type

[**InlineResponse20022**](InlineResponse20022.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **company_spinsights_report_ticker_get**
> InlineResponse20020 company_spinsights_report_ticker_get(ticker)

SpinsightsReportPDF

Get pre-signed URL for a company's generative SPINSIGHTS PDF report

### Example

This API allows the user to retrieve a download link for the SPINSIGHTS PDF report for a company. An example is provided below:
```python
import os

from dotenv import load_dotenv
import openapi_client
from openapi_client.rest import ApiException

# Load the environment variables from the .env file
load_dotenv()

EMAIL = os.getenv('EMAIL')
PASSWORD = os.getenv('PASSWORD')

# Define the API configuration, client object and API instance
configuration = openapi_client.Configuration(
    host = 'https://data.app.alphaiq.ai/api/v1'
    )

with openapi_client.ApiClient(configuration) as api_client:

    # Make an instance of the API class
    api_instance = openapi_client.InvestmentResearchersApi(api_client)

    # Define the values needed to authenticate to the API
    content_type = 'application/json' # str | 
    inline_object = openapi_client.InlineObject(
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

with openapi_client.ApiClient(configuration) as api_client:

    # Make an instance of the API class
    api_instance = openapi_client.InvestmentResearchersApi(api_client)
    ticker = 'TSLA' 

    try:

        # Query the API to get a link to the SpinsightsReport PDF for a given company
        api_response = api_instance.company_spinsights_report_ticker_get(
            ticker=ticker
            )
        print(api_response)

    except ApiException as e:

        # Log an exception if it occurs
        print("Exception when calling the API: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ticker** | **str**| Ticker identifier corresponding to a security or company | 

### Return type

[**InlineResponse20020**](InlineResponse20020.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**404** | InsufficientPermissions |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **factor_library_compass_questions_get**
> InlineResponse20029 factor_library_compass_questions_get(question_id=question_id)

GetCompassQuestions

### Example

The factor_library_compass_questions API allows you to retrieve the list of compass questions. Optionally, you can filter to a single question as well. An example is shown below:
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
    host = 'https://data.app.alphaiq.ai/api/v1'
    )

with openapi_client.ApiClient(configuration) as api_client:

    # Make an instance of the API class
    api_instance = openapi_client.InvestmentResearchersApi(api_client)

    # Define the values needed to authenticate to the API
    content_type = 'application/json' # str | 
    inline_object = openapi_client.InlineObject(
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

with openapi_client.ApiClient(configuration) as api_client:

    # Make an instance of the API class
    api_instance = openapi_client.InvestmentResearchersApi(api_client)
    question_id = 1 # int | Question number 1 - 18 (optional)

    try:

        # Query the API to get all questions
        api_response = api_instance.factor_library_compass_questions_get()
        print(api_response)

    except ApiException as e:

        # Log an exception if it occurs
        print("Exception when calling the API: %s\n" % e)

    try:

        # Query the API to only get question 1
        api_response = api_instance.factor_library_compass_questions_get(question_id=question_id)
        print(api_response)

    except ApiException as e:

        # Log an exception if it occurs
        print("Exception when calling the API: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **question_id** | **int**| Question number 1 - 18 | [optional] 

### Return type

[**InlineResponse20029**](InlineResponse20029.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **factor_library_spindex_factors_get**
> InlineResponse20028 factor_library_spindex_factors_get(spindex_id=spindex_id)

GetSpindexFactors

### Example

The factor_library_spindex_factors API allows the user to query the spindex factors and descriptions. Optionally, they can filter to a single factor as well. An example is shown below:
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
    host = 'https://data.app.alphaiq.ai/api/v1'
    )

with openapi_client.ApiClient(configuration) as api_client:

    # Make an instance of the API class
    api_instance = openapi_client.InvestmentResearchersApi(api_client)

    # Define the values needed to authenticate to the API
    content_type = 'application/json' # str | 
    inline_object = openapi_client.InlineObject(
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

with openapi_client.ApiClient(configuration) as api_client:

    # Make an instance of the API class
    api_instance = openapi_client.InvestmentResearchersApi(api_client)
    spindex_id = 'uncertain'

    try:

        # Query the API to get all of the spindex factors
        api_response = api_instance.factor_library_spindex_factors_get()
        print(api_response)

    except ApiException as e:

        # Log an exception if it occurs
        print("Exception when calling the API: %s\n" % e)

    try:

        # Query the API to get the uncertain spindex factor
        api_response = api_instance.factor_library_spindex_factors_get(
            spindex_id=spindex_id
            )
        print(api_response)

    except ApiException as e:

        # Log an exception if it occurs
        print("Exception when calling the API: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **spindex_id** | **str**| Spindex factor name | [optional] 

### Return type

[**InlineResponse20028**](InlineResponse20028.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generative_company_compass_report_content_ticker_get**
> InlineResponse20025 generative_company_compass_report_content_ticker_get(ticker)

GetCompassReportContent

### Example

The generative_company_compass_report_content API allows the user to retrieve the content from the Compass Report for a given company programmatically.
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
    host = 'https://data.app.alphaiq.ai/api/v1'
    )

with openapi_client.ApiClient(configuration) as api_client:

    # Make an instance of the API class
    api_instance = openapi_client.InvestmentResearchersApi(api_client)

    # Define the values needed to authenticate to the API
    content_type = 'application/json' # str | 
    inline_object = openapi_client.InlineObject(
        email = EMAIL,
        password = PASSWORD
    )

    try:

        # Authenticate using your credentials
        api_response = api_instance.auth_gettoken_post(
            content_type=content_type,
            inline_object=inline_object
            )

    except ApiException as e:

        # Log an exception if it occurs
        print("Exception when calling the API: %s\n" % e)

    # Extract your bearer token for authentication to other API paths
    id_token = api_response.data.id_token

    # Add the bearer token to the configuration for authenticating other routes
    setattr(configuration, 'access_token', id_token)

with openapi_client.ApiClient(configuration) as api_client:

    # Make an instance of the API class
    api_instance = openapi_client.InvestmentResearchersApi(api_client)
    ticker = 'WMT'

    try:

        # Query the API to retrieve the content from Walmart's Compass report
        api_response = api_instance.generative_company_compass_report_content_ticker_get(ticker)
        print(api_response)

    except ApiException as e:

        # Log an exception if it occurs
        print("Exception when calling the API: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ticker** | **str**|  | 

### Return type

[**InlineResponse20025**](InlineResponse20025.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generative_company_question_answer_ticker_get**
> InlineResponse20026 generative_company_question_answer_ticker_get(ticker)

GetCompassExplorerQuestionAnswer

Get the COMPASS Explorer Question & Answer results.

### Example

The generative_company_question_answer API allows a user to query the question/answer portion of a Compass report using the company's ticker. An example is shown below:
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
    host = 'https://data.app.alphaiq.ai/api/v1'
    )

with openapi_client.ApiClient(configuration) as api_client:

    # Make an instance of the API class
    api_instance = openapi_client.InvestmentResearchersApi(api_client)

    # Define the values needed to authenticate to the API
    content_type = 'application/json' # str | 
    inline_object = openapi_client.InlineObject(
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

with openapi_client.ApiClient(configuration) as api_client:

    # Make an instance of the API class
    api_instance = openapi_client.InvestmentResearchersApi(api_client)
    ticker = 'WMT'

    try:

        # Query the API to retrieve the question/answer content from Walmart's report
        api_response = api_instance.generative_company_question_answer_ticker_get(
            ticker=ticker
            )
        print(api_response)

    except ApiException as e:

        # Log an exception if it occurs
        print("Exception when calling the API: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ticker** | **str**|  | 

### Return type

[**InlineResponse20026**](InlineResponse20026.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generative_company_spinsights_explorer_ticker_get**
> InlineResponse2003 generative_company_spinsights_explorer_ticker_get(ticker)

GetSpinsightsExplorer

Get the most recent generative SPINSIGHTS Explorer data for a company. This content explains the underlying drivers of the 9 SPINDEX Factors.

### Example

The generative_company_spinsights_explorer API allows the user to get the most recent generative SPINSIGHTS Explorer data for a company. An example is shown below:
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
    host = 'https://data.app.alphaiq.ai/api/v1'
    )

with openapi_client.ApiClient(configuration) as api_client:

    # Make an instance of the API class
    api_instance = openapi_client.InvestmentResearchersApi(api_client)

    # Define the values needed to authenticate to the API
    content_type = 'application/json' # str | 
    inline_object = openapi_client.InlineObject(
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

with openapi_client.ApiClient(configuration) as api_client:

    # Make an instance of the API class
    api_instance = openapi_client.InvestmentResearchersApi(api_client)
    ticker = 'WMT' 

    try:

        # Query the API to get the Spinsights report content
        api_response = api_instance.generative_company_spinsights_explorer_ticker_get(
            ticker=ticker
            )
        print(api_response)

    except ApiException as e:

        # Log an exception if it occurs
        print("Exception when calling the API: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ticker** | **str**|  | 

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generative_company_spinsights_report_content_ticker_get**
> InlineResponse20024 generative_company_spinsights_report_content_ticker_get(ticker)

GetSpinsightsReportContent

Get the most recent SPINSIGHTS report content for a company. This report content specifically highlights the company's language which is more prominent than peers.  Note: the \"SPINDEX Summary\" is present in this report endpoint but not the GetCompassReportContent. This should avoid duplicate information.

### Example

The generative_company_spinsights_report_content API allows a user to get the most recent SPINSIGHTS report content for a company by providing the company's ticker. An example is included below:
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
    host = 'https://data.app.alphaiq.ai/api/v1'
    )

with openapi_client.ApiClient(configuration) as api_client:

    # Make an instance of the API class
    api_instance = openapi_client.InvestmentResearchersApi(api_client)

    # Define the values needed to authenticate to the API
    content_type = 'application/json' # str | 
    inline_object = openapi_client.InlineObject(
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

with openapi_client.ApiClient(configuration) as api_client:

    # Make an instance of the API class
    api_instance = openapi_client.InvestmentResearchersApi(api_client)
    ticker = 'WMT' 

    try:

        # Query the API to get the Spinsights report content
        api_response = api_instance.generative_company_spinsights_report_content_ticker_get(
            ticker=ticker
            )
        print(api_response)

    except ApiException as e:

        # Log an exception if it occurs
        print("Exception when calling the API: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ticker** | **str**|  | 

### Return type

[**InlineResponse20024**](InlineResponse20024.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

