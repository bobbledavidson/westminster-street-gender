import sexmachine.detector as gender
import csv
import re

d = gender.Detector()

male = 0
female= 0
andy = 0
new_rows_list = []

with open('CityofWestminsterLondres.csv', 'rU') as csvfile:
     spamreader = csv.reader(csvfile, delimiter=',')
     for row in spamreader:
         name = row[0]
         namesplit = re.split("\.| |'",name)
         name_score = 0

         for n in namesplit:
         	if n=='Augustine' or n=='Jude':
         		name_score +=1
         	else:
         		if n !='The' and n!='Piccadilly' and n!='York' and n!='Warwick':
		         	gen = d.get_gender(n)
		                if gen=='andy':
		                    name_score +=0
		                elif gen=='male':
		                    name_score +=1
		                else:
		                    name_score -=1
         new_row = [row[0],row[1],name_score]
         new_rows_list.append(new_row)


with open('results.csv', 'wb') as csvfile:
	spamwriter = csv.writer(csvfile, delimiter =',',quoting=csv.QUOTE_NONE, escapechar="/")
	for row in new_rows_list:
		spamwriter.writerow(row)

