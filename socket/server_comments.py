#!/usr/bin/python
#coding: utf-8
import socket                                           #импортируем библиотеку 

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)  #создаем сокет, через AF_INET задем формат адреса для интернета
                                                        #SOCK_DGRAM используется для определния типа соединения как правило используется в UDP
                                                        #SOCK_STREAM используется для TCP
                                                              
sock.bind (('localhost', 12345))                        #присваеваем сокету - ip-адрес 
                                                        #(в данном случае нашего компьютера) и порт 

client = []                                             #создаем список, куда будем добавлять подключенные клиенты
print('Start Server')                                   #печаем приветствие 

while True:                                             #запускаем на сервере бесконечный цикл
     data , addres = sock.recvfrom(1024)                #сохраняем в переменную data - переданные данные. 
                                                        #в переменную addres - ip и порт с которого получили данные
     
     print (addres[0], addres[1])                       #распечатываем переменную addres

     if addres not in client:                           #проверка условия - если переменная addres не в списке, то добавляем ее
             client.append(addres)                      #добавление переменной addres в список clients
     for clients in client:                             #проходим циклом по списку
             if clients == addres:                      #проверка условия, если элемент списка равен addres то просто идем на следующий проход
                 continue
             sock.sendto(data,clients)                  #если элемент списка не равен addres, то делаем отправку