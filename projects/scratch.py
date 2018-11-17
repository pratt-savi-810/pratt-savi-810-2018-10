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

filename_list.append(
    str(your_downloads_folder) + "NJroads.zip"
)
print(len(filename_list))

