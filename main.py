import sys
import socket
import asyncio
import websockets

async def hello_server(websocket, path):
    name = await websocket.recv()
    print(f"< {name}")

    greeting = f"Hello {name}!"

    await websocket.send(greeting)
    print(f"> {greeting}")

async def hello_client(dest):
    async with websockets.connect(
            'ws://' + dest + ':8765') as websocket:
        name = input("What's your name? ")

        await websocket.send(name)
        print(f"> {name}")

        greeting = await websocket.recv()
        print(f"< {greeting}")

def main():
    script = sys.argv[0]
    arg1 = sys.argv[1] if len(sys.argv) >= 2 else None

    hostname = socket.gethostname()
    
    # hostname based logic
    if arg1 == "server":
        start_server = websockets.serve(hello_server, '*', 8765)

        asyncio.get_event_loop().run_until_complete(start_server)
        asyncio.get_event_loop().run_forever()
    else:
        asyncio.get_event_loop().run_until_complete(hello_client(arg1))

if __name__ == '__main__':
   main()