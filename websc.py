import csv
from builtins import range
from itertools import zip_longest
import requests
from botocore.config import Config
from bs4 import BeautifulSoup
import boto3.s3
import boto3
from botocore.exceptions import NoCredentialsError
registrationNumber=[]
result=[]
names=[]
marks=[]
missingNumbers=[]
#for x in range(1400000001,1499999999):
for x in range(1417109172,1417109192):
    url="https://www.vidyavision.com/results/ssc2014.aspx?h="+str(x)
    page = requests.get(url).text
    soup = BeautifulSoup(page, "html.parser")
    if(soup.__len__()!=0):
        registrationNumber.append(str(soup).split('~')[0])
        names.append(str(soup).split('~')[1])
        result.append(str(soup).split('~')[-1])
        marks.append(str(soup).rsplit("~")[-3])
        print(str(x)+"OK")
    else:
        missingNumbers.append(x)
        print(str(x) + "Not  OK")
d = [registrationNumber, names,marks,result]
export_data = zip_longest(*d, fillvalue = '')
with open('output.csv', 'w', newline='') as myfile:
      wr = csv.writer(myfile)
      wr.writerow(("registrationNumber", "names","marks","result"))
      wr.writerows(export_data)
myfile.close()
print("Done Writing to file")

# ACCESS_KEY = 'AKIAXX2PATWICUYBJRV7'
# SECRET_KEY = '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'
BUCKET_NAME = 'bjoelr'
FILE_NAME = 'output.csv'
data = open('output.csv', 'rb')
s3 = boto3.resource('s3')
s3.Bucket(BUCKET_NAME).put_object(Key=FILE_NAME,Body=data)
print("Done")