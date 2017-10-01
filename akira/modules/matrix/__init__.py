import sys
import re
import modules.matrix.matrix_cfg
import logging
import random
import time
from voice import tts

from matrix_client.client import MatrixClient
from matrix_client.api import MatrixRequestError
from requests.exceptions import MissingSchema


def on_message(room, event):
    if  event['type'] == "m.room.member":
        if event['membership'] == "join":
            print("{0} joined".format(event['content']['displayname']))
    elif event['type'] == "m.room.message":
        if event['content']['msgtype'] == 'm.text':
            print("{0}: {1}".format(event['sender'], event['content']['body']))
    else:
        print(event['type'])


def main(host, username, password, number, msg):
    number = number.replace('-', '')
    print("dbg:", host, username, password, number, msg)
    room_alias = f"akira{number}{random.randint(0, 10000)}"
    mxid_num = f"@+1{number}:matrix.openmarket.com"
    print("dbg:", room_alias, mxid_num)

    client = MatrixClient(host)

    try:
        client.login_with_password(username, password)
    except MatrixRequestError as e:
        print(e)
        if e.code == 403:
            print('Bad username or password.')
            sys.exit(4)
        else:
            print("Check your server details are correct.")
            sys.exit(2)
    except MissingSchema:
        print("Bad URL format.")
        print(3)
        sys.exit(3)

    try:
        room = client.create_room(room_alias, is_public=False)
        room.invite_user(mxid_num)
        time.sleep(10)
    except MatrixRequestError as e:
        print(e)
        if e.code == 400:
            print("Room ID/Alias in the wrong format")
            sys.exit(11)
        else:
            print("Could not find room.")
            print(e)
            sys.exit(12)

    room.add_listener(on_message)
    client.start_listener_thread()

    room.send_text(msg)


trigger_regex = re.compile('text (.+) to (.+)', re.IGNORECASE)


def run(matches):
    msg = matches.groups()[0]
    number = matches.groups()[1]
    logging.basicConfig(level=logging.WARNING)
    tts(f"Okay, sending {msg} to {number}. Please hold.")
    host = modules.matrix.matrix_cfg.cfg["matrix_host"]
    username = modules.matrix.matrix_cfg.cfg["matrix_username"]
    password = modules.matrix.matrix_cfg.cfg["matrix_password"]

    main(host, username, password, number, msg)
    tts("Message sent.")


