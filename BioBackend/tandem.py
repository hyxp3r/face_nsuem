import pyodbc
import pandas as pd

server = ''
database = ''
username = ''
password = ''
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID='+username+';PWD=' + password)

def tandem(personalNumber: str):


    check = pd.read_sql_query(f""" select  
    VPO.LASTNAME 'firstName'
    ,VPO.FIRSTNAME 'middleName' 
    ,ISNULL(VPO.MIDDLENAME, '') 'surname'
    ,REPLACE(REPLACE(VPO.PHONEMOBILE, '+', ''), ' ', '') 'telephone'
    ,VPO.SUBJECTCODE + ' ' + VPO.SUBJECTTITLE as 'programTitle'
    ,VPO.GROUPTITLE as 'group'
    ,VPO.DEVELOPFORMTITLE 'form'
    ,VPO.COURSE as 'course'
    ,CASE when VPO.COMPENSATIONTITLE = 'на основе полного возмещения затрат' then 'договор' else 'бюджет' end 'compensation'

    from vpo2_view as VPO
    
    where VPO.BOOKNUMBER = '{personalNumber}'""", cnxn)

    check = pd.DataFrame(check).to_dict('list')
    return check
    print(check)

