

pizza_nom = ("4 fromages", "Calzone", "Hawai")
pizza_prix = (10.5, 11, 8)
noms_et_prix = list(zip(pizza_nom, pizza_prix))

# for (nom, prix) in zip(pizza_nom, pizza_prix):
#     print(f"{nom} - {prix}€")

unzipped = list(zip(*noms_et_prix))
# print(unzipped)
pn, pp = list(zip(*noms_et_prix))
print(pn, pp)
print(pn)
print(pp)
