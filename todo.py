
from fastapi import APIRouter, Path
from model import ToDo


todo_router = APIRouter()

todo_list = []
todo_counter = 0

@todo_router.post("/todo")
async def add_todo(todo: ToDo ) ->dict: # /todo 라는 경로에 들어오면 add_todo라는 함수를 실행시켜라. 
    # 이 함수는 todo 라는 dict 형태의 값을 받을 것이고 dict 형태로 리턴할 것이다.
    #파이썬의 dict 가 json 과 형식이 같아서 이렇게 함.
    global todo_counter
    todo.id = todo_counter = todo_counter+ 1
    todo_list.append(todo)
    return {
        "msg":"todo added "
    }

@todo_router.delete("/todo/{todo_id}")
async def delete_todo(todo_id: int = Path(..., title="the ID of the todo to delete")) -> dict:
    for index, todo in enumerate(todo_list):
        if todo.id == todo_id:
            del todo_list[index]
            return {"msg": f"Todo with ID {todo_id} deleted successfully"}
    return {"msg": "Todo with supplied ID doesn't exist"}

@todo_router.get("/todo") #/todo 를 get으로 접근할 수도 있다. create 하는 게 post라면 get은 read 읽어들이는 것. 
# 읽기 위해 .get 메소드를 사용함.
# 읽었을 때엔 retrieve_todos() 함수를 사용할 건데 이것도 dict 형태로 반환될 것이야.
# 뭘 리턴하냐고? "todos" : 그리고 여기는 todo_list라는 리스트를 반환할거야. 

async def retrieve_todos() -> dict:
    return{
        "todos" : todo_list
    }
    
@todo_router.get("/todo/{todo_id}")
async def get_single_todo(todo_id: int = Path(..., title="the ID of the todo to retrieve")) -> dict:
    for todo in todo_list:
        if todo.id == todo_id:
            return {"todo" : todo}
    return {"msg": "todo with supplied ID doesn't exist"}
 