import requests
import json

# Set the CyberArk REST API endpoints
login_url = "https://.privilegecloud.cyberark.com/PasswordVault/API/auth/Cyberark/Logon/"
accounts_url = "https://.privilegecloud.cyberark.com/PasswordVault/API/Accounts"

# Replace with your actual credentials
username = "xxx"
password = "xxx"

# Create a session to persist the authentication

session = requests.Session()

# Authentication request payload
login_payload = {
    "username": username,
    "password": password
}
# Set the headers for the authentication request
login_headers = {
    "Content-Type": "application/json"
}

# Make the authentication request
response = session.post(login_url, data=json.dumps(login_payload), headers=login_headers, verify=False)

# Check if the authentication was successful
if response.status_code == 200:
    print("Authentication successful.")
    
    # Extract the session token from the response
    session_token = response.json()

print(session_token)

    # Set the headers for the accounts request, including the session token
accounts_headers = {
        "Content-Type": "application/json",
        #"Authorization": f"Bearer {session_token}"
        "Authorization": session_token
}

    # Make the request to retrieve the list of accounts
accounts_response = session.get(accounts_url, headers=accounts_headers, verify=False)

print(accounts_response.content)

'''
    # Check if the accounts request was successful
if accounts_response.status_code == 200:
        accounts_data = accounts_response.json()

        # Display the list of accounts (adjust as needed based on the response format)
        print("List of accounts:")
        for account in accounts_data.get("Accounts", []):
            print(account)
        else:
            print(f"Error retrieving accounts. Status code: {accounts_response.status_code}")

else:
    print(f"Authentication failed. Status code: {accounts_response.status_code}")

'''
