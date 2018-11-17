import urllib

#create a list of URLs to download each WMA DEM (WMAs 1 through 20)
url_list = []

for i in range(1, 21):
    if i < 10:
        url_list.append("https://www.nj.gov/dep/gis/digidownload/zips/wmalattice/wma0" + str(i) + "lat.zip")
    else:
        url_list.append("https://www.nj.gov/dep/gis/digidownload/zips/wmalattice/wma" + str(i) + "lat.zip")

print(url_list)

#  create a list of file paths/file names for download
filename_list = []

your_downloads_folder = "C:/Users/jbagtas/Downloads/"

for i in range(1, 21):
    if i < 10:
        filename_list.append(
            str(your_downloads_folder) + "wma0" + str(i) + ".zip")
    else:
        filename_list.append(
            str(your_downloads_folder) + "wma" + str(i) + ".zip")

print(filename_list)

#download all WMA DEMs to the specified file paths
for url_item, filename_item in zip(url_list, filename_list):
    urllib.urlretrieve(url_item, filename_item)


#  download the street network file, then append file location to filename_list
urllib.urlretrieve(
    "https://www.state.nj.us/transportation/gis/zip/NJ_Roads_shp.zip",
    str(your_downloads_folder) + "NJ_Roads_shp.zip"
    )

filename_list.append(
    str(your_downloads_folder) + "NJ_Roads_shp.zip"
)

print(filename_list)
