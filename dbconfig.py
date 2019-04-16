import pymysql

class MysqlController:
    def __init__(self, host, id, pw, db_name):
        self.conn = pymysql.connect(host=host, user= id, password=pw, db=db_name,charset='utf8')
        self.curs = self.conn.cursor()

    def insert_values(self,values):
        sql = 'INSERT INTO PROPAGATIONS (secs, percent, freq, cumulative, time_stamp) VALUES (%s, %s ,%s, %s, %s)'

        self.curs.execute(sql, tuple(values))
        self.conn.commit()
