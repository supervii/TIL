import socket
import time
import math

# User and Game Server Information
NICKNAME = 'Namsh'
HOST = '127.0.0.1'
PORT = 1447 # Do not modify

# predefined variables(Do not modify these values)
TABLE_WIDTH = 254
TABLE_HEIGHT = 124
NUMBER_OF_BALLS = 5
HOLES = [ [0, 0], [130, 0], [260, 0], [0, 130], [130, 130], [260, 130] ]

class Conn:
    def __init__(self):
        self.sock = socket.socket()
        print('Trying to Connect: ' + HOST + ':' + str(PORT))
        self.sock.connect((HOST, PORT))
        print('Connected: ' + HOST + ':' + str(PORT))
        send_data = '9901/' + NICKNAME
        self.sock.send(send_data.encode('utf-8'))
        print('Ready to play.\n--------------------')
    def request(self):
        self.sock.send('9902/9902'.encode())
        print('Received Data has been currupted, Resend Requested.')
    def receive(self):
        recv_data = (self.sock.recv(1024)).decode()
        print('Data Received: ' + recv_data)
        return recv_data
    def send(self, angle, power):
        merged_data = '%d/%d' % (angle, power)
        self.sock.send(merged_data.encode('utf-8'))
        print('Data Sent: ' + merged_data)
    def close(self):
        self.sock.close()

class GameData:
    def __init__(self):
        self.reset()
    def reset(self):
        self.balls = [[0, 0] for i in range(NUMBER_OF_BALLS)]
    def read(self, conn):
        recv_data = conn.receive()
        split_data = recv_data.split('/')
        idx = 0    
        try:
            for i in range(NUMBER_OF_BALLS):
                for j in range(2):
                    self.balls[i][j] = int(split_data[idx])
                    idx += 1
        except:
            self.reset()
            conn.request()
            self.read(conn)
    def show(self):
        print('=== Arrays ===')
        for i in range(NUMBER_OF_BALLS):
            print('Ball%d: %d, %d' % (i, self.balls[i][0], self.balls[i][1]))
        print()

# 자신의 차례가 되어 게임을 진행해야 할 때 호출되는 Method
def play(conn, gameData):
    angle, power = 190, 100
    if gameData.balls[:3] == [[65, 65], [125, 120], [0, 0]]: angle, power = 50, 60
    elif gameData.balls[:3] == [[65, 65], [250, 10], [0, 0]]: angle, power = 105, 100
    elif gameData.balls[:3] == [[65, 65], [250, 10], [15, 10]]: angle, power = 105, 90
    elif gameData.balls[:3] == [[241, 23], [0, 0], [15, 10]]: angle, power = 268, 120
    elif gameData.balls[:3] == [[65, 65], [125, 120], [240, 124]]: angle, power = 50, 60
    elif gameData.balls[:3] == [[161, 124], [0, 0], [240, 124]]: angle, power = 93, 80
    elif gameData.balls[:3] == [[230, 75], [0, 0], [0, 0]]: angle, power = 165, 80
    elif gameData.balls[:3] == [[65, 65], [195, 65], [0, 0]]: angle, power = 89, 200
    elif gameData.balls[:3] == [[250, 86], [248, 45], [0, 0]]: angle, power = 190, 100
    elif gameData.balls[:3] == [[179, 22], [243, 11], [0, 0]]: angle, power = 100, 80
    elif gameData.balls[:3] == [[65, 65], [195, 65], [203, 57]]: angle, power = 89, 200
    elif gameData.balls[:3] == [[250, 86], [248, 45], [233, 19]]: angle, power = 190, 100
    elif gameData.balls[:3] == [[179, 22], [243, 11], [230, 26]]: angle, power = 100, 80
    elif gameData.balls[:3] == [[251, 16], [0, 0], [230, 26]]: angle, power = 290, 80
    elif gameData.balls[:3] == [[157, 26], [0, 0], [148, 79]]: angle, power = 353, 85
    elif gameData.balls[:3] == [[165, 116], [0, 0], [0, 0]]: angle, power = 110, 27
    elif gameData.balls[:3] == [[221, 95], [0, 0], [0, 0]]: angle, power = 60, 70
    elif gameData.balls[:3] == [[229, 109], [0, 0], [0, 0]]:angle, power = 140, 17
    elif gameData.balls[:3] == [[252, 82], [0, 0], [0, 0]]: angle, power = 229, 300
    conn.send(angle, power)

def main():
    global cnt
    conn = Conn()
    gameData = GameData()

    while True:
        gameData.read(conn)
        gameData.show()
        if gameData.balls[0][0] == 9909:
            break
        play(conn, gameData)
    conn.close()
    print('Connection Closed')

if __name__ == '__main__':
    main()
