import json
import csv
  
metiers_dict = {}

# Lecture des données métiers
with open('input/metiers.csv', 'r', encoding='utf-8') as csvfile:
  data = csv.reader(csvfile, delimiter=',', quotechar='"')
  next(data)
  # Enregistrement des données métiers
  for row in data:
    metiers_dict[row[0]] = {
      "libelle": row[1],
      "domaine" : { "code" : row[2], "libelle" : row[3] },
      "domaine_pro" : { "code" : row[4], "libelle" : row[5] },
      "competences" : [],
      "exemples" : []
      }

# Lecture et enregistrement des données d'exemples métiers
with open('input/metiers_exemple.csv', 'r', encoding='utf-8') as csvfile:
  data = csv.reader(csvfile, delimiter=',', quotechar='"')
  next(data)
  for row in data: metiers_dict[row[3]]["exemples"] += [row[1]]

# Lecture et enregistrement des données de correspondances entre métiers et compétences
with open('input/correspondances.csv', 'r', encoding='utf-8') as csvfile:
  data = csv.reader(csvfile, delimiter=',', quotechar='"')
  next(data)
  for row in data: metiers_dict[row[0]]["competences"] += [row[1]]

# Chargement des données de mes compétences
with open('input/mescompetences.json', 'r', encoding='utf-8') as f:
  mescompetences_data = json.load(f)

# Création des données de mescompétences
mescompetence = [str(mescompetence["code_ogr"]) for mescompetence in mescompetences_data["mescompetences"]]

competences = {}

# Lecture des données métiers
with open('input/competences.csv', 'r', encoding='utf-8') as csvfile:
  data = csv.reader(csvfile, delimiter=',', quotechar='"')
  next(data)
  # Enregistrement des données métiers
  for row in data:
    if not row[0] in competences:
      competences[row[0]] = row[1]

# Regarde pour chaque metier si tu es compatible
for metier in metiers_dict:
  n = len(metiers_dict[metier]["competences"])
  score = 0

  metiers_dict[metier]["competencesManquantes"] = []

  for competence in metiers_dict[metier]["competences"]:
    if competence in mescompetence:
      score += 1
    else:
      if competence in competences:
        metiers_dict[metier]["competencesManquantes"] += [competences[competence]]
      else:
        metiers_dict[metier]["competencesManquantes"] += ["Compétence inconnue, code : " + str(competence)]

  metiers_dict[metier]["score"] = {
    "resultat": score/n,
    "score": score,
    "surcombien": n
    }

# Transformation de données et trie
code_rom_trie = sorted(metiers_dict, key=lambda metier: (-metiers_dict[metier]["score"]["score"], -metiers_dict[metier]["score"]["resultat"]))

# Affiche les résultat
for i in range(3):
  resultat = metiers_dict[code_rom_trie[i]]

  print("Résultat top ", i + 1)
  print("Code métier : ", code_rom_trie[i])
  print("Qui corressponds aux métiers :")
  for metier in resultat["exemples"]:
    print(" - ", metier)
  print("Ton score est de : ", '{:.1%}'.format(resultat["score"]["resultat"]), " soit ", resultat["score"]["score"], "/", resultat["score"]["surcombien"])
  print("Pour avoir un meilleur score tu devrais travailler sur les compétences :")
  for competence in resultat["competencesManquantes"]:
    print(" - ", competence)

# Jolie Affichage sous forme JSON
# print(json.dumps(metiers_dict, indent = 4, sort_keys=True, ensure_ascii=False))