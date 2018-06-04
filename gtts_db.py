#-*- coding: utf-8 -*-
import connect_db
from ko_gtts_test import TexttoSpeech_KO

try:
    connect_db.ConnectMySQL()

except:
    print("db connect error")




text = "안녕하세요, 라즈베리파이 입니다."

TexttoSpeech_KO(text)


connect_db.DisconnectMySQL()