# 파일명: server.py
# 작성자: 유태욱
# 작성일자: 2022-11-30
# 주요기능: 파이썬 스레드 기반 채팅 프로그램 구현 프로그램 (서버 부분)
# 최종수정일자: 2022-11-30
# 수정내용: 최초작성

from Class_TextChat import *  # 채팅 프로그램을 사용하기 위한 모듈 import

if __name__ == "__main__":  # 메인 메소드인 경우
    print("Running TCP server")  # 서버 역할 실행 임을 출력한다.
    textChatServer = TextChat("Server")  # 채팅 프로그램을 서버 역할로 생성한다.
    textChatServer.win.mainloop()  # 생성된 채팅 프로그램의 UI를 실행한다.
