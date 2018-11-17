
# coding: utf-8

# In[1]:


import arcpy
import pandas as pd
import geocoder


# In[3]:


address_df = pd.read_csv(r'C:\Users\dcook13\Documents\GitHub\pratt-savi-810-2018-10\students\dcook\class4\addresses.csv')


# In[4]:


address_df


# In[5]:


address_df['Lat'] = ''
address_df['Long'] = '' ## adding new columns


# In[6]:


address_df


# In[10]:


# df_test = address_df.set_index('Address')
for index, row in address_df.iterrows():
    # print(index)
    # print(row)
    # print(index,row)
    g = geocoder.arcgis(row['Address'])
    row['Lat'] = g.lat
    row['Long'] = g.lng


# In[11]:


address_df


# In[13]:


address_df.to_csv(r'C:\Users\dcook13\Documents\GitHub\pratt-savi-810-2018-10\students\dcook\class4\addresses_geocoded.csv')


# In[14]:


arcpy.MakeXYEventLayer_management(
    r'C:\Users\dcook13\Documents\GitHub\pratt-savi-810-2018-10\students\dcook\class4\addresses_geocoded.csv',
    'Long',
    'Lat',
    'latlong_plot'
    )
## might result in errors, but 'latlong_plot' will still generate successfully


# In[16]:


arcpy.CopyFeatures_management(
    'latlong_plot',
    r'C:\Users\dcook13\Documents\GitHub\pratt-savi-810-2018-10\students\dcook\class4\plot.shp',
    )

