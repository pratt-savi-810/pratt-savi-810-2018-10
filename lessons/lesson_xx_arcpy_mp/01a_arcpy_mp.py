import arcpy


def export_layout_to_pdf(aprx, layout_name, output_pdf):
    aprx = arcpy.mp.ArcGISProject(aprx)
    lyt = aprx.listLayouts(layout_name)[0]
    lyt.exportToPDF(output_pdf, resolution=300)


def main():
    export_layout_to_pdf(
        'W:/GIS/ArcGISPro/Author_and_share_a_web_map/portland_buildings.aprx',
        'Buildings',
        'W:/GIS/ArcGISPro/Author_and_share_a_web_map/portland_buildings_v1.pdf',
    )


if __name__ == '__main__':
    main()
