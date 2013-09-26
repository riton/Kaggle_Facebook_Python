import numpy
import csv
import nltk

from nltk.tokenize import word_tokenize, sent_tokenize

from numpy import genfromtxt
import pandas as pd1
nr1 = 500000
#nr2 = 5000
nr2 =  2013337 - 3*nr1

t = pd1.read_csv('Train.csv',nrows=5) #read 10 rows
print t.Title[3],t.Body[3],t.Tags[3]

t2 = pd1.read_csv('Test.csv',nrows=2)
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

ofile= open('res.csv', 'wb')
writer = csv.writer(ofile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
writer.writerow(["Id","Tags"])

for i in range(1,nr1):
    out_list=[]
    list1 = t2.Title[i].split()
    print word_tokenize(t2.Body[i])
    list2 = [word_tokenize(t) for t in sent_tokenize(t2.Body[i])]
    #print list2
    for e in key_list:
        if(any(e in l1 for l1 in list1) or any(e in l2 for l2 in list2)):
            out_list.append(e)
    if(len(out_list)>0):
        outstr = '"'+''.join(' '+item+' ' for item in out_list)+'"'
        #writer.writerow([t2.Id[i],' '.join('"'+item+'"' for item in out_list)])
        writer.writerow([t2.Id[i],outstr])
    else:
        #print t2.Title[i]
        cnt = cnt + 1

print "done1"

t2 = pd1.read_csv('Test.csv',skiprows=nr1,nrows=nr1)
t2.columns=['Id','Title','Body']
for i in range(1,nr1):
    out_list=[]
    list1 = t2.Title[i].split()
    list2 = t2.Body[i].split()
    
    for e in key_list:
        if(any(e in l1 for l1 in list1) or any(e in l2 for l2 in list2)):
            out_list.append(e)
    if(len(out_list)>0):
        outstr = '"'+''.join(' '+item+' ' for item in out_list)+'"'
        #writer.writerow([t2.Id[i],' '.join('"'+item+'"' for item in out_list)])
        writer.writerow([t2.Id[i],outstr])
    else:
        #print t2.Title[i]
        cnt = cnt + 1

print "done2"

t2 = pd1.read_csv('Test.csv',skiprows=2*nr1,nrows=nr1)
t2.columns=['Id','Title','Body']
for i in range(1,nr1):
    out_list=[]
    list1 = t2.Title[i].split()
    list2 = t2.Body[i].split()
    
    for e in key_list:
        if(any(e in l1 for l1 in list1) or any(e in l2 for l2 in list2)):
            out_list.append(e)
    if(len(out_list)>0):
        outstr = '"'+''.join(' '+item+' ' for item in out_list)+'"'
        #writer.writerow([t2.Id[i],' '.join('"'+item+'"' for item in out_list)])
        writer.writerow([t2.Id[i],outstr])
    else:
        #print t2.Title[i]
        cnt = cnt + 1

print "done3"
        
t2 = pd1.read_csv('Test.csv',skiprows=3*nr1,nrows=nr2)
t2.columns=['Id','Title','Body']
for i in range(1,nr2):
    out_list=[]
    list1 = t2.Title[i].split()
    list2 = t2.Body[i].split()
    
    for e in key_list:
        if(any(e in l1 for l1 in list1) or any(e in l2 for l2 in list2)):
            out_list.append(e)
    if(len(out_list)>0):
        outstr = '"'+''.join(' '+item+' ' for item in out_list)+'"'
        #writer.writerow([t2.Id[i],' '.join('"'+item+'"' for item in out_list)])
        writer.writerow([t2.Id[i],outstr])
    else:
        #print t2.Title[i]
        cnt = cnt + 1
print cnt            
ofile.close()    
