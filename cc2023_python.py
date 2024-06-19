
#==========================================================
#=================    Exercice 1     ======================
#==========================================================

'''
import random


def exercice1():
    L = []
    sept = False
    while sept == False:
        n = random.randint(1,10)
        if n == 7 :
            sept = True
        else :
            L.append(n)
    return L  

liste = exercice1()
print(liste)

somme = 0
nb = 0
for i in liste:
    somme += i
    nb += 1
print(somme/nb)


min = liste[0]
for i in liste:
    if i <= min:
         min = i
print(min)


max = liste[0]
for i in liste:
    if i >= max:
         max = i
print(max)


n = 0
for i in liste:
    if i > 7:
         n += 1
print(n)

'''



#==========================================================
#=================    Exercice 2     ======================
#==========================================================

'''

def exercice2(texte):
    d = {}
    for lettre in texte :
        if lettre in "aeiouy":
            d[lettre] = d.setdefault(lettre,0) +1
    
    max_occ = 0
    max_lettre = ''
    for lettre, occ in d.items():
        if d[lettre] >= max_occ:
            max_occ = d[lettre]
            max_lettre = lettre

    return max_lettre

print(exercice2("aaaaaaaaaaaaaaaeeeeeeeiiiouyyyyyy"))

'''




#==========================================================
#=================    Exercice 3     ======================
#==========================================================

'''
def remplacer(c1, c2, s):
    new_s = ""
    for lettre in s :
        if lettre == c1:
            new_s += c2
        else:
            new_s += lettre

    return new_s

print("Donnez le caractère à remplacer")
c1 = input()
print("Donnez le nouveau caractère")
c2 = input()
print("Donnez un texte :")
s = input()
r = remplacer(c1, c2, s)
print("Résultat : ",r)

'''





#==========================================================
#=================    Exercice 4     ======================
#==========================================================

'''
def nb_phrase(fichier_txt):
    with open('help.txt', 'r') as f:
        txt = f.read()
    nb_phrase = 0
    for i in range (len(txt)) :
        if (txt[i] == '.' or txt[i] == '?' or txt[i] == '!') and txt[i+1] != '.' and txt[i+2] != '.' :
            nb_phrase += 1
    return nb_phrase



print("Nom du fichier à lire : ")
fichier_txt = input()
print(nb_phrase(fichier_txt))

'''




#==========================================================
#=================    Exercice Bonus     ==================
#==========================================================