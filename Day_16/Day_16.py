#CSV....comma separeted values...the python csv module makes it easy to parse CSV files
#they are simply simplified spreadsheets stored as plaintext files
#each line in a CSV file represents a row in spreadshet and commas separate the cells in the row

#Reader Objects
#to read data from a Csv file with the csv module, you neeed to create a Reader object...a reader object lets you iterate over lines in the CSV file an example
import csv
exampleFile = open('example.csv')
exampleReader = csv.reader(exampleFile)
exampleData = list(exampleReader)
print(exampleData)
#dispays
#[['4/5/2015 13:34', 'Apples', '73'], ['4/5/2015 3:41', 'Cherries', '85'],
#['4/6/2015 12:46', 'Pears', '14'], ['4/8/2015 8:59', 'Oranges', '52'],
#['4/10/2015 2:07', 'Apples', '152'], ['4/10/2015 18:10', 'Bananas', '23'],
#['4/10/2015 2:40', 'Strawberries', '98']]

#you can access the value at a particular row and column with the expression exampleData[row][col], where row is the index of one of the lists in exampleData and col is the index of one of the lists in exampleData and col is the index of the item you want from that list
print(exampleData[0][1])#displays apple

#reading Data from Reader Objects in a for loop...especially for large CSV files

for row in exampleReader:
	print('Row #' + str(exampleReader.line_num) + ' ' + str(row))#note that line_num is a variable that contains the number of the current line
	#this will display
#Row #1 ["[['4/5/2015 13:34'", " 'Apples'", " '73']", " ['4/5/2015 3:41'", " 'Cherries'", " '85']", '']
#Row #2 ["['4/6/2015 12:46'", " 'Pears'", " '14']", " ['4/8/2015 8:59'", " 'Oranges'", " '52']", '']
#Row #3 ["['4/10/2015 2:07'", " 'Apples'", " '152']", " ['4/10/2015 18:10'", " 'Bananas'", " '23']", '']
#Row #4 ["['4/10/2015 2:40'", " 'Strawberries'", " '98']]"]


#writer Objects...they let you write data to a CSV file
outputFile = open('output.csv','w',newline='')#note that on Windows you'll need to pass a blank string fo rthe open()fundtion's newline keyword argument
outputWriter = csv.writer(outputFile)
outputWriter.writerow(['spam','eggs','bacon','ham'])#this adds to the output.csv file...when you print this line its return value is the number of characters written to the file 
outputWriter.writerow(['hall,world','eggs','bacon','ham'])#this object automatically escapes the comma in the value 'hallo,world'


#The delimiter and lineterminator keyword Arguments
#for this you do
outputWriter = csv.writer(outputFile,delimiter='\t',lineterminator='\n\n')

