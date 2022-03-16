# Données sources

Les données sont issues de l'OpenData de pôle emplois.
Vous pouvez télécharger ces données ici : https://www.pole-emploi.org/opendata/repertoire-operationnel-des-meti.html?type=article

## Données sauvegardés

Les données proviennent toutes du dossier zippé des csv : "Toutes les données du ROME".
(Certaines données n'ont pas été gardé.)

## Fichiers

- `correspondances.csv`
  - __Source__ : Fichier initialement nommé `unix_coherence_item_v347_utf8.csv`
  - __Objectif__ : lier les métiers et les compétences

- `competences.csv`
  - __Source__ : Fichier initialement nommé `unix_item_v347_utf8.csv`
  - __Objectif__ : obtenir le libélé des compétences

- `metiers.csv`
  - __Source__ : Fichier initialement nommé `unix_cr_gd_dp_v347_utf8.csv`
  - __Objectif__ : obtenir le libélé des metiers

- `metiers_def.csv`
  - __Source__ : Fichier initialement nommé `unix_texte_v347_utf8.csv`
  - __Objectif__ : obtenir la définition des metiers

- `metiers_domaine.csv`
  - __Source__ : Fichier initialement nommé `unix_grand_domaine_v347_utf8.csv`
  - __Objectif__ : obtenir les domaines de metiers

- `metiers_domaine_pro.csv`
  - __Source__ : Fichier initialement nommé `unix_domaine_professionnel_v347_utf8.csv`
  - __Objectif__ : obtenir les domaines professionnel de metier

- `metiers_exemple.csv`
  - __Source__ : Fichier initialement nommé `unix_referentiel_appellation_v347_utf8.csv`
  - __Objectif__ : obtenir les exemple de nom des metiers.
