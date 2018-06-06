#-*- coding: utf-8 -*-
import pymysql

class DroneSQL:
    conn = None
    cursor = None
    def ConnectMySQL(self):
        self.conn = pymysql.connect(host='13.125.251.95',
                               port=3306, user='root',
                               password='cbnuroot123',
                               db='INFORM_DRONE_STATUS',
                               charset='utf8')
        self.cursor = self.conn.cursor()
        sql = 'SELECT STATUS FROM DRONE_ON_OFF WHERE NAME=%s'
        self.cursor.execute(sql, ('MI DRONE'))
        print("db에 연결합니다.")
        return

    def getOnOffOne(self):
        result = self.cursor.fetchone()
        return result

    def getOnOffAll(self):
        result = self.cursor.fetchall()
        return result

    def DisconnectMySQL(self):
        print("db 종료합니다")
        self.cursor.close()
        self.conn.close()
        return


