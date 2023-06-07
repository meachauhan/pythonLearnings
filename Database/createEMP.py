import mysql.connector
conn=mysql.connector.connect(host='localhost',database='mydb',user='root',password='akash123')
if conn.is_connected():
    print("Conntectd to mysql db")
    
cursor=conn.cursor()
try:
    cursor.execute("insert into emp values(3,'Garima',100300)")
    conn.commit()
    print("Employee Added Successfully")
except:
    conn.rollback()

row=cursor.fetchall()
for r in row:
    print(r)
print("Total no of rows: " , cursor.rowcount)
cursor.close()
conn.close()