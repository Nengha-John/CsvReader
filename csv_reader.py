import csv
print('Start')
#Keywords that represent a particular category with a unique code
#Make sure maneno unayoweka hapa yanaappear zaidi katika context ya mafile yako
#If many caterogies, you can add in the data dictionary
#My files had health context so my list has only health categories, be sure to verify your category before using the script
#Make sure to change the name of the old file and new file each time you run the script for multiple files
#Make sure all the files are in the same directory as the script and execute from the terminal

data = { 
    'A1' : ['ujauzito','mimba','umeshajifungua','kujifungua','jifungua','mimba','mjamzito','mama na mtoto'],
    'A2':['corona','covid','covid-19','kifua','mafua makali'],
    'A3':['chanjo','sindano'],
    'A4' : ['mtoto','kuharisha','chanjo','kuhara','utapiamlo'],
    'A5': ['uzito','nyonya','nyonyesha','mtoto mchanga','maziwa','urefu','kipimo'],
    'A6': ['mtoto','kijana','uzazi','balehe','kubalehe','elimu ya uzazi','msichana','mvulana'],
    'A7': ['afya','kliniki','dawa','shinikizo la damu','damu','presha','kupima','kipimo']
    }

#Open the file that has the particular data
with open('user27_Msgs_File_4.csv', newline='') as csv_file:
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
        with open('user27_Msgs_File_4(filled).csv',mode='a') as csvFileR:
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

