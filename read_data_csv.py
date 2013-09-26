import numpy
import csv
import nltk

from numpy import genfromtxt
import pandas as pd1
nr1 = 2013337
#nr2 = 5000
#nr2 =  2013337 - 3*nr1

t = pd1.read_csv('Train.csv',nrows=10) #read 10 rows
#print t.Tags

#t2 = pd1.read_csv('Test.csv',nrows=nr1)
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

f = open('Test.csv','rb')
ofile= open('res.csv', 'wb')
writer = csv.writer(ofile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
#writer.writerow(["Id","Tags"])
rown = 0
try:
    reader = csv.reader(f)
    for row in reader:
        
        out_list=[]
        list1 = row[1].split()
        list2 = row[2].split()
        
        for e in key_list:
            if(any(e in l1 for l1 in list1) or any(e in l2 for l2 in list2)):
                out_list.append(e)
        if(len(out_list)>0):
            outstr = ''+''.join(''+item+' ' for item in out_list)+''
            newstr = '"'+outstr+'"'
            #writer.writerow([t2.Id[i],' '.join('"'+item+'"' for item in out_list)])
            writer.writerow([row[0],newstr])
        else:
            #print t2.Title[i]
            if(rown == 0):
                writer.writerow([row[0],'Tags'])
            else:
                writer.writerow([row[0],'"programming"'])
            cnt = cnt + 1
        rown = rown + 1
finally:
    f.close()    
print "done1"


ofile.close()    
