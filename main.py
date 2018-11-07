import sys
import socket
import asyncio
import websockets
# import threading
# class T1 (threading.Thread):
#     def run (self):
#         # stuff here
# class T2 (threading.Thread):
#     def run(self):



async def hello_server(websocket, path):
    name = await websocket.recv()
    print(f"< {name}")

    greeting = f"Hello {name}!"

    await websocket.send(greeting)
    print(f"> {greeting}")

async def hello_client(dest):
    async with websockets.connect(
            'ws://' + dest) as websocket:
        name = input("What's your name? ")

        await websocket.send(name)
        print(f"> {name}")

        greeting = await websocket.recv()
        print(f"< {greeting}")

def main():
    script = sys.argv[0]
    arg1 = sys.argv[1] if len(sys.argv) >= 2 else None

    hostname = socket.gethostname()
    # how websocket.server works
    # open 3 seperate web sockets on 3 ports; 8765, +1, +2
    # server prints ports it recieved message, and print message, and send hello back to client
    # hostname based logic
    if arg1 == "server":
        start_server = websockets.serve(hello_server, '*', 8765)

        asyncio.get_event_loop().run_until_complete(start_server)
        asyncio.get_event_loop().run_forever()
    if arg1 == "server1":
        start_server = websockets.serve(hello_server, '*', 8766)

        asyncio.get_event_loop().run_until_complete(start_server)
        asyncio.get_event_loop().run_forever()
    if arg1 == "server2":
        start_server = websockets.serve(hello_server, '*', 8767)
        asyncio.get_event_loop().run_until_complete(start_server)
        asyncio.get_event_loop().run_forever()
    else:
        asyncio.get_event_loop().run_until_complete((arg1))


# if __name__ == '__main__':
    t1 = T1()
    t1.start()
    t2 = T2()
    t2.start()
if __name__ == '__main__':
   main()