import pyodbc

# Hardcoded Global variables used connect to DB
server = 'HCL-02-NEW-08\SQLEXPRESS01'
database = 'Employeedata1'
username = 'capstone'
password = 'Capstone@123'
cnxn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
cursor = cnxn.cursor()
#print(cnxn)
class Employee_schema:
        def Employee_table(self):
                query1=cursor.execute('''use Employeedata1''')
                query2=cursor.execute('''create table Employee_table(Name varchar(50),salary int,Project varchar(50),)''')
                cnxn.commit()

        def insert_values(self, Name, salary, Project):
                query = '''
                        INSERT INTO Employee_table (Name, salary, Project)
                        VALUES
                        ('{0}',{1},'{2}')  '''

                insertQuery = query.format(Name, salary, Project)
                cursor.execute(insertQuery)
                cnxn.commit()
        def display_employee_details_fromdb(self):
            query = cursor.execute('select * from Employee_table')
            print("display values in the table")
            for tableinfo in query:
                    print("name: {}".format(tableinfo.Name),"salary: {}".format(tableinfo.salary),"project: {}".format(tableinfo.Project))
        def update_details_indb(self):
                query = cursor.execute("UPDATE Employee_table SET Project='java' WHERE Project='c'")
                query1 = cursor.execute('select * from Employee_table')
                print("Updated values in the table")
                for tableinfo in query1:
                        print("Name: {}".format(tableinfo.Name), "salary: {}".format(tableinfo.salary),
                              "Project: {}".format(tableinfo.Project))


obj=Employee_schema()
#obj.Employee_table()
obj.insert_values("prathibha",20000,"c")
obj.display_employee_details_fromdb()
obj.update_details_indb()