import socket
import sys
import time

serversocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host=socket.gethostname()#获取本地主机名
port=9999
#绑定端口号
serversocket.bind((host,port))

#设置最大连接数
serversocket.listen(5)
while True:
    print('服务器启动，监听客户端链接')
    clientsocket,addr=serversocket.accept()
    print('链接地址：%s' % str(addr))
    while True:
        try:
            data=clientsocket.recv(1024)
        except Exception:
            print('断开的客户端：',addr)
            break
        print('客户端发送内容：',data.decode('utf-8'))
        reply=input('回复：').strip()
        if not reply:
            break
        msg=time.strftime('%Y-%m-%d %X')#获取结构化时间戳
        msg1='[%s]:%s'% (msg,reply)
        clientsocket.send(msg1.encode('utf-8'))
    clientsocket.close()
serversocket.closel()