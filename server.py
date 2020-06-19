import socket
import sys


def create_soket():
    try:
        global host
        global port
        global s
        host = ""
        port = 9999
        s = socket.socket()
    except socket.error as message:
        print("\n[ Error ] Error creating the socket : " + str(message))


def bind_socket():
    try:
        global host
        global port
        global s
        print("[ info ] Binding the port : " + str(port))
        s.bind((host, port))
        s.listen(5)
    except socket.error as message:
        print("[ Error ] Error binding the socket : " +
              str(message) + "\n[ + ] Retring...")
        # bind_socket()


def socket_accept():
    conn, address = s.accept()
    print("\n[ + ] Successfullt Connected! : " +
          address[0] + ":" + str(address[1]))
    exec_command(conn)
    conn.close()


def exec_command(conn):
    while True:
        cmd = input()
        if input == "exit;":
            conn.close()
            s.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            response = str(conn.recv(1024), 'utf-8')
            print(response, end="")


def main():
    create_soket()
    bind_socket()
    socket_accept()


main()
