#-*- coding: utf-8 -*-
import pymysql
conn = pymysql.connect(host='13.125.251.95',
                       port=3306, user='root',
                       password='cbnuroot123',
                       db='INFORM_DRONE_STATUS',
                       charset='utf8')

def ConnectMySQL():
    with conn.cursor() as cursor:
        sql = 'SELECT * FROM DRONE_ON_OFF WHERE NAME=%s'
        cursor.execute(sql,('MI DRONE'))
        result = cursor.fetchall()
        print("db를 연결합니다.")
        print(result)
        # (1, 'test@test.com', 'my-passwd')



def DisconnectMySQL():
    print("db 종료합니다")
    conn.close()
