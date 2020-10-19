import pymysql

def db_host(database,sql):
    db_host = pymysql.connect('localhost','root','123456',database)
    cursor = db_host.cursor()
    cursor.execute(sql)
    db_date = cursor.fetchall()
    cursor.close()
    db_host.close()
    return db_date