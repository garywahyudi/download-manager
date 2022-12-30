import click
import os
import requests
import shutil

@click.command()
@click.option("--url", required=True, help="URL of the file to download")
@click.option("--file", required=True, help="local file path to save the file")
def download_file(url, file):
    # Create the local directory if it does not already exist
    if not os.path.exists(os.path.dirname(file)):
        os.makedirs(os.path.dirname(file))

    # Use the 'get' method of the 'requests' module to download the file
    response = requests.get(url, stream=True)

    # Check for any HTTP errors and raise an exception if there is an error
    response.raise_for_status()

    # Get the total file size
    total_size = int(response.headers.get("Content-Length", 0))

    # Open the local file in 'write binary' mode and write the contents of the
    # downloaded file to it
    with open(file, 'wb') as f:
        for chunk in response.iter_content(chunk_size=1024):
            # Write the chunk to the file
            f.write(chunk)
            # Print the progress bar to the console
            downloaded = f.tell()
            progress = downloaded / total_size
            print(f"\r[{'#' * int(30 * progress):<30}] {int(progress * 100)}%", end="", flush=True)

    # Print a completion message
    print(f"{url} download complete")

if __name__ == "__main__":
    download_file()
