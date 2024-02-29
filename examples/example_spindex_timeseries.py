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

with alphaiq_sdk.ApiClient(configuration) as api_client:

    # Make an instance of the API class
    api_instance = alphaiq_sdk.InvestmentResearchersApi(api_client)

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