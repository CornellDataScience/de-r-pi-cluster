import websockets
import time
import socket
from os import linesep

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
            print(f"received problem: {problem}")

            # TODO: do processing here
            solution = str(int(problem) + 1)
            time.sleep(5)

            # send result back to server
            await websocket.send(solution)
            print(f"sent solution: {solution}")
            print(linesep)