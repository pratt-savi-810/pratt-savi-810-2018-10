import zipfile


#  create a list of zip file names to unzip

filename_list = []

your_downloads_folder = "C:/Users/jbagtas/Downloads/"

for i in range(1, 21):
    if i < 10:
        filename_list.append(
            str(your_downloads_folder) + "wma0" + str(i) + ".zip")
    else:
        filename_list.append(
            str(your_downloads_folder) + "wma" + str(i) + ".zip")

#  also include the NJ road network zip file
filename_list.append(
    str(your_downloads_folder) + "NJ_Roads_shp.zip"
)

#  unzip files from the location listed in filename_list into the specified folder (your_project_folder)


def unzip_file(zip_file_name, extract_location):
    zip_object = zipfile.ZipFile(zip_file_name, 'r')
    zip_object.extractall(extract_location)


#  designate the folder where you want to extract the data

your_project_folder = "C:/Users/jbagtas/Documents/"

# extract the data
for i in range(len(filename_list)):
    unzip_file(
        filename_list[int(i) - 1],
        your_project_folder
    )



