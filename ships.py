import csv
import time
from datetime import datetime
from dateutil.parser import parse


# Opens read / write
def clearLines():
    with open('data/raw.csv', 'rb') as infile, open('data/manifest.csv', 'wt') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        for row in reader:
            if row[0] != "":
                writer.writerow(row)


# Creates a string and writes to .txt
def formString():
    with open('data/manifest.csv', 'rb') as infile, open('data/manifest.txt', 'wt') as outfile:
        reader = csv.reader(infile)
        months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

        for row in reader:
            migrantFirstName = row[0].title()
            migrantSurName = row[1].title()
            migrantAge = str(int(row[2].split(' ')[1]))
            migrantCountry = row[3].title()
            migrantEmbark = row[4].title()
            migrantDate = datetime.strptime(row[5], "%m/%d/%Y")
            migrantDate = "{0:} {1:} {2:}".format(months[migrantDate.month - 1], migrantDate.day, migrantDate.year)
            migrant = migrantFirstName + ' ' + migrantSurName + ', aged ' + migrantAge + ', from ' + migrantCountry + ', ' + 'arrived in New York on ' + migrantDate + ', having embarked from ' + migrantEmbark + '.\n'
            outfile.write(migrant)


# Call functions
clearLines()
formString()
