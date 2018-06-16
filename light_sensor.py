#-*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time # sleep 용도

class myLight:
    #7번 핀 사용
    def __init__(self, pin):
        self.light_pin = pin
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)


    def rc_time(self):
        count = 0

        # Output on the pin for
        GPIO.setup(self.light_pin, GPIO.OUT)  # 7번 핀을 입력으로 설정
        GPIO.output(self.light_pin, GPIO.LOW)  # 7번 핀의 디지털 출력 설정
        #  셋중에 아무거나 골라서 사용
        #  1, GPIO.HIGH, True
        #  0, GPIO.LOW, False

        time.sleep(0.1)  # 0.1 sec sleep

        #  7번 핀을 input으로 변경
        GPIO.setup(self.light_pin, GPIO.IN)

        # 7번 핀으로부터 읽은 값이 HIGH가 될 때까지 count 수행
        # 그래서 실행해보면 센서 주변이 어두울 수록 카운트 값이 크다.
        while (GPIO.input(self.light_pin) == GPIO.LOW):
            count += 1

        return count

    def CleanLight(self):
        GPIO.cleanup()  # 사용했던 모든 포트에 대해서 정리

