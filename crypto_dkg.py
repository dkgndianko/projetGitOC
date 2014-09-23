#!/usr/bin/python
# -*- coding: utf8 -*-
from string import maketrans
from string import printable
MAPPING=["éèêëçàöô","eeeecaoo"]# POUUR DES RAISONS DE TRANSFORMATION
MYPRINTABLE=printable+MAPPING[0] #C'est pour la plage de lettres à utiliser
def reordonner_alphabet(phrase):
  """Réordonner l'alphabet en utilisant la phrase comme mot clé"""
  longueur=len(phrase)
  resultat=""
  alphabet=map(None,MYPRINTABLE)
  for i in range(longueur):
    if resultat.find(phrase[i])==-1: # la lettere n'est pas encore dans le résultat
      resultat+=phrase[i] # on l'ajoute
      alphabet.remove(phrase[i])
  resultat+=''.join(alphabet)
  return resultat
def normaliser(texte):
  """Elle permet de normaliser un texte en prenant en compte les caractère qu'il faut transformer"""
  myTans=maketrans(MAPPING[0],MAPPING[1])
  return texte.translate(myTans)
def encoder_vigenere(texte,cle):
  TRANS=maketrans(MYPRINTABLE,reordonner_alphabet(cle))
  return texte.lower().translate(TRANS)
def decoder_vigenere(texte,cle):
  TRANS=maketrans(reordonner_alphabet(cle),MYPRINTABLE)
  return texte.translate(TRANS)
