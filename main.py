import sys
import socket
import asyncio
import websockets
import signal
import server
import client

signal.signal(signal.SIGINT, signal.SIG_DFL)

def main():
    script = sys.argv[0]
    arg1 = sys.argv[1] if len(sys.argv) >= 2 else None

    #hostname = socket.gethostname()
    
    # hostname based logic
    if arg1 == "server":
        print("Server starting...")
        # create 3 servers
        # TODO: make this not terrible
        server_1 = websockets.serve(server.run, host='localhost', port=8765)
        server_2 = websockets.serve(server.run, host='localhost', port=8766)
        server_3 = websockets.serve(server.run, host='localhost', port=8767)

        asyncio.get_event_loop().run_until_complete(server_1)
        asyncio.get_event_loop().run_until_complete(server_2)
        asyncio.get_event_loop().run_until_complete(server_3)

        # run event loop
        asyncio.get_event_loop().run_forever()
    else:
        print("Client starting...")
        asyncio.get_event_loop().run_until_complete(client.run(arg1))

if __name__ == '__main__':
   main()