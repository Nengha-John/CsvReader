#The script reads through the csv file ,updates the required categories and writes the content into a new .csv file
#Keywords that represent a particular category with a unique code
#Make sure maneno unayoweka hapa yanaappear zaidi katika context ya mafile yako
#If many caterogies, you can add in the data dictionary
#My files had health context so my list has only health categories, be sure to verify your category before using the script
#Make sure to change the name of the old file and new file each time you run the script for multiple files
#Make sure all the files are in the same directory as the script and execute from the terminal


import csv
print('Start')
data = { 
    'A1' : ['Maneno ambayo yako related na category husika'],
    'A2': ['Maneno ambayo yako related na category husika'],
    'A3': ['Maneno ambayo yako related na category husika'],
    'A4' :  ['Maneno ambayo yako related na category husika'],
    'A5':  ['Maneno ambayo yako related na category husika'],
    'A6':  ['Maneno ambayo yako related na category husika'],
    'A7':  ['Maneno ambayo yako related na category husika']
    }

#Open the file that has the particular data
with open('name_of_file.csv', newline='') as csv_file:
    file = csv.reader(csv_file,delimiter=',')
    #Loop through each row in the file
    for row in file:
        print('     ')
        print("Row before:")
        print(row)
        print('<<<<<<<*******************>>>>>>')
        ids = []
        #Check if the keywords in the dictionaries appear in the messages
        for key,wordlist in data.items():
            for word in wordlist:
                if word in row[2] and key not in ids:
                    #Store the keys in a single list
                        ids.append(key)
        #Create a copy of the csv file that will store the filled version
        with open('name_of_new_csv_file_(filled).csv',mode='a') as csvFileR:
            write = csv.writer(csvFileR,delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for id in ids:
                if id not in row[0]:
                    #Append the list into the csv file
                     row[0] = ','.join(ids)
            write.writerow(row)
            print("Row After")
            print(row)
            print('     ')
            print('     ')
            print('Write Successful.')
    csv_file.flush()
    csv_file.close()
print('Finished.')     

