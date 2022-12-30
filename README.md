# Download-Manager (DL-Manager)

DL-Manager is a Python-based CLI download utility where is useful when no browser is available and cases where you want a simple terminal download manager whereas things like wget and curl isn't for you.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install additional requirements if you want to make changes to it on your own. In cases where your Python version doesn't have the library I use, feel free to download it.

```bash
pip install requests os click shutil
```


## Usage

To use the CLI, you would need to run the script in a terminal and pass the required arguments to the command. For example:
```python
python dl-manager.py --url https://www.example.com/file.zip --file /path/to/local/file.zip
```

This would download the file located at https://www.example.com/file.zip and save it to the local path /path/to/local/file.zip. The progress of the download will be displayed in the console as a progress bar.

You can also use the --help flag to see the available options and their descriptions:
```python
python dl-manager.py --help
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[GPLv3](https://www.gnu.org/licenses/gpl-3.0.en.html)
