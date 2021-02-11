import scraplyrics  # on importe la bibliothèque scraplyrics
import json  # on importe le fichier json
import boyermoore  # on importe le fichier boyer_moore
import matplotlib.pyplot as plt  # on importe la bibliothèque matplotlib


def openData(jsonFilePath):
    file = open(str(jsonFilePath), "r")  # on ouvre le fichier json
    data = json.load(file)  # on lis le fichier json
    return data


def main(url=None, printout=True):
    counter = {}
    text = scraplyrics.scrap(url)
    # on ouvre le fichier champLexicaux.json
    lexicalFieldData = openData("champLexicaux.json")
    # champLexicaux.json qui contient tous les champs lexicaux qu'on utilise
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
                # on supprime ce qu'il y a dans altCounter
                del altCounter[champ]
        plt.barh(range(len(altCounter)), list(
            altCounter.values()), align='center')
        plt.yticks(range(len(altCounter)), list(altCounter.keys()))
        plt.show()
    return altCounter


if __name__ == '__main__':
    from kivy.app import App    # On importe kivy et ses modules spécifique aux programmes
    from kivy.uix.label import Label
    from kivy.uix.button import Button
    from kivy.uix.textinput import TextInput
    from kivy.uix.boxlayout import BoxLayout
    from kivy.core.window import Window

    class UIApp(App):  # Classe qui régit l'application
        def build(self):  # Méthode de construction de la fenêtre
            self.title = 'Analyzer'  # titre de la fenêtre
            Window.clearcolor = (0.3, 0.3, 0.3, 1)  # couleur de fond
            # layout haut en bas
            b = BoxLayout(orientation='vertical', padding=10)
            l = Label(text="Lyrics analyser",
                      font_size=50, bold=True)  # titre
            # box horizontale pour l'input et son label
            b1 = BoxLayout(padding=40)

            l1 = Label(text="URL de la page Genius : ",
                       font_size=20)  # Label pour l'input
            i1 = TextInput(font_size=20, height=50, padding=10, background_color=(
                0.2, 0.2, 0.2, 1), foreground_color=(1, 1, 1, 1))  # l'input en question pour l'URL
            b1.add_widget(l1)  # on ajoute à la box horizontale
            b1.add_widget(i1)  # idem

            b.add_widget(l)  # on ajoute le titre à la main box
            b.add_widget(b1)  # on ajoute la box horizontale à la main box

            # bouton pour lancer (on lui met la fonction plus tard)
            okButton = Button(text="Start")
            b.add_widget(okButton)

            returnZone = TextInput(text="", font_size=20, padding=20, background_color=(
                0.2, 0.2, 0.2, 1), foreground_color=(1, 1, 1, 1))   # zone dans laquelle on va mettre le return de main()
            b.add_widget(returnZone)

            # on doit définir la fonction dans le build() sinon ça ne marche pas
            def startMainProgram(instance):
                url = i1.text  # on récupère l'URL entrée
                if url == "" or "/" not in url:
                    returnZone.text = "URL Invalide"
                else:
                    returnZone.text = str(main(url, True))
            # on ajoute la fonction au bouton
            okButton.bind(on_release=startMainProgram)
            return b  # on return la box principale comme racine du programme

    UIApp().run()
