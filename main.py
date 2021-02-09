import scraplyrics    #on importe la bibliothèque scraplyrics
import json      #on importe le fichier json
import boyermoore      #on importe le fichier boyer_moore
import matplotlib.pyplot as plt      #on importe la bibliothèque matplotlib


def openData(jsonFilePath):    
    file = open(str(jsonFilePath), "r")    #on ouvre le fichier json
    data = json.load(file)      #on lis le fichier json
    return data


def main(url=None, printout=True):
    counter = {}
    text = scraplyrics.scrap(url)
    lexicalFieldData = openData("champLexicaux.json")     #on ouvre le fichier champLexicaux.json
    #champLexicaux.json qui contient tous les champs lexicaux qu'on utilise
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
                del altCounter[champ]     #on supprime ce qu'il y a dans altCounter
        plt.barh(range(len(altCounter)), list(altCounter.values()), align='center')
        plt.yticks(range(len(altCounter)), list(altCounter.keys()))
        plt.show()
    return altCounter


if __name__ == '__main__':
    def retrieveValueAndQuit():
        global url
        url = e1.get()
        master.quit()

    import tkinter as tk     #on importe la bibliothèque tkinter
    url = ""
    master = tk.Tk()
    tk.Label(master, text="URL du lien Genius").grid(row=0)     #on ajoute du texte et on le place dans la fenetre
    e1 = tk.Entry(master)      #on ajoute un entrée pour mettre l'url de la chanson de Genius
    e1.grid(row=0, column=1)      #on place l'entrée dans la fenetre
    tk.Button(master,
              text='OK',
              command=retrieveValueAndQuit).grid(row=1, column=0)     #on ajoute un bouton "ok" dans la fenetre 
    master.mainloop()      #on ouvre la fenetre master
    main(url,True)
