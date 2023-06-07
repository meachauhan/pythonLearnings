import mysql.connector
conn=mysql.connector.connect(host='localhost',database='mydb',user='root',password='akash123')
if conn.is_connected():
    print("Conntectd to mysql db")
    
cursor=conn.cursor()
cursor.execute("select * from emp")
row=cursor.fetchone()
while row is not None:
    print(row)
    row=cursor.fetchone() 

row=cursor.fetchall()
for r in row:
    print(r)
print("Total no of rows: " , cursor.rowcount)
cursor.close()
conn.close()