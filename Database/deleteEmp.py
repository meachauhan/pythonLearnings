import mysql.connector
def delete(id):
    conn=mysql.connector.connect(host='localhost',database='mydb',user='root',password='akash123')
    if conn.is_connected():
        print("Conntectd to mysql db")
        
        cursor=conn.cursor()
        str="delete from emp where id='%d'"
        args=(id)
        try:
            cursor.execute(str % args)
            conn.commit()
            print("Employee Deleted Successfully")
        except:
            conn.rollback()
        finally:
            cursor.close()
            conn.close()

empId=int(input("Enter the emp id"))

delete(empId)
