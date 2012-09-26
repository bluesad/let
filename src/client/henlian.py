'''
Created on 2012-9-24

@author: huangchong
'''
import util.telnet_util as util

def control_bandwidth(host,port,user,password,id,bandwidth):
    tn = util.telnet_login(host,port,user,password)
    util.do_something(tn, 'sys')
    comm = 'vlan '+id
    util.do_something(tn, comm)
    comm = 'undo traffic-policy inbound'
    util.do_something(tn, comm)
    comm = 'traffic-policy '+bandwidth+'M inbound'
    util.do_something(tn, comm)
    comm ='undo traffic-policy outbound'
    util.do_something(tn, comm)
    comm = 'traffic-policy '+bandwidth+'M outbound'
    util.do_something(tn, comm)
    util.end_telnet(tn)
