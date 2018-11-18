import websockets
import time
import socket
from os import linesep as ls
import json

def recognize_faces(url):
    # takes a URL for an image, downloads, finds faces, and returns a dict of results
    return {}

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
            # solution = str(int(problem["content"]) + 1)
            # time.sleep(5)
            # solution_package = {"content": solution}
            solution_package = recognize_faces(problem["url"])

            # send result back to server
            await websocket.send(json.dumps(solution_package))
            print(f"sent solution: {solution_package}")
            print(ls)