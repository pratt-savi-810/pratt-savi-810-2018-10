**Final Project Description**

*Toronto bikeshare analysis*

This project creates a network analyst map of bike routes in Toronto and shows the shortest travel route from one bikeshare station to another.

This project is useful, since numbers of bikes at stands change dynamically, and this data can be accessed in realtime.

All information comes from the Toronto Open Data portal.

*Procedure*

* Pull bikeshare station data

	* Read Lat/Long information from json file

	* Place points on map

* Pull Toronto Bikeways dataset

	* This is a full street/river/rail/etc. line dataset for Toronto

		* It is enhanced with data detailing bike paths

	* Select potential bike routes - filter for the following data types:

		* local road

		* collector road

		* collector ramp

		* minor arterial

		* minor arterial ramp

		* laneway

		* any road that has a comment in the CP_TYPE field (Bikeway Types)

* Add weights to the bike routes

	* Dedicated bikeways have lowest weight

	* The busier the street segment, the higher the weight

* Create new points dataset

	* Create points at closest point on street network to each bikestand

		* These will be the entry points for the network analyst layer

		* User must walk (highest time penalty) to/from the nearest stand

* Create a geodatabase for the network

	* Upload street and stations data

	* Set-up weights for travel through network and other parameters

	* Build network

* Perform sample analysis in network

	* Route of least resistance between two points	