import pandas as pd
import matplotlib.pyplot as plt

# Charger les données
ventes = pd.read_csv("ventes.csv")
ventes["Date"] = pd.to_datetime(ventes["Date"])

# Afficher les premières lignes
print(ventes.head())
# Afficher les informations générales du tableau
print(ventes.info())

# Afficher les statistiques principales
print(ventes.describe())
# Calculer le chiffre d'affaires
ventes["Chiffre_Affaires"] = ventes["Quantite"] * ventes["Prix"]
# Extraire le mois
ventes["Mois"] = ventes["Date"].dt.month

print("\nDonnées avec le mois :")
print(ventes[["Date", "Mois", "Chiffre_Affaires"]])

# Afficher les ventes avec le chiffre d'affaires
print(ventes)
# Calculer le chiffre d'affaires total
chiffre_affaires_total = ventes["Chiffre_Affaires"].sum()

print("Chiffre d'affaires total :", chiffre_affaires_total)
# Chiffre d'affaires par produit
ca_par_produit = ventes.groupby("Produit")["Chiffre_Affaires"].sum()

print("\nChiffre d'affaires par produit :")
print(ca_par_produit)
# Graphique du chiffre d'affaires par produit
ca_par_produit.plot(kind="bar")

plt.title("Chiffre d'affaires par produit")
plt.xlabel("Produit")
plt.ylabel("Chiffre d'affaires")
plt.xticks(rotation=45)
plt.tight_layout()

# Quantité totale vendue par produit
quantite_par_produit = ventes.groupby("Produit")["Quantite"].sum()

print("\nQuantité vendue par produit :")
print(quantite_par_produit)
plt.show()
# Graphique des quantités vendues
quantite_par_produit.plot(kind="bar")

plt.title("Quantité vendue par produit")
plt.xlabel("Produit")
plt.ylabel("Quantité vendue")
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()
# Chiffre d'affaires par ville
ca_par_ville = ventes.groupby("Ville")["Chiffre_Affaires"].sum()

print("\nChiffre d'affaires par ville :")
print(ca_par_ville)
plt.show()
# Graphique du chiffre d'affaires par ville
ca_par_ville.plot(kind="bar")

plt.title("Chiffre d'affaires par ville")
plt.xlabel("Ville")
plt.ylabel("Chiffre d'affaires")
plt.xticks(rotation=0)
plt.tight_layout()

plt.show()
# Chiffre d'affaires par mois
ca_par_mois = ventes.groupby("Mois")["Chiffre_Affaires"].sum()

print("\nChiffre d'affaires par mois :")
print(ca_par_mois)
# Évolution du chiffre d'affaires par mois
ca_par_mois.plot(kind="line", marker="o")

plt.title("Évolution du chiffre d'affaires par mois")
plt.xlabel("Mois")
plt.ylabel("Chiffre d'affaires")
plt.xticks([1, 2, 3])
plt.grid(True)
plt.tight_layout()

plt.show()
ca_produit = ventes.groupby("Produit")["Chiffre_Affaires"].sum().sort_values(ascending=False)

ca_produit
plt.figure(figsize=(8,5))

ca_produit.plot(kind="bar")

plt.title("Chiffre d'affaires par produit")
plt.xlabel("Produit")
plt.ylabel("Chiffre d'affaires")
plt.xticks(rotation=0)

plt.show()
quantite_produit = ventes.groupby("Produit")["Quantite"].sum().sort_values(ascending=False)

print(quantite_produit)
# Résumé de l'analyse

print("\n===== RÉSUMÉ DE L'ANALYSE =====")

print("Chiffre d'affaires total :", ventes["Chiffre_Affaires"].sum())

print("Produit générant le plus de CA :",
      ca_par_produit.idxmax(),
      "avec", ca_par_produit.max())

print("Ville générant le plus de CA :",
      ca_par_ville.idxmax(),
      "avec", ca_par_ville.max())

print("Mois avec le plus de CA :",
      ca_par_mois.idxmax(),
      "avec", ca_par_mois.max())