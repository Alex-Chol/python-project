import pyodbc
conn = pyodbc.connect('driver=SQL Server Native Client 10.0;server=ALEX_HUA;database=house;uid=sa;pwd=787001245')
cursor = conn.cursor()
#cursor.execute(sql)   %传递sql语句给数据库
cursor.execute("insert house_data1 values('222','12',4,123)")
conn.commit()
#cursor.execute("select * from house_data")
#row = cursor.fetchone()
#print(row)
conn.close()