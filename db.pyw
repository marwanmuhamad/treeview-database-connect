import pyodbc


# print(pyodbc.drivers())

class Database:
    def __init__(self, database):
        self.con = pyodbc.connect('Driver={MySQL ODBC 8.0 Unicode Driver};Server=localhost;Port=3306;UID=marwan;PWD=marwan;Database=%s' 
                                    %(database))
        self.cursor = self.con.cursor()

    def fetchData(self, table):
        self.cursor.execute("SELECT * FROM %s" %table)
        data = self.cursor.fetchall()
        return data

    def fetchColumns(self):
        column = [x[0] for x in self.cursor.description]
        return column 
    
    def searchItems(self, table = 'orderdetails', x = None):
        self.cursor.execute(f"SELECT * FROM {table} WHERE productCode LIKE '{x}%' OR orderNumber LIKE '{x}%'")
        data = self.cursor.fetchall()
        return data
    
    def __del__(self):
        self.con.commit()
        self.con.close()

if __name__ == '__main__':
    db = Database('classicmodels')
    # data = db.fetchData('orderdetails')
    # column = db.fetchColumns()
    # for row in data:
    #     print(row)
    # print(column)

    # column_tpl = tuple(column)
    
    # print(type(column_tpl))
    
    # cari = db.searchItems(x = '10419')
    # for item in cari:
    #     print(item)

    # print(column_tpl)
    