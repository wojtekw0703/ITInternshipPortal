from scraping import list_of_id,list_of_company,list_of_locations, list_of_titles, list_of_urls
import mysql.connector
from mysql.connector import Error

def insertVariblesIntoTable(id, job_title, company_name,location, url):
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='internship_database',
                                             table ='internship',
                                             user='root@',
                                             password='')
        cursor = connection.cursor()
        mySql_insert_query = """INSERT INTO internship (id, job_title, company_name, location, url) 
                                VALUES (%s, %s, %s, %s) """

        recordTuple = (id, job_title, company_name,location,url)
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

for i in list_of_id:
    insertVariblesIntoTable(list_of_id[i],list_of_titles[i],list_of_company[i],list_of_locations[i],list_of_urls[i])
