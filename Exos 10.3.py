phrase = input("Entrez une phrase : ")
mots = phrase.split()

un_sur_deux = mots[::2]

print(f"mots un sur deux : {un_sur_deux}")
