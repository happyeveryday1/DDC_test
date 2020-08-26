import pymysql
con =pymysql.connect(host = '127.0.0.1',port =3306,user = 'root',password = '861128',db = 'test',charset = 'utf8')
cur = con.cursor()
cur.execute("insert test0 value(1,'小王')")
con.commit()