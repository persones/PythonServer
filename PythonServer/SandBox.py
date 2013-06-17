# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 17:24:57 2013

@author: Person
"""

class obj():
    myName = 'Eyal'
    def getName(self):
        return "I am " + self.myName
        


if __name__ == "__main__":
    a = obj()
    print (a.myName)
    print (a.getName())