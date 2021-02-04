import bs4 as bs
import urllib.request


hdr = {'User-Agent': 'Mozilla/5.0'}
site= "https://genius.com/amp/Damso-feu-de-bois-lyrics"
req = urllib.request.Request(site,headers=hdr)
saucel=urllib.request.urlopen(req)
soupl = bs.BeautifulSoup(saucel, 'html')


tmp = soupl.find('div', "lyrics")
lyrics = open('lyrics.txt','w')
lyrics.write(tmp.text)
lyrics.close()