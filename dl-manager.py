import requests
import os

# Prompt the user for the URL of the file they want to download
url = input("Enter the URL of the file you want to download: ")

# Prompt the user for the local file name and path where they want to save the file
local_filename = input("Enter the local file name and path where you want to save the file: ")

# Create the local directory if it does not already exist
if not os.path.exists(os.path.dirname(local_filename)):
    os.makedirs(os.path.dirname(local_filename))

# Use the 'get' method of the 'requests' module to download the file
response = requests.get(url)

# Check for any HTTP errors and raise an exception if there is an error
response.raise_for_status()

# Open the local file in 'write binary' mode and write the contents of the
# downloaded file to it
with open(local_filename, 'wb') as f:
    f.write(response.content)
