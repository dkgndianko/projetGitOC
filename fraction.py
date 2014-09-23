#!/usr/bin/python
# -*- coding: utf8 -*-

"""
module pour fraction réelle qui gère tous les opérateurs
"""
import euclide
class Fraction:
  """C'est cette classe qui gère tout"""
  def __init__(self,num,denom=1):
    if not isinstance(num,(int,long)):
      raise TypeError('Le numérateur doit être etier ou long')
    if not isinstance(denom,(int,long)):
      raise TypeError('Le dénominateur doit être etier ou long')
    self.__numerateur=num
    self.__denominateur=denom
    self.simplifier()
  @classmethod
  def create(cls,num,denom=1):
    f=Fraction(num,denom)
    return f
  def simplifier(self):
    p=euclide.pgcd(self.__numerateur,self.__denominateur)
    self.__numerateur/=p
    self.__denominateur/=p
  def __str__(self):
    return 'Fraction: '+str(self.__numerateur)+'/'+str(self.__denominateur)
  def __repr__(self):
    return str(self.__numerateur)+'/'+str(self.__denominateur)+'(='+str(self.decimalValue())+')'
  def decimalValue(self):
    try:
      p=float(self.__numerateur)/float(self.__denominateur)
    except:
      print('Une erreur est survenue dans le calcul (exemple de dénominateur nul)')
      p=0
    finally:
      return p
  def __lt__(self,other):
    return self.decimalValue() < other.decimalValue()
  def __gt__(self,other):
    return self.decimalValue() > other.decimalValue()
  def __le__(self,other):
    return self.decimalValue() <= other.decimalValue()
  def __ge__(self,other):
    return self.decimalValue() >= other.decimalValue()
  def __eq__(self,other):
    return self.decimalValue() == other.decimalValue()
  def __ne__(self,other):
    return self.decimalValue() != other.decimalValue()
  def __cmp__(self,other):
    if self < other:
      return -1
    elif self > other:
      return 1
    return 0
  def __neg__(self):
    return Fraction(-self.__numerateur,self.__denominateur)
  def __abs__(self):
    return Fraction(abs(self.__numerateur),abs(self.__denominateur))
  def __add__(self,other):
    if self.__denominateur==other.__denominateur:
      f= Fraction(self.__numerateur+other.__numerateur,self.__denominateur)
    else:
      f=Fraction(self.__numerateur*other.__denominateur+other.__numerateur*self.__denominateur,self.__denominateur*other.__denominateur)
    return f
  def __iadd__(self, other):
    return self.__add__(other)

  def __sub__(self,other):
    return self+(-other)
  def __mul__(self,other):
    return Fraction(self.__numerateur*other.__numerateur,self.__denominateur*other.__denominateur)
  def __div__(self,other):
    return Fraction(self.__numerateur*other.__denominateur,self.__denominateur*other.__numerateur)