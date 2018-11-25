project_data_folder = "C:/Users/bagta/Documents/810 Project/"

data_path = []

for i in range(1, 21):
    if i < 10:
        data_path.append(str(project_data_folder) + "wma0" + str(i) + "/wma0" + str(i) + "lat")
    else:
        data_path.append(str(project_data_folder) + "wma" + str(i) + "/wma" + str(i) + "lat")

#  add the road network
data_path.append(str(project_data_folder) + "NJ_Roadway_Network.shp")

print(data_path)

