def scrap(site):
    import bs4 as bs  # library de scrapping
    import urllib.request

    siteSplitted = site.split("/")  # on sépare le tring
    # on récupère le dernier de la liste correspondant à par exemple: Alpha-wann-soldat-tue-soldat-lyrics
    lyricsName = str(siteSplitted[len(siteSplitted)-1])
    vraiSite = "https://genius.com/amp/"+lyricsName  # on recrée la bonne url
    # pour éviter le rejet on se fait passer pour un navigateur lambda
    hdr = {'User-Agent': 'Mozilla/5.0'}
    # on prépare une requete http
    req = urllib.request.Request(vraiSite, headers=hdr)
    saucel = urllib.request.urlopen(req)  # on la fait
    soupl = bs.BeautifulSoup(saucel, 'html')    # on scrappe!

    tmp = soupl.find('div', "lyrics")  # on récupère le div lyrics
    # on écrit dans le fichier les paroles
    lyrics = open('temp/lyrics.txt', 'w+', encoding='utf-8')
    lyrics.write(tmp.text)
    lyrics.close()
    return tmp.text


if __name__ == '__main__':
    scrap("https://genius.com/Alpha-wann-soldat-tue-soldat-lyrics")
