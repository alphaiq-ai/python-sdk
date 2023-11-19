# AlphaIQ Python SDK
To get access to the API, [sign up here](https://alphaiq.ai).

Welcome to the AlphaIQ API! We offer Quantitative Linguistic Risk Indicators that enable investors to uncover hidden risks in forward-looking statements from management. For a complete API request response.

## Requirements

Python >=3.7

## Installation

```
pip install alphaiq-sdk
```
Then import the package:
```python
import alphaiq_sdk
```
## Installation from GitHub
```
pip install git+https://github.com/alphaiq-ai/python-sdk.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/alphaiq-ai/python-sdk.git`
Then import the package:
```python
import alphaiq_sdk
```
## SDK Code Examples

A jupyter notebook and other code examples for the Alpha IQ SDK are available in our [Getting Started folder](alphaiq_sdk/get_started)

## Getting Started

Please follow the [installation instructions](#installation) and then run the following:

```python
import alphaiq_sdk

# Set user credentials
email = 'bob.ross@gmail.com' #str | The email you signed up with AlphaIQ. To sign up for an account, go to our website: https://alphaiq.ai
base64_password = 'AB23sdf34$=' #str | This is the password for your AlphaIQ account with Base64 encryption applied. Copy your password into this base64 encryption tool to get the encrypted version of your password: https://www.base64encode.org/

# Retrieve user token    
token_details = alphaiq_sdk.get_token(email, base64_password)
token = token_details["data"]["IdToken"]

# Connect to the AlphaIQ client
client = alphaiq_sdk.client(token)

# Get example data, a list of identifiers available to the users
identifiers = client.get_identifiers()
print(identifiers)

# Get example summary information for a particular company, Godaddy Inc
summary = client.get_identifier_details(identifier="Godaddy Inc (GDDY)")
print(summary)

# Get example list of high-risk companies
companies = client.get_high_risk_companies_across_all_industries(view_change='1q')
print(companies)

```


