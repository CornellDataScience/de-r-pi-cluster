import websockets
import time
import socket

async def run(dest):
    async with websockets.connect(
            'ws://' + dest) as websocket:

        # get our hostname
        hostname = socket.gethostname()

        # send hostname
        await websocket.send(hostname)
        
        while True:
            # get problem
            problem = await websocket.recv()
            print(f"received start value {problem}")

            # TODO: do processing here
            solution = str(int(problem) + 1)
            time.sleep(5)

            # send result back to server
            await websocket.send(solution)
            print(f"sent to server: {solution}")
            
            # get a new problem
            problem = await websocket.recv()
            print(f"received from server: {problem}")