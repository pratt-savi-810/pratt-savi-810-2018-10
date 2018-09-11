import urllib.request


def download_file_from_web(url, file_name):
    # Download the file from `url` and save it locally under `file_name`:
    urllib.request.urlretrieve(url, file_name)

    # for reference
    # https://stackoverflow.com/questions/7243750/download-file-from-web-in-python-3


def main():
    url = 'http://www1.nyc.gov/assets/planning/download/zip/data-maps/open-data/nybb_17c.zip'
    download_location = "Z:/Windows/GitHub/pratt-savi-810-2018-10/temp/nybb_17c.zip"
    
    download_file_from_web(url, download_location)


if __name__ == '__main__':
    main()
