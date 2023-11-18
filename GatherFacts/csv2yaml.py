# Import the csv library
import csv

# Open the sample csv file, and create a csv.reader object
with open("Show_Version_Output_new.csv") as f:
    csv_2_yaml = csv.reader(f)
    # Loop over each row in csv and leverage the data in yaml
    print("---\n")
    for row in csv_2_yaml:
       print (f"{row[0]}:\n   hostname: {row[1]}\n   group:\n      - {row[2]}")
       count=(len(row))
       i=3
       while i<count:
            print(f"      - {row[i]}")
            i=i+1
