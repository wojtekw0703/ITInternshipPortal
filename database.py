from indeed_scraping import list_of_company,list_of_locations, list_of_titles, list_of_urls
from wayup_scraping import ultimate_title_list,ultimate_compname_list, ultimate_jurl_list
import mysql.connector


def insertVariblesIntoTable(id, job_title, company_name, location, url_address):
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='@@@@@',
                                             user='@@@@@',
                                             password='')
        cursor = connection.cursor()
        mySql_insert_query = """INSERT INTO internships (id, job_title, company_name, location, url_address) 
                                VALUES (%s, %s, %s, %s, %s) """

        recordTuple = (id, job_title, company_name, location, url_address)
        cursor.execute(mySql_insert_query, recordTuple)
        connection.commit()
        print("Record inserted successfully into internship table")

    except mysql.connector.Error as error:
        print("Failed to insert into MySQL table {}".format(error))

    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

for i in range(0,len(list_of_titles)-1):
    insertVariblesIntoTable(i,list_of_titles[i],list_of_company[i],list_of_locations[i],list_of_urls[i])
for k in range(len(list_of_titles),len(ultimate_title_list)-2):
    insertVariblesIntoTable(k, ultimate_title_list[k], ultimate_compname_list[k], "USA", ultimate_jurl_list[k])
