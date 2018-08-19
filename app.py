import zillow
import xlsxwriter
import json

key = 'X1-ZWz1glpadyviff_44w9p'

api = zillow.ValuationApi()

address = '9315 West St, Manassas, VA'
postal_code = '20110'

data = api.GetSearchResults(key, address, postal_code)
full_data = data.get_dict()
zestimate = full_data['zestimate']

print json.dumps(full_data, indent=1)


# Create a workbook and add a worksheet.
workbook = xlsxwriter.Workbook('zillow_data.xlsx')
worksheet = workbook.add_worksheet()

# Start from the first cell. Rows and columns are zero indexed.
row = 1     # start row 1 to skip headers
col = 0

# Iterate over the data and write it out row by row.
for field, val in zestimate.iteritems():
    worksheet.write(0, col, field)  # write headers
    worksheet.write(row, col, val)  # write row of data
    col += 1

workbook.close()