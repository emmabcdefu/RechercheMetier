import json
  
# chargement des données métiers
with open("input/metiers.json", 'r', encoding='utf-8') as f:
  metiers_data = json.load(f)

dict_metiers = {}

# Transformation des données métiers
for metier in metiers_data["metiers"]:
  code_rom = metier["code_rom"]
  if code_rom in dict_metiers:
    dict_metiers[code_rom]["metiers"] += [metier["label"]]
  else:
    dict_metiers[code_rom] = { "metiers": [metier["label"]]}

# Chargement des données de correspondances entre métiers et compétences
with open('input/correspondances.json', 'r', encoding='utf-8') as f:
  correspondances_data = json.load(f)

# Ajout des données de compétences
for correspondance in correspondances_data["correspondances"]:
  code_rom = correspondance["code_rom"]
  if "competences" in dict_metiers[code_rom]:
    dict_metiers[code_rom]["competences"] += [correspondance["code_ogr"]]
  else:
    dict_metiers[code_rom]["competences"] = [correspondance["code_ogr"]]

# Chargement des données de mes compétences
with open('input/mescompetences.json', 'r', encoding='utf-8') as f:
  mescompetences_data = json.load(f)

# Création des données de mescompétences
mescompetence = [mescompetence["code_ogr"] for mescompetence in mescompetences_data["mescompetences"]]

# Chargement des données de compétences
with open('input/competences.json', 'r', encoding='utf-8') as f:
  competence_data = json.load(f)

# Transformations des données compétences
competences = {}
for competence in competence_data["competences"]:
  competences[competence["code_ogr"]] = competence["libelle"]

# Regarde pour chaque metier si tu es compatible
for metier in dict_metiers:
  n = len(dict_metiers[metier]["competences"])
  score = 0

  dict_metiers[metier]["competencesManquantes"] = []

  for competence in dict_metiers[metier]["competences"]:
    if competence in mescompetence:
      score += 1
    else:
      if competence in competences:
        dict_metiers[metier]["competencesManquantes"] += [competences[competence]]
      else:
        dict_metiers[metier]["competencesManquantes"] += ["Compétence inconnue, code : " + str(competence)]

  dict_metiers[metier]["score"] = {
    "resultat": score/n,
    "score": score,
    "surcombien": n
    }

# Transformation de données et trie
code_rom_trie = sorted(dict_metiers, key=lambda metier: (-dict_metiers[metier]["score"]["resultat"], -dict_metiers[metier]["score"]["score"]))

# Affiche les résultat
for i in range(10):
  resultat = dict_metiers[code_rom_trie[i]]

  print("Résultat top ", i + 1)
  print("Code métier : ", code_rom_trie[i])
  print("Qui corressponds aux métiers :")
  for metier in resultat["metiers"]:
    print(" - ", metier)
  print("Ton score est de : ", '{:.1%}'.format(resultat["score"]["resultat"]), " soit ", resultat["score"]["score"], "/", resultat["score"]["surcombien"])
  print("Pour avoir un meilleur score tu devrais travailler sur les compétences :")
  for competence in resultat["competencesManquantes"]:
    print(" - ", competence)

# Jolie Affichage sous forme JSON
# print(json.dumps(dict_metiers, indent = 4, sort_keys=True, ensure_ascii=False))
