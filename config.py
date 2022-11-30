KEY = ""

template_intro = """génère une introduction d'article de blog sans titres  pour le titre '{}' en Français de minimum 100 mots et maximum 200 mots.
        Ne pas ajouter de titres.
        Faire qu'un seul paragraphe.
        Finir la génération par un point."""
template_chapitres = "Génère plusieurs paragraphes d'article de blog pour le sous titre '{}' en Français de minimum 100 mots et maximum 400 mots. Ajoute une liste en html entre 2 paragraphes. Fini la génération après les point d'une phrase. Ne fais pas de titres."
template_conclusion = """génère une conclusion d'article de blog avec un titre h2 pour le titre '{}' en Français. Ajoute un titre de conclusion au début de la génération.
                    Finir la génération par un point.
                    """
mot_cles =[
# "quelle somme d'argent peut-on donner sans déclarer ?",
# "comment mettre de l'argent sur Paypal avec ou sans carte bancaire ?",
# "comment investir son argent quand on est jeune ?",
# "PME : pensez à centralisez vos données d'entreprise",
# "quels sont les effets de la fleur de CBD sur la santé",
# "Devenir Sauveteur Secouriste du Travail : nos 3 conseils d'experts",
# "terre de diatomée punaise de lit comment utiliser",
# "comment vider un ballon d'eau chaude de 200/300 litres",
# "comment aménager le tour d'une piscine hors sol",
# "différence entre vitrocéramique et induction",
# "quand planter des fraisiers en jardinière",
# "comment aménager un balcon de 5m2",
# "comment peindre un meuble en bois avec effet vieilli",
# "de quelle couleur peindre les portes d'un couloir blanc",
# "dalle PVC adhésive sur carrelage salle de bain",
# "idée d'aménagement et rangement d'un garage Elevée",
# "abcès dentaire sous couronne traitement naturel",
# "comment soigner une tendinite au coude remède de grand-mère",
# "dent définitive qui pousse derrière dent de lait que faire",
# "comment éliminer la cortisone dans le corps naturellement",
# "comment soulager un mal de dos rapidement naturellement",
# "gâteau sans sucre pour diabétique",
# "comment savoir si on est diabétique avec prise de sang",
# "quand apparaissent les premiers signes de grossesse sous pilule",
"comment perdre la graisse du ventre en 1 mois",
# "remèdes naturels contre les démangeaisons du cuir chevelu",
# "enceinte courbe température grossesse",
# "mal au téton quand j'appuie"
]

model = "text-davinci-002"

suggestions_google = False
