import scraplyrics
import json
import boyermoore


def openData(jsonFilePath):
    file = open(str(jsonFilePath), "r")
    data = json.load(file)
    return data


def main():
    url = input("Quel est le lien Genius: ")
    text = scraplyrics.scrap(url)
    lexicalFieldData = openData("champLexicaux.json")
    print(lexicalFieldData)


if __name__ == '__main__':
    main()
