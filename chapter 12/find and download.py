import requests, os, bs4
comicElem = Soup.select('#comic img')
if comicElem == []:
        print('Could not find comic image.')
else:
        comicUrl = 'https:' + comicElem[0].get('src')
        print('Downloading image %s...' % (comicUrl))
        res = requests.get(comicUrl)
        res.raise_for_status()

print('Done.')

