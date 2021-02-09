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
        plt.barh(range(len(altCounter)), list(
            altCounter.values()), align='center')
        plt.yticks(range(len(altCounter)), list(altCounter.keys()))
        plt.show()
    return altCounter


if __name__ == '__main__':
    import tkinter as tk
    from kivy.app import App
    from kivy.uix.label import Label
    from kivy.uix.button import Button
    from kivy.uix.textinput import TextInput
    from kivy.uix.boxlayout import BoxLayout

    class UIApp(App):
        def build(self):
            self.title = 'Analyzer'
            b = BoxLayout(orientation='vertical', padding=10)
            l = Label(text="Lyrics analyser",
                      font_size=50, bold=True)
            b1 = BoxLayout(padding=40)

            l1 = Label(text="URL de la page Genius : ", font_size=20)
            i1 = TextInput(font_size=20, height=50, padding=10, background_color=(
                0.2, 0.2, 0.2, 1), foreground_color=(1, 1, 1, 1))
            b1.add_widget(l1)
            b1.add_widget(i1)

            b.add_widget(l)
            b.add_widget(b1)

            okButton = Button(text="Start")
            b.add_widget(okButton)

            returnZone = TextInput(text="", font_size=20, padding=20, background_color=(
                0.2, 0.2, 0.2, 1), foreground_color=(1, 1, 1, 1))
            b.add_widget(returnZone)

            def startMainProgram(instance):
                url = i1.text
                returnZone.text = str(main(url, True))
            okButton.bind(on_release=startMainProgram)

            return b
    UIApp().run()
