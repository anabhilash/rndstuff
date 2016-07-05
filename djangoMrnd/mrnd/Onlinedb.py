import click,os,sys
import MySQLdb
import django
import openpyxl
from bs4 import BeautifulSoup
import urllib


sys.path.append("C:\summer\djangoMrnd")
os.environ["DJANGO_SETTINGS_MODULE"] = "djangoMrnd.settings"
django.setup()

from mrnd.models import *

@click.group()
def onlinedb():
    """database commands"""
    pass

@onlinedb.command()
@click.argument('username')
@click.argument('password')
@click.argument('dbname')
def createdb(username,password,dbname):
    """create database"""
    conn=MySQLdb.connect(host='localhost',user=username,passwd=password)
    cursor=conn.cursor()
    query='CREATE DATABASE '+dbname
    cursor.execute(query)

@onlinedb.command()
@click.argument('username')
@click.argument('password')
@click.argument('dbname')
def dropdb(username,password,dbname):
    """drop database"""
    conn=MySQLdb.connect(host='localhost',user=username,passwd=password)
    cursor=conn.cursor()
    query='DROP DATABASE '+dbname
    cursor.execute(query)

@onlinedb.command()
@click.argument('excelfile')
@click.argument('htmlfile')
def populatedb(excelfile,htmlfile):
    """populateData Command"""
    dumpExcel(excelfile)
    dumpHtml(htmlfile)

def dumpExcel(excelFile):
    ex = openpyxl.load_workbook(excelFile)
    ws1 = ex.get_sheet_by_name('Colleges')
    flag=False
    for row in ws1:
        if flag:
            cname=row[0].value
            cacronym=row[1].value
            clocation=row[2].value
            ccontact=row[3].value
            c=College(name=cname,acronym=cacronym,location=clocation,contact=ccontact)
            c.save()
        flag=True
    ws2=ex.get_sheet_by_name('Current')
    flag=False
    for row in ws2:
        if flag:
            sname=row[0].value
            sacronym=row[1].value
            semail=row[2].value
            sdbname=row[3].value
            sdbname=sdbname.lower()
            scollege=College.objects.get(acronym=sacronym)
            s=Student(name=sname,email=semail,dbfolder=sdbname,college=scollege,dropped=False)
            s.save()

        flag=True
    ws3=ex.get_sheet_by_name('Deletions')
    flage=False
    for row in ws3:
        if flag:
            sname=row[0].value
            sacronym=row[1].value
            semail=row[2].value
            sdbname=row[3].value
            sdbname=sdbname.lower()
            try:
                scollege=College.objects.get(acronym=sacronym)
                s=Student(name=sname,email=semail,dbfolder=sdbname,college=scollege,dropped=True)
                s.save()
            except Exception as e:
                pass
        flag=True

def dumpHtml(htmlfile):
    htmlsrc=urllib.urlopen(htmlfile)
    try:
        s = BeautifulSoup(htmlsrc, "html.parser")
    except UserWarning as u:
        pass
    tables=s.findAll('table')
    rows=tables[0].findAll('tr')
    for row in rows:
        first_col=False
        marks=[]
        for col in row:
            if first_col:
                marks.append(col.text)
            first_col=True
        nl = marks[0].split('_')
        try:
            stud=Student.objects.get(dbfolder=str(nl[2]))
            m=Marks(student=stud,transform=marks[1],from_custom_base26=marks[2],get_pig_latin=marks[3],top_chars=marks[4],total=marks[5])
            m.save()
        except Exception as e:
            pass



if __name__=='_ss_main__':
    onlinedb()
