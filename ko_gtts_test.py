#-*- coding: utf-8 -*-
from gtts import gTTS
import os
import sys

#chang Unicode. 소스파일의 맨위에 실행해줘야 한다.
def init():
    reload(sys)
    sys.setdefaultencoding('utf-8')
    return

def TexttoSpeech_KO(text):
    unicode(text)
    print str(text)

    #한국어로
    tts = gTTS(text=text, lang='ko')

    #파일 저장
    filename = "gTTS_KO.mp3"
    tts.save(filename)

    #음원재생 플레이어 실행. mp3 재생 플레이어는: omxplayer 파일이름
    os.system("omxplayer " + filename)


