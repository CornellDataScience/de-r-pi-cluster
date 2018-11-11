import random

async def run(websocket, path):
    # get ID data
    client_name = await websocket.recv()
    client_port = websocket.port
    id = str(client_name) + ":" + str(client_port)
    print(f"({id}) sent ID")

    while True:
        # send problem to client
        problem = str(random.randint(0,100))
        await websocket.send(problem)
        print(f"({id}) sent problem: {problem}")

        # get solution from client
        solution = await websocket.recv()
        print(f"({id}) received from client: {solution}")