from pinterest_scraper import scraper as s
from pathlib import Path

res_dir = './results'
Path(res_dir).mkdir(exist_ok=True);

ph = s.Pinterest_Helper(login="dapda1202@gmail.com", pw="Asdasd12")
url = "https://www.pinterest.com/search/pins/?q=logo%20lion&rs=typed&term_meta[]=logo%7Ctyped&term_meta[]=lion%7Ctyped"
images = ph.runme(url, threshold=10)
images = list(map(lambda img: img.decode(), images))
print('Downloading {} from Pinterest'.format(len(images)))
s.download(images, mydir=res_dir)
