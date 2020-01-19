import csv

with open('43rd_Congress.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    classes = []
    for row in csv_reader:
        if line_count == 0:
            #print(f'Column names are {", ".join(row)}')
            line_count += 1
        classes.append(row["name"])
        line_count += 1
    #print(f'Processed {line_count} lines.')
    #print (classes)
    command = ""
    for i in classes:
        #print(i)
        command += "CREATE TABLE "
        command += i
        command += " (C_Number int,Lecture json, Lab json, Tutorial json, Seminar json, Workshop json);"
    print (command)