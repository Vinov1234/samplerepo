import requests
url = 'https://www.flipkart.com/'
response = requests.get(url =url)
#print(response.status_code)
#print(response.headers)
#print(response.request.headers)
print(response.content)
