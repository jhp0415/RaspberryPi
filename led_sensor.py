#-*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time

class myLED:
    #11번 핀 사용하기
    def __init__(self, pin):
        self.led_pin = pin

        GPIO.setwarnings(False)
        # 핀 설정 초기화
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.led_pin, GPIO.OUT)
        #출력 초기화
        GPIO.output(self.led_pin, False)

    def LEDOn(self):
        GPIO.output(self.led_pin, True)

    def LEDOff(self):
        GPIO.output(self.led_pin, False)

    def CleanLED(self):
        GPIO.cleanup()

