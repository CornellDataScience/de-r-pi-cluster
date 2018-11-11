import websockets
import time
import socket
from os import linesep as ls
import json

async def run(dest):
    async with websockets.connect(
            'ws://' + dest) as websocket:

        # get our hostname
        hostname = socket.gethostname()

        # send hostname
        await websocket.send(hostname)
        
        while True:
            # get problem
            problem = json.loads(await websocket.recv())
            print(f"received problem: {problem}")

            # TODO: do processing here
            solution = str(int(problem["content"]) + 1)
            time.sleep(5)

            # send result back to server
            solution_package = {"content": solution}
            await websocket.send(json.dumps(solution_package))
            print(f"sent solution: {solution_package}")
            print(ls)