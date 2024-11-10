import xml.etree.ElementTree as ET

# Load XML file
tree = ET.parse('MUSIT_arkeologi.xml')
root = tree.getroot()

# Access data
for child in root:
    print(child.tag, child.attrib)  # Prints tag and attributes of each element

# To access specific elements
for element in root.findall('tag_name'):
    print(element.text)  # Prints the text of specific tags

##########################
import xml.etree.ElementTree as ET
import pandas as pd

# Parse the XML file
tree = ET.parse('MUSIT_arkeologi.xml')
root = tree.getroot()

# Initialize a list to hold the data
data = []

# Iterate over each <Entity> element in the XML tree
for entity in root.findall('Entity'):
    record = {
        'id': entity.get('id'),
        'MuseumNo': entity.find('MuseumNo').text if entity.find('MuseumNo') is not None else None,
        'Artefact': entity.find('Artefact').text if entity.find('Artefact') is not None else None,
        'County': entity.find('County').text if entity.find('County') is not None else None,
        'Municipality': entity.find('Municipality').text if entity.find('Municipality') is not None else None,
        'Period': entity.find('Period').text if entity.find('Period') is not None else None,
        'Form': entity.find('Form').text if entity.find('Form') is not None else None,
        'Material': entity.find('Material').text if entity.find('Material') is not None else None,
        'CadastralName': entity.find('CadastralName').text if entity.find('CadastralName') is not None else None,
        'CadastralNo': entity.find('CadastralNo').text if entity.find('CadastralNo') is not None else None,
        'PropertyName': entity.find('PropertyName').text if entity.find('PropertyName') is not None else None,
        'PropertyNo': entity.find('PropertyNo').text if entity.find('PropertyNo') is not None else None,
        'FindCategory': entity.find('FindCategory').text if entity.find('FindCategory') is not None else None,
        'AcquisitionDate': entity.find('AcquisitionDate').text if entity.find('AcquisitionDate') is not None else None,
        'Description': entity.find('Description').text if entity.find('Description') is not None else None,
        'UTMZone': entity.find('UTMZone').text if entity.find('UTMZone') is not None else None,
        'Projection': entity.find('Projection').text if entity.find('Projection') is not None else None,
        'UTMEast': entity.find('UTMEast').text if entity.find('UTMEast') is not None else None,
        'UTMNorth': entity.find('UTMNorth').text if entity.find('UTMNorth') is not None else None,
        'Latitude': entity.find('Latitude').text if entity.find('Latitude') is not None else None,
        'Longitude': entity.find('Longitude').text if entity.find('Longitude') is not None else None,
        'CoordinatePrecision': entity.find('CoordinatePrecision').text if entity.find('CoordinatePrecision') is not None else None,
        'PdfId': entity.find('PdfId').text if entity.find('PdfId') is not None else None,
        'LocationId': entity.find('LocationId').text if entity.find('LocationId') is not None else None,
        'Museum': entity.find('Museum').text if entity.find('Museum') is not None else None,
    }
    data.append(record)

# Convert the list of records to a DataFrame
df = pd.DataFrame(data)

# Display the first few rows of the DataFrame
print(df.head())

