import requests
r = requests.get('https://en.wikipedia.org/wiki/File:Black_hole_-_Messier_87_crop_max_res.jpg')
with open("blackhole.jpg", "wb") as f:
    f.write(r.content)
