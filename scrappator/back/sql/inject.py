from setup import * 
def user():
    with connection:
        with connection.cursor() as cursor :
            #requete sql :
            #todo voir pouquoi elle s'éxexcute automatiquement et pas dan la page /scrapator (ce lance au python manage.py runserver)

             sql = "INSERT INTO `users` (`username`,`email`, `password`) VALUES (%s, %s,%s)"
             #execution de la requete sql / remplissage des %s :
             cursor.execute(sql,('toto','webmaster@gmail.com','S3cret!'))
             #commit pour sauvegarder les changements 
             connection.commit()
             
def data():
    with connection:
        with connection.cursor as cursor : 
            sql = "INSERT INTO `data`(`nom`,`image`,`lien`,`prix`) VALUES (%s,%s,%s,%s)"
            cursor.execute(sql,(data_name,image,lien,prix))
            connection.commit
            
def shop_sneakers():
    with connection:
        with connection.cursor as cursor:
            sql= "INSERT INTO `shop_sneaker`(`nom`,`url`,`separator`) VALUES (%s,%s,%s)"
            cursor.execute(sql,(nom,url,separateur))

def views():
    #pour afficher le resultat : 
             with connection:
                with connection.cursor() as cursor:
                    sql = "SELECT `id`,`password` FROM `users`  WHERE `email` =%s"
                    cursor.execute(sql,("webmaster@gmail.com",))
                    result = cursor.fetchone()