import zipfile


def unzip_file(zip_file_name, extract_location):
    # Download the file from `url` and save it locally under `file_name`:
    zip = zipfile.ZipFile(zip_file_name, 'r')
    zip.extractall(extract_location)


def main():
    input_zipfile = 'Z:/Windows/GitHub/pratt-savi-810-2018-10/temp/nybb_17c.zip'
    zipfile_extraction_location = "Z:/Windows/GitHub/pratt-savi-810-2018-10/temp"

    unzip_file(input_zipfile, zipfile_extraction_location)


if __name__ == '__main__':
    main()
