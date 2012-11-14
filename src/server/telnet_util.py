'''
Created on 2012-9-25

@author: huangchong
'''
import telnetlib
import time

class TelnetManage:
    def __init__(self, host, port_name, username, password):
        self.host = host
        self.username = username
        self.password = password
        self.port_name = port_name
        print 'telnet name: %s ', self.name
        
    def set_bandwidth(self, host, username, password):
        print 'bandwidth: %s' % (username)
        self.tn = telnet_login(host, username, password)

class TelnetManage3560(TelnetManage):
    def __init__(self, host, port_name, username, password, bandwidth):
        TelnetManage.__init__(self, host, port_name, None, password)
        self.bandwidth = bandwidth
        print 'TelnetManage3560: ', self.host

    def set_bandwidth(self):
        TelnetManage.set_bandwidth(self, self.host , self.username, self.password)
        do_something(self.tn, 'en')
        if self.password:
            self.tn.read_until("Password:")
            self.tn.write(self.password + "\n")      
        bwvalue = 100 / self.bandwidth
        ex_bandwidth = 0
        do_something(self.tn, 'conf t')
        do_something(self.tn, 'interface FastEthernet%s' % self.port_name)
        do_something(self.tn, str('no service-policy input %sM' % ex_bandwidth))
        do_something(self.tn, 'service-policy input %sM ' % self.bandwidth)
        do_something(self.tn, 'srr-queue bandwidth shape %s %s %s %s' % (bwvalue, bwvalue, bwvalue, bwvalue))
        do_something(self.tn, 'end')
        print 'end'
        end_telnet(self.tn)
        print self.tn.read_all()
        print 'bandwidth: s% ' % self.now_bandwidth

class TelnetManage3600(TelnetManage):
    def __init__(self, host, port_name, username, password, bandwidth):
        TelnetManage.__init__(self, host, port_name, username, password)
        self.inbound = bandwidth * 1024
        self.outbound = bandwidth * 1024  
        print 'TelnetManage3600: ', self.host

    def set_bandwidth(self):
        TelnetManage.set_bandwidth(self, self.host , self.username, self.password)
        do_something(self.tn, 'system')
        time.sleep(2)
        do_something(self.tn, 'interface ', self.port_name)
        time.sleep(1)
        do_something(self.tn, 'line-rate inbound ', self.inbound)
        time.sleep(1)
        do_something(self.tn, 'line-rate outbound ', self.outbound)
        end_telnet(self.tn)
        print 'bandwidth: ', self.inbound  


def telnet_login(host, username, password):
    tn = telnetlib.Telnet(host)
    if username:
        tn.read_until("Username:")
        tn.write(username + "\n")
    if password:
        tn.read_until("Password:")
        tn.write(password + "\n")
    return tn

def do_something(tn, comm):
    tn.write(comm + '\n')

def end_telnet(tn):
    tn.write("exit\n")
  


