import scraplyrics
import json
import boyermoore
import matplotlib.pyplot as plt


def openData(jsonFilePath):
    file = open(str(jsonFilePath), "r")
    data = json.load(file)
    return data


def main(url=None, printout=True):
    counter = {}
    text = scraplyrics.scrap(url)
    lexicalFieldData = openData("champLexicaux.json")
    totalWordsFound = 0
    for champ in lexicalFieldData.keys():
        counter[champ] = 0
        for mot in lexicalFieldData[champ]:
            returnList = boyermoore.boyer_moore(text, mot)
            counter[champ] += len(returnList)
            totalWordsFound += len(returnList)
    if printout == True:
        altCounter = counter.copy()
        print("Voici les thèmes trouvés:")
        for champ in counter.keys():
            if counter[champ] != 0:
                print(str(champ)+" : " +
                    str(round(counter[champ]/totalWordsFound*100))+" %")
            else:
                del altCounter[champ]
        plt.barh(range(len(altCounter)), list(altCounter.values()), align='center')
        plt.yticks(range(len(altCounter)), list(altCounter.keys()))
        plt.show()
    return altCounter


if __name__ == '__main__':
    def retrieveValueAndQuit():
        global url
        url = e1.get()
        master.quit()

    import tkinter as tk
    url = ""
    master = tk.Tk()
    tk.Label(master, text="URL du lien Genius").grid(row=0)
    e1 = tk.Entry(master)
    e1.grid(row=0, column=1)
    tk.Button(master,
              text='OK',
              command=retrieveValueAndQuit).grid(row=1, column=0)
    master.mainloop()
    main(url,True)
