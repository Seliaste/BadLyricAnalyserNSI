Site="https://sites.google.com/site/francaislycee/langue/champslexicaux/mort"
hdr = {'User-Agent': 'Mozilla/5.0'}
req = urllib.request.Request(Site,headers=hdr)
saucel=urllib.request.urlopen(req)
soupl = bs.BeautifulSoup(saucel, 'html')


tmp = soupl.find('div', "lyrics")
lyrics = open('temp/lyrics.txt','w')
lyrics.write(tmp.text)
lyrics.close()
