#!/usr/bin/python
# -*- coding: utf8 -*-

"""
module euclide
"""
def pgcd(a,b):
  """Plus grand diviseur commun entre deux nombres"""
  #print('(%d,%d)' %(a,b))
  if not isinstance(a,(int,long)):
    raise TypeError('Les arguments doivent être etier ou long')
  if not isinstance(b,(int,long)):
    raise TypeError('Les arguments doivent être etier ou long')
  if a<0:# a négatif alors le rendre positif
    a=-a
  if b<0:# b négatif alors le rendre positif
    b=-b
  if (b==1) or (b==0):
    return 1
  if a%b==0:#a est multiple de b
    return b
  if a<b:
    return pgcd(b,a)
    return a
  return pgcd(a-b,b)
def ppcm(a,b):
  """Plus petit multiple commun entre deux nombres"""
  if a==b:
    return a
  return abs(a*b)/pgcd(a,b)