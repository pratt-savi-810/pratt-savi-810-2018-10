# Identify Rent Stabilized Buildings in Brooklyn NY

[![watch the video](https://img.youtube.com/vi/rB3tkYohPnk/hqdefault.jpg)]

[Code Recording Link](https://youtu.be/rB3tkYohPnk)

Project Description

The goal of this project is to map the locations of rent stabilzed buildings in Brooklyn, New York, to later examine the income levels of the population living in the communities where these buildings are more prevalent.

Project Outline

download project files

    * https://www1.nyc.gov/assets/planning/download/zip/data-maps/open-data/bk_mappluto_18v1.zip
    * https://www1.nyc.gov/assets/rentguidelinesboard/pdf/2016brooklynbldgs.pdf
    
unzip project files

Converted list of rent stabilized buildings from pdf to csv and manually created Borough,Block and Lot number(BBL) field
to be able to join this table to the BKMapPLUTO shapefile. Also geocoded the addresses of the rent stabilized buildings using the
US Census Bureau Geocoder. 


    wrote function to create geodatabase
    
    wrote function to convert shapefile to feature class
        added new BKMapPLUTO feature class to geodatabase 
                     
    wrote function to convert csv file to geodatabase table
        added new table to geodatabase    
         
    wrote function to join table to shapefile in geodatabase
    
    then symbolized rent stabilized buildings in ArcMap
    



