def table_sauts(cle) :
    """la fonction renvoie la table de décalage en utilisant la formule :
    pour toute lettre de cle : decalage = longueur de cle - index de la lettre -1
    sauf dernière lettre et toutes les autres : decalage = longueur de cle
    precondition :
        cle : string
    postcondition :
        dict
    """
    d = {}
    for i in range(len(cle)-1) :
        d[cle[i]] = len(cle)-i-1
    for lettre in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' :
        if lettre not in d.keys() :
            d[lettre] = len(cle)
    return d
def boyer_moore (texte, cle):
    texte = texte.upper()
    cle = cle.upper()
    long_txt = len(texte)
    long_cle = len(cle)
    positions = [] #liste des positions où l'on trouve le motif
    if long_cle <= long_txt :
        decalage = table_sauts(cle) #on charge la table des décalages
    i=0
    trouve = False
    while (i <= long_txt-long_cle):
        for j in range (long_cle -1, -1, -1): #On part du dernier indice de la cle jusque 0 en décalant de -1 à chaque fois
            trouve = True
            if texte[i+j] != cle[j] : # Si on tombe sur une lettre différentes de celle de la clé
                if (texte[i+j] in decalage and decalage[texte[i+j]]<=j):
                    i+=decalage[texte[i+j]] # on décale dans le texte en utilisant la table de décalage
                else :
                    i+=j+1 # si la lettre n'est pas dans la table de décalage alors on décale du nombre de lettres restantes à explorer sur la clé
                trouve = False
                break #on sort de la boucle for car on a trouvé une lettre qui ne convient pas
        if trouve : #si toutes les lettres convenait donc on a trouvé une occurence de la clé dans texte
            positions.append(i) #on ajoute à la liste des positions où l'on trouve la clé dans le texte
            i=i+1
            trouve = False #on remet trouvé à False car on cherche la prochaine occurence
    return positions

if __name__=='__main__':
    print(table_sauts('TARTEMPION'))
    print(boyer_moore('bonjour Mr tartempion, comment va mr tartempion ?','tartempion'))