#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Renommage.py
#  

import os
import re
import csv
import logging, logging.config

# Main

logging.config.fileConfig('F:\\Code\\config.ini')
malog = logging.getLogger(__name__)

with open('param.csv', 'r') as csvfile:
  fic_param = csv.DictReader(csvfile, delimiter=';')
  for row in fic_param:
    rep=row["Répertoire"]
    regex=re.compile(row["Regex"])
    nom=row["Nom"]
    Deja_renomme=False
    fic_list=os.listdir(rep) # Récupère les noms de fichiers d'un répertoire
    nb_fic_traite=0

    for fic in fic_list:
      decoupe=regex.match(fic)
      if decoupe is not None:
        nom_episode=decoupe.group(3)
        extension=decoupe.group(4)
        decoupe_int1=int(decoupe.group(1))
        if decoupe_int1 < 10:
          saison="S0"+str(decoupe_int1)
        else:
          saison="S"+decoupe.group(1)

        decoupe_int2=int(decoupe.group(2))
        if decoupe_int2 < 10:
          saison+="E0"+str(decoupe_int2)
        else:
          saison+="E"+str(decoupe_int2)
        
        fic_new_name=rep+"\\"+nom+" - "+saison+nom_episode+extension
        
        fic_old=rep+"\\"+fic
        os.rename(fic_old,fic_new_name)
        malog.info('\n%s renommé en\n%s',fic_old,fic_new_name)
        nb_fic_traite+=1

