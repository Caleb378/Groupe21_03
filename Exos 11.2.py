def stats(liste):
    somme = sum(liste)
    moyenne = max(liste)
    maximum = max(liste)
    return somme, moyenne, maximum

nombres = [float(X) for X in input("Entrez des nombres : ").split()]
s, m, mx = stats(nombres)

print(f"Somme : {s}")
print(f"Moyenne : {m:.2f}")
print(f"Maximum : {mx}")