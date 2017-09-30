import sys
import modules.matrix.ref
import modules.matrix.cfg
import logging

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


def main(host, username, password, room_id_alias):
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
    except MissingSchema as e:
        print("Bad URL format.")
        print(3)
        sys.exit(3)

    try:
        room = client.join_room(room_id_alias)
    except MatrixRequestError as e:
        print(e)
        if e.code == 400:
            print("Room ID/Alias in the wrong format")
            sys.exit(11)
        else:
            print("Could not find room.")
            sys.exit(12)

    room.add_listener(on_message)
    client.start_listener_thread()

    while True:
        msg = cogs.matrix.ref.get_input()
        if msg == "/quit":
            break
        else:
            room.send_text(msg)



def start_matrix():
    logging.basicConfig(level=logging.WARNING)
    host = cogs.matrix.cfg.matrix_host
    username = cogs.matrix.cfg.matrix_username
    password = cogs.matrix.cfg.matrix_password
    room_id_alias = cogs.matrix.cfg.matrix_room

    main(host, username, password, room_id_alias)


