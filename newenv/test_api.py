import urllib3
import requests

# payload = 

# a = requests.get("https://test-world-soda.fusion-tech.pro/api/v1/sodas/1").json()
# print(a)


url = "https://test-world-soda.fusion-tech.pro/api/v1/sodas/parse-csv"

payload = {}
files=[
  ( 
      'file',(
            '2024.09.19 - Soda Mania Database copy.csv',
            open('/home/nikita/Downloads/2024.09.19 - Soda Mania Database copy.csv','rb'),
            'text/csv'
      )
)
]
headers = {
#    'Authorization': 'Bearer'
}

response = requests.request("POST", url, headers=headers, data=payload, files=files)

print(response.text)
