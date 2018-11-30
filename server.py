import random
from threading import Lock
from os import linesep as ls
import json

results_lock = Lock()
results = {}

def save_solution(client_id, soln):
    with results_lock:
        if client_id in results:
            results[client_id].append(soln)
        else:
            results[client_id] = [soln]
        
        print(ls + "-=-=-=-=-=-=-=-=-=-=-")
        print("results: " + str(results))
        print("-=-=-=-=-=-=-=-=-=-=-" + ls)

async def run(websocket, path):
    # get ID data
    client_name = await websocket.recv()
    client_port = websocket.port
    id = str(client_name) + ":" + str(client_port)
    print(f"({id}) ID recieved")

    while True:
        # send problem to client
        problem = random.randint(0,100)
        problem_package = {"content": problem}
        await websocket.send(json.dumps(problem_package))
        print(f"({id}) sent problem: {problem}")

        # get solution from client
        solution = json.loads(await websocket.recv())
        print(f"({id}) received solution: {solution}")

        # save solution
        save_solution(id, solution["content"])