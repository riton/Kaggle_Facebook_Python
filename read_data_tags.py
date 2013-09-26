import numpy
import csv
import nltk

from numpy import genfromtxt
import pandas as pd1
nr1 = 10
#nr2 = 5000
nr2 =  2013337 - 3*nr1

t = pd1.read_csv('Train.csv',usecols=['Tags']) #read 10 rows
#print t.Tags
print "here", len(t.Tags)

t2 = pd1.read_csv('Test.csv',nrows=nr1)
#print t2
cnt = 0
key_list = ['c++','Java','Javascript','Ruby','Mozilla','Firefox','CMS','Perl','android',
            'Python','Scala','Visual Studio 2010','VMWare','cocos2d-x','ASP.Net','div',
            'PHP','JSON','linux','c#','VPN','ASP','jquery','Visual','yardoc','matlab',
            'database','django','Windows','Mac','CSS','db2','SQL','8086','Android','CPU',
            'iphone','ios','API','html','XSD','VM','jqueryUI','C#','JVM','bash','App',
            'exception','iterator','DI','TSV','file','javascript','stream','standard',
            'enumerate','ASP.NET','MVC','Vault','WordPress','version','release','Stack',
            'python','x86','Server','array','XML','grammar','function','EC2','search',
            'database?','nginx','iOS','MySQL','YQL','Websphere','SOLR','Flash','LINQ',
            'jQuery','java','3D','graph','Pop-up','recursive','Log4j','OpenGL','visio',
            'Framework','modem','posix','SharePoint','Routers','memory','Spring','date',
            'Drupal','script','shell','Apache','VB','git','WPF','SOAP','Excel','Tree',
            'rails','Intel','Linux','Eclipse','CentOS','Matrices','HTML','Ubuntu','Awk',
            'Json','iPhone','Algorithm']

ofile= open('Tags.csv', 'wb')
writer = csv.writer(ofile, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONE)
writer.writerow(["Tag","Count"])
tags = {}

for i in range(len(t.Tags)):
    list1 = t.Tags[i].split()
    for tag in list1:
        if tag in tags:
            tags[tag] = tags[tag]+1
            #print tag, i
        else:
            tags[tag]=1
    
print "done1"
s_tags = sorted(tags,key=tags.get, reverse=True)
for tag in s_tags:
    writer.writerow([tag,tags[tag]])

ofile.close() 
print "done writing csv"

 
