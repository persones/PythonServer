# -*- coding: utf-8 -*-
"""
Created on Fri Jun 07 01:19:34 2013

@author: Person
"""

from flask import Flask, request, g
import json
from CrawlPath import FileReg

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def query():
    print 'query:'
    if request.method == 'GET':
        print 'GET'
        inPath = request.args['path']
        print 'inPath : ' + inPath
        if inPath == 'root':
            print 'path is root'
            print g.crawler.getFullName()
            print 'no?'
            g.crawler = g.crawler.getChild(inPath)
            print 'crawler: '
        
        print 'crawler: ' + g.crawler
        #c = json.dumps({'path' : inPath, 'files' : [['one', 1], ['two', 2], ['three', 3]]} , sort_keys=True)
        c = json.dumps(g.crawler.getChildrenSizes() , sort_keys=True)
        #print c
        return c
    else:
        print 'error'
    

@app.route("/welcome")
def welcome():
    print 'welcome'
    g.crawler = FileReg('C:/Users/Person/Documents', 'eagle')
    print "crawler: " + g.crawler.getFullName()
    txt = open('C:/Users/Person/dropbox/client.html');
    return txt.read()    
    
if __name__ == "__main__":
    app.run()