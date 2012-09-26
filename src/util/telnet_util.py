'''
Created on 2012-9-25

@author: huangchong
'''
import telnetlib


def telnet_login(host,port,user,password):
    tn = telnetlib.Telnet(host)
    if password:
        tn.read_until("Password:")
        tn.write(password + "\n")
    return tn

def do_something(tn,comm):
    tn.write(comm)


def end_telnet(tn):
    tn.write("exit\n")
