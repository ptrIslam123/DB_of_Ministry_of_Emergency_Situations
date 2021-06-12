#! /usr/bin/env python
#-*-coding: utf-8-*-

import socket


s = socket.socket()

host = socket.gethostname()
port = 12000

s.bind((host, port))

s.listen(5)

while True:
    
    try:
        client, addr = s.accept()

        while True:
            result = client.recv(1024)

            if result == "close":
                print("__destroy connect__")
                client.close()
                break
            print 'клиент: ',result

            client.send(result)

    except KeyboardInterrupt:
        print("__destroy_server__")
        s.close()
        break
        
    
    

    

    
        


'''
result = c.recv(1024)
print 'клиент: ', result

c.send('и тебе привет мир')
'''