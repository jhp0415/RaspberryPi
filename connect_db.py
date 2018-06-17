#-*- coding: utf-8 -*-
import pymysql

class DroneSQL:
    #db='INFORM_DRONE_STATUS',
    #sql = 'SELECT STATUS FROM DRONE_ON_OFF WHERE NAME=MI DRONE'
    def ConnetDB(self, sql):
        self.conn = pymysql.connect(host='13.125.251.95',
                               password='cbnuroot123',
                               port=3306, user='root',
                               db='INFORM_DRONE_STATUS',
                               charset='utf8')
        self.cursor = self.conn.cursor()
        #sql = 'SELECT STATUS FROM DRONE_ON_OFF WHERE NAME="MI DRONE"'
        self.cursor.execute(sql)
        #print("db에 연결합니다.")
        return

    def getOne(self):
        result = self.cursor.fetchone()
        return result

    def getAll(self):
        result = self.cursor.fetchall()
        return result

    def DisconnetDB(self):
        self.cursor.close()
        self.conn.close()
        return


