 # select and export the cross streets from centerline
# cross street 1
# list_of_cross_streets = ('W  60 ST', 'CATHEDRAL PKWY', 'W  125 ST', 'W  155 ST', 'W  168 ST')
# list_of_test_streets = ('W  62 ST', 'W  63 ST', 'W  64 ST')
# exported_cross_streets = ()
#
# def export_cross_streets(list_of_streets, borocode):
#      for i in list_of_streets:
#          sql_statement = ''' "FULL_STREE"= {0}{1}{0} AND "BOROCODE" = {0}{2}{0} '''.format('~', i, borocode).replace("~", "'")
#          arcpy.FeatureClassToFeatureClass_conversion(
#              centerline,
#              r'E:\SAVI810\Final_Project\Data_Test\shape\cross_streets',
#              "{}_test".format(i.replace(" ", "_")),
#              sql_statement,
#          )
#
# export_cross_streets(list_of_cross_streets,'1')
# export_cross_streets(list_of_test_streets, '1')