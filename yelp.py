import requests 
import csv
import json

api_key = '1USXDxhKMHfAu1jpsOCtoquTyv3O2Wadc9ScJsfTq7Sh3_SXf4gsL_P5amJr9ZjT5pxW34s-4NrVrKlzDxjwjafmAXlT28UFxIOCQ4nyHJsPAjzkVk_A7eo7Ct7VXnYx'
headers = {'Authorization': 'Bearer %s' % api_key}

url='https://api.yelp.com/v3/businesses/mQzC5F3oXu4NxybQuQ73hA/reviews'
req = requests.get(url,headers=headers)
parsed = json.loads(req.text)
#print (json.dumps(parsed, indent=4))
reviews = parsed['reviews']
data = open('reviews.csv', 'w')
writer = csv.writer(data)
count = 0
for emp in reviews:

      if count == 0:

             header = emp.keys()

             writer.writerow(header)

             count += 1

      writer.writerow(emp.values())

data.close()
