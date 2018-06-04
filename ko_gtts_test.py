#-*- coding: utf-8 -*-
from gtts import gTTS
import os
import sys
#chang Unicode. 소스파일의 맨위에 실행해줘야 한다.
reload(sys)
sys.setdefaultencoding('utf-8')


#text = u"안녕하세요, 선언할 때 이미 유니코드 입니다."

#외부에서 문장을 입력받았을 때, 문장을 유니코드로 변환시켜야 한다.
#text= "안녕하세요, 충북대학교 정보통신공학부 아이티에스 동아리 입니다."
#text = sys.argv[1]

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


