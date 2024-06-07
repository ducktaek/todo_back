from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from todo import todo_router # main에 todo 를 추가. todo.py 파일의 todo_router를 추가하겠다~
import uvicorn
app = FastAPI()
origins = ["http://127.0.0.1:5500"]#  여기다가 엔진엑스 아마존 주소 등록해야함.

app.add_middleware(
CORSMiddleware,
allow_origins=origins,
allow_credentials=True,
allow_methods=["*"],
allow_headers=["*"],
)
# fastapi 앱 객체 만들어
@app.get("/") # 데코레이터 / 0.0.0.0 뒤에 붙는 주소  0.0.0.0:8000/*여기 내용이 붙음)
async def welcome() -> dict:
    return {
"msg" : "hello world?????" # 주소로 들어오면 jcon 형식의 저 hello world 를 리턴할 것이다. 
}
    
app.include_router(todo_router) 
# a todo_router를 import한 다음엔 app 객체에다가 해당 라우터를 추가해줘야해. 
# 모든 라우팅정보는 main에서 관리가 되어야 한다.


if __name__ == '__main__': # 이런 app 이라는 놈은 uvicorn으로 돌릴거야. 
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
    # 이름은 main.py 의 main 을 따오고 app는 fastapi 의 app객체 . 0.0.0.0 : 로컬. 내 컴퓨터안에서 돌려볼 떄. / port 8000번(80번?) 
    # 0.0.0.0 은 실제 배포할 떄 쓰는 주소.
    # reloac : 내가 코드 수정하고 저장하면 알아서 uvicorn 웹서버를 재시작한다. 
    
    # 터미널 실행 후 가상환경 실행해야만 함. why? 내가 깔아둔 fastapi, uvicorn 은 다 가상환경에만 깔려 있는 거잖아.
    
    # 터미널에서 가상환경 실행하고 파이썬 파일 실행하면 보통 실행안됨. 
    # why? 보통 포트번호가 80으로 설정되어있으니까.
    # 그러면 포트번호를 바꾸기 위해 url 에 localhost:8000 이라고 입력해주면 포트번호 인식해서 실행이 됨.
    # 나중에 배포할 떈 uvicorn.run 했을 때 파일이름, 객체 이름 잘 확인하고
    # 아이피주소 아마 nginx의 그 아이피주소 입력하고 포트번호를 80으로 세팅하던가 해야겠지.
    