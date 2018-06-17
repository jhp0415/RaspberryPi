#-*- coding: utf-8 -*-
import threading, time
import connect_db
import ko_gtts_test
import led_sensor
import light_sensor


#드론의 on/off 상태 체크하는 쓰레드
def CheckOnOff(dr):
    try:
        global dr_status
        while(1):
            lock.acquire()  #Lock 실행

            dr.ConnetDB('SELECT STATUS FROM DRONE_ON_OFF WHERE NAME="MI DRONE"')
            result = dr.getOne()

            if result is not None:
                dr_status = result[0]
                print(dr_status)
            else:
                lock.release()
                break

            dr.DisconnetDB()

            lock.release()  #Lock 해제
            time.sleep(5)

    except Exception as e:
        print("e: ", e)

    finally:
        dr_status = None
        dr.DisconnetDB()
        print("dr_status db를 종료합니다.")
    return

###############################################################################################

#조도 센서 및 LED 관리하는 쓰레드
def SensorAndLED(light, led):
    try:
        global dr_status
        while(1):
            lock.acquire()  #드론의 상태를 체크하기전 Lock 실행

            if dr_status == "ON":
                result = light.rc_time()
                print(result)
                if result > 5000:   #조도가 5000이상으로 어둡다면, LED On
                    print("LED On")
                    led.LEDOn()
                else:
                    print("LED Off")    #조도가 밝으면, LED Off
                    led.LEDOff()

            elif dr_status == "OFF":    #드론이 꺼져있으면, 강제 LED off
                led.LEDOff()
            elif dr_status == None: #Thread1이 종료된 상태라면(데이터베이스에 더이상 값이 없다면), Thread2 종료
                lock.release()  # Lock 해제
                break

            lock.release()  #Lock 해제

    except Exception as e:
        print("e: ", e)

    finally:
        light.CleanLight()
        led.CleanLED()
    return

#################################################################################################

#DB에 입력된 문장을 스피커로 출력하는 쓰레드
def DroneSpeaker(sp):
    try:
        global dr_status
        before = None
        while(1):
            sp.ConnetDB('SELECT Broadcast FROM DRONE_SPEAK WHERE Name="MI DRONE"')
            lock.acquire()  # 드론의 상태를 체크하기전 Lock 실행

            if dr_status == "ON":   #드론이 작동중이면,
                lock.release()  # Lock 해제
                result = sp.getOne()    #출력할 문장 읽어오기
                if result is not None:
                    if result[0] != before:
                        #출력하기
                        before = result[0]
                        ko_gtts_test.TexttoSpeech_KO(result[0])

            elif dr_status != "ON": #Thread3 종료
                lock.release()  # Lock 해제
                break



    except Exception as e:
        print("e: ", e)

    finally:
        sp.DisconnetDB()
        print("dr_speak db를 종료합니다.")
    return

#################################################################################################

#인코딩 설정 실행
ko_gtts_test.init()

#Lock 객체 선언
lock = threading.Lock()

#객체 및 변수 생성
dr_status = False   #드론의 상태를 체크하는 변수, glrobal 변수로 사용한다.
#dr_status = "ON"
db_status = connect_db.DroneSQL()
led = led_sensor.myLED(11)  #LED 클래스 생성
light = light_sensor.myLight(7) #조도센서 클래스 생성
db_speak = connect_db.DroneSQL()

# 메인 함수 실행하기############################################################################
if __name__ == "__main__":
    #데이터베이스에서 드론의 상태를 주기적으로 받아오는 쓰레드
    th1 = threading.Thread(target=CheckOnOff, args=(db_status, ))
    #드론의 상태에 따라 조도센서와 LED 센서 동작하는 쓰레드
    th2 = threading.Thread(target=SensorAndLED, args=(light, led, ))
    #드론 스피커 출력하기
    th3 = threading.Thread(target=DroneSpeaker, args=(db_speak,))

    #쓰레드 실행
    th1.start()
    th2.start()
    th3.start()

    th1.join()
    th2.join()
    th3.join()


    print("all the program is finished")



