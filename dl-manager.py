import tkinter as tk
import tkinter.filedialog
import requests
import os

# Create a tkinter window
root = tk.Tk()
root.withdraw()

# Prompt the user for the URL of the file they want to download
url = input("Enter the URL of the file you want to download: ")

# Use the tkinter filedialog to allow the user to choose the local directory
# where they want to save the file
local_directory = tk.filedialog.askdirectory()

# Prompt the user for the local file name
local_filename = input("Enter the local file name (REMEMBER TO PUT THE FILE TYPE): ")

# Create the full local file path by combining the directory and file name
local_filepath = os.path.join(local_directory, local_filename)

# Create the local directory if it does not already exist
if not os.path.exists(os.path.dirname(local_filepath)):
    os.makedirs(os.path.dirname(local_filepath))

# Use the 'get' method of the 'requests' module to download the file
response = requests.get(url)

# Check for any HTTP errors and raise an exception if there is an error
response.raise_for_status()

# Open the local file in 'write binary' mode and write the contents of the
# downloaded file to it
with open(local_filepath, 'wb') as f:
    f.write(response.content)
