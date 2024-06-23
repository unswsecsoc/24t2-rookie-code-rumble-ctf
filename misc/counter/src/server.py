import socket
import threading
import time

db = {}

def modify_variable(username, value):
    db[username] += value
    time.sleep(0.5)

def handle_user(conn, addr):
    print(f"User connected")

    conn.send(b"Please enter your username to log in:\n")
    uname = conn.recv(1024).decode().strip()
    if not uname in db:
        db[uname] = 0

    try:
        conn.send(b"A simple counter. You can use 'plus' or 'minus' to control it. It cannot go above 10\n")
        while True:
            data = conn.recv(1024).decode().strip()
            if not data:
                break
            if data == "plus":
                copy = db[uname]
                modify_variable(uname, 1)
            elif data == "minus":
                copy = db[uname]
                modify_variable(uname, -1)
            elif data == "quit":
                break
            else:
                conn.send(b"Invalid command\n")
                continue
            if db[uname] > 10:
                conn.send(b"Flag: BEGINNER{t00_qu1ck_5l0w_d0wn}\n")
                # Reset to prevent others getting the flag with same username
                db[uname] = 0
            elif db[uname] == 10:
                db[uname] = 0
            conn.send(f"Current is {db[uname]} was {copy}\n".encode())
    except Exception as e:
        print(f"whoops {e}")
    finally:
        print(f"User disconnected")
        conn.close()

def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 9999))
    server_socket.listen(5)
    print("Server listening on port 9999...")
    try:
        while True:
            try:
                conn, addr = server_socket.accept()
                thread = threading.Thread(target=handle_user, args=(conn, addr))
                thread.start()
            except Exception as e:
                print(f"whoops {e}")
    finally:
        server_socket.close()
        

server_thread = threading.Thread(target=server)
server_thread.start()