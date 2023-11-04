# HeartRateOnResonite - A websocket server for Resonite
# Developed for Python by AlphaNeon
# Example Resonite client is available at: <ResDB: placeholder>

import websockets
from aioconsole import aprint
import json
import asyncio
import logging
import socket

port = 4456 # Port to listen on, this is the default in HeartRateOnStream
IP = socket.gethostbyname(socket.gethostname())  # Get local IP
stage = 0
connected = False # Use this to check if the client is connected
requestType = ""
requestId = ""
lastHeartrate = 0
heartrate = 0 # This is the heart rate that will be sent to the client
clients = set() # This is a set of all the clients connected to the server, including Resonite or any other client
# This is mostly for debugging
logger = logging.getLogger('websockets')
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler())

async def hello_and_identify(websocket):
    global stage, connected, requestId, requestType
    while True:
        await asyncio.sleep(1)
        # Authentication Steps
        if connected:
            if stage == 0:
                stage += 2
                # Hello!
                await websocket.send(json.dumps({"op": 0, "d": {"obsWebSocketVersion": "5.1.0", "rpcVersion": 1}}))
                print("Hello sent.")
            
            elif stage == 2:
                stage += 1
                # Pretend to be OBS
                await websocket.send(json.dumps({"op": 2, "d": {"negotiatedRpcVersion": 1}}))
                print("Identified, setup complete. Waiting for heart rate data...")
            
            if requestId:
                # Respond to requests
                await websocket.send(json.dumps({"op": 7, "d": {"requestType": requestType, "requestId": requestId, "requestStatus": {"result": True, "code": 100}}}))
                requestId = ""
    
        
async def onMessage(websocket):
    global stage, requestType, requestId, heartrate, lastHeartrate

    async for message in websocket:
        # Parse JSON message into a python dictionary
        data = json.loads(message)

        # If the message was eventSubscriptions, we can move to the next stage
        if "eventSubscriptions" in data and stage == 1:
            stage += 1
        else:
            # If the message is from a heartbeat event, we can extract the heart rate
            if data.get("op") == 6:
                requestId = data["d"]["requestId"]
                requestType = data["d"]["requestType"]
                
                if requestType == "SetInputSettings":
                    try:
                        heartrate = int(data["d"]["requestData"]["inputSettings"]["text"])
                        await aprint(f"Latest heart rate: {heartrate}")
                    except Exception as e:
                        print(f"Caught exception: {e}")
                        
        # If there is more than one client, and the heart rate has changed, then send the heart rate to the other clients
        if clients.__len__() > 1 and lastHeartrate != heartrate:
            for client in clients:
                if client != websocket:
                    try:
                        await client.send(str(heartrate))
                    except Exception as e:
                        print(f"Caught exception: {e}")

            await aprint(f"Message: {message} \n Clients list: {clients}")

async def onOpen(websocket):
    global connected, stage
    print("Connection opened.")
    clients.add(websocket)
    connected = True
    stage = 0

async def onClose():
    global connected
    print("Socket closed")
    connected = False

async def websocketServer(websocket, _):
    await onOpen(websocket)
    try:
        # Create two tasks, one for reading messages and one for writing messages
        consumer_task = asyncio.ensure_future(onMessage(websocket))
        producer_task = asyncio.ensure_future(hello_and_identify(websocket))

        # Wait for either task to finish, then cancel the other one
        done, pending = await asyncio.wait(
            [consumer_task, producer_task],
            return_when=asyncio.FIRST_COMPLETED,
        )

        for task in pending:
            task.cancel()
    except Exception as e:
        print(f"Caught exception: {e}")
    finally:
        await onClose()

async def main():
    async with websockets.serve(websocketServer, IP, port):
        print("Server started.")
        await asyncio.Event().wait() 
    
    

if __name__ == "__main__":
    asyncio.run(main())