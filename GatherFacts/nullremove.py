import csv    

myfile = '/home/network-ent/Ehsan_Codes/Show_Version_Output.csv'
newfile = '/home/network-ent/Ehsan_Codes/Show_Version_Output_new.csv'
reader = csv.reader(open(myfile))
remove_me = {'Null'}

# print('Before:')
# print(open(myfile).read())
for row in reader:
    new_row = []
    for column in row:
        if column not in remove_me:
            new_row.append(column)
    csv.writer(open(newfile,'a')).writerow(new_row)
# print('\n\n')
# print('After:')
# print(open(newfile).read())
