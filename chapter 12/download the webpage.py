import requests, os, bs4
url = 'https://xkcd.com'
os.makedirs('xkcd',exist_ok = True)
while not url.endswith('#'):
    print('downloading page %s....'%url)
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text,'html.parser')
print('done')    
