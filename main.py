import scraplyrics
import json
import boyermoore


def openData(jsonFilePath):
    file = open(str(jsonFilePath), "r")
    data = json.load(file)
    return data


def main():
    counter = {}
    url = input("Quel est le lien Genius: ")
    text = scraplyrics.scrap(url)
    lexicalFieldData = openData("champLexicaux.json")
    totalWordsFound = 0
    for champ in lexicalFieldData.keys():
        counter[champ] = 0
        for mot in lexicalFieldData[champ]:
            returnList = boyermoore.boyer_moore(text,mot)
            counter[champ] += len(returnList)
            totalWordsFound += len(returnList)
    print(counter)
    print("Voici les thèmes trouvés:")
    for champ in counter.keys():
        if counter[champ]!=0:
            print(str(champ)+" : "+str(round(counter[champ]/totalWordsFound*100))+" %")
    

            


if __name__ == '__main__':
    main()
