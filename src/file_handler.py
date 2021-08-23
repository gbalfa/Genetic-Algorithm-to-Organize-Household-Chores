'''
Librería para el manejo de archivos
'''

import csv
  
def readCSV(filename):
    # initializing the titles and rows list
    fields = []
    rows = []
    
    # reading csv file
    with open(filename, 'r') as csvfile:
        # creating a csv reader object
        csvreader = csv.reader(csvfile, quoting=csv.QUOTE_NONE)
        
        # extracting field names through first row
        fields = next(csvreader)
        
        # extracting each data row one by one
        for row in csvreader:
            int_row = [int(x) for x in row]
            rows.append(int_row)
            
        # get total number of rows
        # print("Total no. of rows: %d"%(csvreader.line_num))
        
    # printing the field names
    # print('Field names are: ' + ', '.join(field for field in fields))
    return rows

def arrangeSchedules(rows, n_time_slots):
    chunks = [rows[x:x+n_time_slots] for x in range(0, len(rows), n_time_slots)]
    return chunks

# csv_rows = readCSV("data/availability.csv")
# schedules = arrangeSchedules(csv_rows, 6)
# print(schedules)
