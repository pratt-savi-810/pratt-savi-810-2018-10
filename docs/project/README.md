# Identify NYC Subway travel time Destination from two Origin pairs with time restrictions

Data and Inspiration: https://project.wnyc.org/transit-time/

### Dependencies

	pip install ipython
	pip install pandas
	pip install jupyter


### Project Description

After recently look at the WNYC Transit Time map interface, I had an idea that it would be interesting to use their data to select hexagon grids that fall under a time threshold travel time so that two origin locations could be a shared destination with travel time thresholds set. For example, wouldn't it be great to be able to submit two pairs of coordinates, and return where in the city you have equal or preset travel times to get to. This may be useful in planning meeting with folks that live or work in different parts of NYC. So imagine an API you and a friend, one who works in downtown Brooklyn, while you work in midtown Manhattan, could hit to find locations in the city where you could both only have to travel 25 minutes to get to. That way its an equitable travel cost (time) for both parties. Also, if say, we both had restrictions in time to travle to meet at a given time, say 7 pm and one person got out of work at 5 pm, and the other 5:30 pm, the API could have time thresholds for each party, and return hexagons that met the combined travel time restrictions. Next imagine that API returned coffee shops, bars or restaurants that are within those hexagon grids. That may be useful in selecting a place to meet. This project is sample project working on concurrently with students at Pratt SAVI. 


### Project Outline

```
download project files
    * https://project.wnyc.org/transit-time/data/nyc_hexes_2000ft_4326.zip
    * https://project.wnyc.org/transit-time/data/transit-time-json-files.zip

unzip project files

create function to read json file 
    return dictionary

create function to select time threshold, value from key value pair
    return selected keys and values

find origin-destinations that share same destination and valid time value
    create empty dictionary
    loop through one o-d set 
        loop through other o-d set
            if match destination 
                generate dicationary item 
    return matches dictionary 


read json
select by time threshold 
find matches 
return matches dictionary
```
