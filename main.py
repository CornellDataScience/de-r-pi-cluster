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

    hostname = socket.gethostname()
    # how websocket.server works
    # open 3 seperate web sockets on 3 ports; 8765, +1, +2
    # server prints ports it recieved message, and print message, and send hello back to client
    # hostname based logic
    if arg1 == "server":
        print("Server starting...")
        # create 3 servers
        # TODO: make this not terrible
        server_1 = websockets.serve(server.run, host='*', port=8765)
        server_2 = websockets.serve(server.run, host='*', port=8766)
        server_3 = websockets.serve(server.run, host='*', port=8767)

        asyncio.get_event_loop().run_until_complete(server_1)
        asyncio.get_event_loop().run_until_complete(server_2)
        asyncio.get_event_loop().run_until_complete(server_3)

        # run event loop
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
        print("Client starting...")
        asyncio.get_event_loop().run_until_complete(client.run(arg1))


# if __name__ == '__main__':
    t1 = T1()
    t1.start()
    t2 = T2()
    t2.start()
if __name__ == '__main__':
   main()