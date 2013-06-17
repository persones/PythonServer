# -*- coding: utf-8 -*-
"""
Created on Sun Jun 09 22:50:42 2013

@author: Person
"""

import os

class FileReg:
    def __init__(self, inPath, inName, inParent = None):
        self.path = inPath + '/'
        self.name = inName
        self.size = 0
        self.childrenList = []
        self.parent = inParent
        self.crawl()
    
    def crawl(self):
        if os.path.isdir(self.path + self.name):
            fileList = os.listdir(self.getFullName())
            for aFile in fileList:
                aFileReg = FileReg(self.getFullName(), aFile)
                aFileReg.parent = self
                self.childrenList.append(aFileReg)
                self.size = self.size + aFileReg.crawl()
        else:
            self.size = os.stat(self.getFullName()).st_size
        #print (self.getFullName(), self.size)
        return self.size
                
    def getFullName(self):    
        return self.path + self.name
    
    def getChild(self, name):
        if (self.children):
            for aChild in self.childrenList:
                if (aChild.name == name):
                    return aChild
        return None
        
    def getChildrenSizes(self):
        childrenArray = []
        for aChild in self.childrenList:
            childrenArray.append([aChild.name, aChild.size])
        return ({'path' : self.getFullName(), 'files' : childrenArray})
        
    
if __name__ == "__main__":
    f = FileReg('C:/Users/Person/Documents', 'eagle')
   
    print(f.getChildrenSizes())
    