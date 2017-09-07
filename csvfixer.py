import csv

reader = csv.reader(open('testdata.csv'))
uniqueIds={}

for row in reader:
        if not ''.join(row).strip():
                continue
        theId= row[2]
        valueToConcatonate=row[0]
        if theId in uniqueIds:
                valueToConcatonate= uniqueIds[theId] +"; "+valueToConcatonate
        uniqueIds[theId] = valueToConcatonate

with open('newcsv.csv','wb') as f:
        for entry in uniqueIds:
                f.write(uniqueIds[entry]+", rand, "+entry)
                f.write('\n')import csv
