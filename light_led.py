#-*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time # sleep 용도

# GPIO.BOARD 보드 상의 핀 번호 사용
# GPIO.BCM . 핀번호가 아니라 Broadcom SOC channel을 사용 GPIOXX의 XX 번호를 사용
GPIO.setmode(GPIO.BOARD)

# 7번 핀을 사용함
light_pin = 7

def rc_time (light_pin):
    count = 0

    #Output on the pin for
    GPIO.setup(light_pin, GPIO.OUT) # 7번 핀을 입력으로 설정
    GPIO.output(light_pin, GPIO.LOW) # 7번 핀의 디지털 출력 설정
    #  셋중에 아무거나 골라서 사용
    #  1, GPIO.HIGH, True
    #  0, GPIO.LOW, False

    time.sleep(0.1) # 0.1 sec sleep

    #  7번 핀을 input으로 변경
    GPIO.setup(light_pin, GPIO.IN)

    # 7번 핀으로부터 읽은 값이 HIGH가 될 때까지 count 수행
    # 그래서 실행해보면 센서 주변이 어두울 수록 카운트 값이 크다.
    while (GPIO.input(light_pin) == GPIO.LOW):
        count += 1

    return count


# 스크립트가 인터럽트 될때 catch하고, 올바르게 cleanp
try:
    # 메인 루프
    while True:
        print (rc_time(light_pin)) # 조도 센서의 값 출력

except KeyboardInterrupt:
    pass

finally:
    GPIO.cleanup() # 사용했던 모든 포트에 대해서 정리

