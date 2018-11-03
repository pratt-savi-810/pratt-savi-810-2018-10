# Data input

soil data within NYC(change proprietary data results by editing in excel with lat/long points)
tax parcel lots

# Output

map of interested area with buffer of sampling points

# Process

make up data in CSV
unzip file code (soil)
convert CSV to shapefile
add in tax parcel data

select the interested area
create a buffer within area
select all soil data points over a certain "arsenic" threshold
    file = soil data
    select = soil data intersecting buffer & where 'aresnic' is greater than XX

If i have extra time, print the arsenic data to a CSV file showing the Sample ID, lat/long, and arsenic result



