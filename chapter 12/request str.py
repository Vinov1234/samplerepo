import requests
url = "https://www.flipkart.com/"
response = requests.get(url=url)
print(type(response.text))
