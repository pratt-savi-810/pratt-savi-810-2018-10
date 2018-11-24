import urllib.request


def download_file_from_web(url, file_name):
    # Download the file from `url` and save it locally under `file_name`:
    urllib.request.urlretrieve(url, file_name)


def main():
    download_data = {
        "zoning": "https://www1.nyc.gov/assets/planning/download/zip/data-maps/open-data/nycgiszoningfeatures_201808shp.zip",
        "boro_boundary": "http://www1.nyc.gov/assets/planning/download/zip/data-maps/open-data/nybb_17c.zip",
        "sidewalk_cafes": "https://www1.nyc.gov/assets/planning/download/zip/data-maps/open-data/nycgissidewalkcafe_201808shp.zip"
    }

    download_location = "Z:/Windows/GitHub/pratt-savi-810-2018-10/temp" C:\Users\ksutton\Documents\GitHub\pratt-savi-810-2018-10\projects\KSutton_project\Data

    for key, url in download_data.items():

        print('downloading {0} data, from url: {1}'.format(key, url))

        download_file_from_web(
            url,
            '{0}/{1}.zip'.format(download_location, key)
        )


if __name__ == '__main__':
    main()