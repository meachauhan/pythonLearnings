import mysql.connector
def update(id,salary):
    conn=mysql.connector.connect(host='localhost',database='mydb',user='root',password='akash123')
    if conn.is_connected():
        print("Conntectd to mysql db")
        
        cursor=conn.cursor()
        str="update emp set sal='%d' where id='%d'"
        args=(salary,id)
        try:
            cursor.execute(str % args)
            conn.commit()
            print("Employee Updated Successfully")
        except:
            conn.rollback()
        finally:
            cursor.close()
            conn.close()

empId=int(input("Enter the emp id  to update:"))
salary=int(input("Enter the emp salary to update:"))
update(empId,salary)