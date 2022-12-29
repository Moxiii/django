import pymysql , pymysql.cursors


#connexion to DATABASE : 
connection = pymysql.connect(host='localhost',
                             user='root',
                             database='scrappator',
                             password='',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
                             
#connection or create to db 
