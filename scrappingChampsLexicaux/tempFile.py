String="Agonie, disparition, extinction, décès, trépas, tombeau, disparu, victime, dépouille, défunt, tombe, sépulture, meurtre, homicide, suicide, mausolée, caveau, tué, décédé, trépassé, martyre, cadavre, feu, crypte, cénotaphe, cercueil, bière, linceul, suaire"
listString=String.split(",")
result=open("scrappingChampsLexicaux/tempText.txt","w")
result.write(str(listString))
result.close()