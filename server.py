import random
from threading import Lock
from os import linesep as ls
import json
# unsent, interested in last value
unsent_urls =   ["https://static1.squarespace.com/static/59ec1dc7268b9699fe3a82ce/t/5bae8df74785d3638a102c1a/1538166381084/download+-+Nolan+Gray.png",
                "https://static1.squarespace.com/static/59ec1dc7268b9699fe3a82ce/t/5baa55fa24a694c239750c1d/1537889846029/20180824_144614+-+Linnea+May.jpg",
                "https://static1.squarespace.com/static/59ec1dc7268b9699fe3a82ce/t/5baa57f6a4222f04be1d89f7/1537890321439/Propic+2+-+Junyoung+Lim.JPG",
                "https://static1.squarespace.com/static/59ec1dc7268b9699fe3a82ce/t/59fdd14c71c10b5cf30d9170/1538155134044/Kevin.jpg",
                "https://static1.squarespace.com/static/59ec1dc7268b9699fe3a82ce/t/5bae629f1905f46e2a7ad256/1538155210553/Yuji.JPG",
                "https://static1.squarespace.com/static/59ec1dc7268b9699fe3a82ce/t/5bae62e5c830256b79fdf0c5/1538155256226/Julia.jpg",
                "https://static1.squarespace.com/static/59ec1dc7268b9699fe3a82ce/t/5bae6228104c7b7a4c3a677e/1538155088361/cds_photo+-+Haram+Kim.PNG",
                "https://static1.squarespace.com/static/59ec1dc7268b9699fe3a82ce/t/59fdd19b08522952619fcd42/1538155318297/Kenta.JPG",
                "https://static1.squarespace.com/static/59ec1dc7268b9699fe3a82ce/t/5bae6114a4222f0eb782c09b/1538154926187/milan.png"]

# sent urls stored with popped values from unsent_urls
sent_urls = []

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
        # OLD: problem = random.randint(0,100)
        problem = unsent_urls.pop()

        # dictionary version of sent urls?
        problem_package = {"url": problem}

        # problem is popped url, put into sent list
        sent_urls.append(problem)

        await websocket.send(json.dumps(problem_package))
        print(f"({id}) sent problem: {problem}")

        # get solution from client
        solution = json.loads(await websocket.recv())
        print(f"({id}) received solution: {solution}")

        # save solution
        save_solution(id, solution["content"])