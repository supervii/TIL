import socket
import time
import math

# User and Game Server Information
NICKNAME = 'Shinjeong-woo'
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
    if gameData.balls[2] ==[0,0] and gameData.balls[3] ==[0,0] and gameData.balls[4] ==[0,0]:
        if gameData.balls[1] == [125, 120]:
            angle = 50
            power = 55
        elif gameData.balls[1] == [250, 10]:
            angle = 106
            power = 300
        elif gameData.balls[1] == [195, 65]:
            angle = 89
            power = 200
        elif gameData.balls[1] == [248, 45]:
            angle = 184
            power = 200
    elif gameData.balls[3] ==[0,0] and gameData.balls[4] ==[0,0]:
        if gameData.balls[1] == [250, 10]:
            angle = 106
            power = 300
        else:
            angle = 267
            power = 300
    elif gameData.balls[4] ==[0,0]:
        if gameData.balls[1] == [125, 120] :
            angle = 50
            power = 55
        elif gameData.balls[2] == [240, 124]:
            angle = 85
            power = 200
        elif gameData.balls[3] == [250, 10]:
            angle = 135
            power = 70
    else :
        if gameData.balls[1] == [195, 65]:
            angle = 89
            power = 200
        elif gameData.balls[1] == [248, 45]:
            angle = 184
            power = 200 
        elif gameData.balls[1] ==[0,0] and gameData.balls[2] ==[197, 33]:
                angle = 251
                power = 70
        elif gameData.balls[2] ==[135,6]:
                angle = 221
                power = 50
        elif gameData.balls[2] ==[0,0] and gameData.balls[3] == [234, 106]:
                angle = 45
                power = 200
        elif gameData.balls[3] ==[0,0] and gameData.balls[4] == [232, 70]:
                angle = 192
                power = 200
        elif gameData.balls[4] == [161, 95]:
                angle = 280
                power = 140   
        elif gameData.balls[4] == [9, 123]:
                angle = 290
                power = 60
    ######################################################################################
    # 주어진 정보를 바탕으로 샷을 할 방향과 세기를 결정해서 angle, power 값으로 지정 #
    ######################################################################################
    conn.send(angle, power)


def main():
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
