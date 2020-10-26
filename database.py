from scraping import find_job_url,find_job_location,find_job_location,find_job_titles, find_job_id, find_company_name
import mysql.connector
from mysql.connector import Error

def insertVariblesIntoTable(id, job_title, company_name,location):
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='internship_database',
                                             table ='internship',
                                             user='root@',
                                             password='')
        cursor = connection.cursor()
        mySql_insert_query = """INSERT INTO internship (id, job_title, company_name, location) 
                                VALUES (%s, %s, %s, %s) """

        recordTuple = (id, job_title, company_name,location)
        cursor.execute(mySql_insert_query, recordTuple)
        connection.commit()
        print("Record inserted successfully into Laptop table")

    except mysql.connector.Error as error:
        print("Failed to insert into MySQL table {}".format(error))

    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

for i in find_job_id:
    insertVariblesIntoTable(find_job_id[i],find_job_titles[i],find_company_name[i],find_job_location[i])
