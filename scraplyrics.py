def scrap(site):
    import bs4 as bs
    import urllib.request

    siteSplitted = site.split("/")
    lyricsName=str(siteSplitted[len(siteSplitted)-1])
    vraiSite= "https://genius.com/amp/"+lyricsName
    print(lyricsName)
    print(vraiSite)
    hdr = {'User-Agent': 'Mozilla/5.0'}
    req = urllib.request.Request(vraiSite,headers=hdr)
    saucel=urllib.request.urlopen(req)
    soupl = bs.BeautifulSoup(saucel, 'html')


    tmp = soupl.find('div', "lyrics")
    lyrics = open('temp/lyrics.txt', 'w+', encoding='utf-8')
    lyrics.write(tmp.text)
    lyrics.close()
    return tmp.text

if __name__ == '__main__':
    scrap("https://genius.com/Alpha-wann-soldat-tue-soldat-lyrics")