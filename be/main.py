import socketio
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

sio = socketio.AsyncServer(async_mode='asgi', cors_allowed_origins='*')
app = FastAPI()
socket_app = socketio.ASGIApp(sio, other_asgi_app=app)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@sio.event
async def connect(sid, environ):
    print("connect ", sid)

#receive data from client
@sio.event
async def client_send(sid, data: list[any]):
    print("client sent:  ", data)
    squared = int(data[0]) ** 2
    # Example of sending an acknowledgment or modified message back to the sender
    await sio.emit('server_response', squared, to=sid)

@sio.event
def disconnect(sid):
    print('disconnect ', sid)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(socket_app, host="0.0.0.0", port=8000)