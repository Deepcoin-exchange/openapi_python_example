# -*- coding:utf-8 -*-
"""
# Author: Rocky Zhao
# Time: 2025/2/20 21:29
"""
import websocket
import json
import time
import threading

ws_url = "wss://stream.deepcoin.com/public/ws"

def on_message(ws, message):
    print(f"Received: {message}")


def on_error(ws, error):
    print(f"Error: {error}")


def on_close(ws, close_status_code, close_msg):
    print("WebSocket closed")


def on_open(ws):
    print("WebSocket connected")


    def send_heartbeat():
        while True:
            ws.send("ping")
            print("Sent: ping")
            time.sleep(30)

    threading.Thread(target=send_heartbeat, daemon=True).start()

    request_data = {
        "SendTopicAction": {
            "Action": "1",
            "FilterValue": "DeepCoin_BTCUSDT_1m",
            "LocalNo": 6,
            "ResumeNo": -1,
            "TopicID": "11"
            }
    }
    ws.send(json.dumps(request_data))
    print(f"Sent: {json.dumps(request_data)}")


ws = websocket.WebSocketApp(
    ws_url,
    on_open=on_open,
    on_message=on_message,
    on_error=on_error,
    on_close=on_close,
)

ws.run_forever()