import alphaiq_sdk

def main():
    '''
    Function used for introducing users to the functionality of the AlphaIQ SDK
    '''
    # Introductory text
    print("\nWelcome to the AlphaIQ API. This is a demonstration of the API.\n")
    print("First, you will need to sign in with your AlphaIQ account credentials.\n")
    print("If you have not created an account, please do so now: https://alphaiq.ai\n\n")
    # User inputs email assocated with AlphaIQ account
    email = input("Please provide email: ")
    if email=='':
        print("Error: Email should be a string.")
    elif not isinstance(email, str):
        print("Error: Email should be a string.")
    
    # User inputs password associated with AlphaIQ account
    base64_password = input("Please provide password with base64 encryption applied (https://www.base64encode.org/): ")
    if base64_password=='':
        print("Error: Password should be a string with base64 encryption applied. https://www.base64encode.org/")
        exit()
    elif not isinstance(base64_password, str):
        print("Error: Password should be a string with base64 encryption applied. https://www.base64encode.org/")
        exit()
    elif base64_password[-1]!='=':
        print("Error: Password should be a string with base64 encryption applied. https://www.base64encode.org/")
        exit()
    
    # Retrieve user token    
    token_details = alphaiq_sdk.get_token(email, base64_password)
    token = token_details["data"]["IdToken"]

    # Connect to the AlphaIQ client
    client = alphaiq_sdk.client(token)
    
    # Get example data, a list of identifiers available to the users
    identifiers = client.get_identifiers()
    print(identifiers)
    print("------------------\n")
    print("This returns a list of identifiers that you can use to query the API.\n")
    print("Now you can explore the rest of the API. Please reach out at contact@alphaiq.ai with any questions or feedback.")

if __name__ == '__main__':
    main()


