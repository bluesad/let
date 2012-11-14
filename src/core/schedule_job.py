'''
Created on 2012-11-8

@author: huangchong
'''
import datetime
from client.rpc_client import TelnetRpcClient
from apscheduler.scheduler import Scheduler
import json
import logging
'''
    Singleton
'''
logging.basicConfig()
  
schedudler = Scheduler(daemonic = False) 

@schedudler.cron_schedule(minute='00,30')
def set_bandwidth_job():
    print " [x] Requesting"
    rpc = TelnetRpcClient('211.147.71.42')
    print " [x] Requesting from rpc"
    response = rpc.call(json.dumps({'switch_name':'TelnetManage3560', 
                            "port_name":"e1/0/1", "host":"211.147.71.41", "bandwidth":2}))
    print " [.] Got %r" % (response,)
    print 'set_bandwidth_job start at ', datetime.datetime.now()

@schedudler.cron_schedule(minute='30')
def setback_bandwidth_job():
    rpc = TelnetRpcClient('211.147.71.42')
    print " [x] Requesting from rpc"
    response = rpc.call(json.dumps({'switch_name':'TelnetManage3560', 
                            "port_name":"e1/0/1", "host":"211.147.71.41", "bandwidth":2}))
    print " [.] Got %r" % (response,)
    print 'setback_bandwidth_job start at ', datetime.datetime.now()

    
schedudler.start()  

