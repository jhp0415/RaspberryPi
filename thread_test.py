import threading, time
import connect_db
#from ko_gtts_test import TexttoSpeech_KO

#Lock 객체 선언
lock = threading.Lock()
dr_status = False
drone = connect_db.DroneSQL()

#드론의 on/off 상태 체크하는 쓰레드
def CheckOnOff(dr):
    try:
        dr.ConnectMySQL()
        global dr_status
        while(1):
            lock.acquire()

            result = dr.getOnOffOne()
            if result != None:
                dr_status = result[0]
                print(dr_status)
            else:
                lock.release()
                break
            lock.release()


    except Exception as e:
        print(e)

    finally:
        dr.DisconnectMySQL()

    return

#조도 센서 및 LED 관리하는 쓰레드
def SensorAndLED():
    while(1):
        print(dr_status)
    return




# 메인 함수 실행하기
if __name__ == "__main__":
    #스레드 실행
    th1 = threading.Thread(target=CheckOnOff, args=(drone, ))
    #th2 = threading.Thread(target=SensorAndLED, args=())

    th1.start()
    #th2.start()

    th1.join()
    #th2.join()


    print("all the program is finished")



