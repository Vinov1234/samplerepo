import requests, os, bs4
imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)),'wb')
for chunk in res.iter_content(100000):
            imageFile.write(chunk)
            imageFile.close()

    
    prevLink = soup.select('a[rel="prev"]')')[0]
    url = 'https://xkcd.com' + prevLink.get('href')

print('Done.')
