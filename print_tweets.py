import csv



with open('tweets.csv') as csv_file:
  csv_reader=csv.reader(csv_file,delimiter=',')
  line_count=0
  for row in csv_reader:
    print (row[1])