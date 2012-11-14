# -*- coding: utf-8 -*-
import pika
import json
from file_util import read
import socket
import sys

key_file = sys.argv[1]

localIP = socket.gethostbyname(socket.gethostname())

connection = pika.BlockingConnection(pika.ConnectionParameters(
        localIP))
  
channel = connection.channel()
channel.queue_declare(queue='rpc_queue')

def do_command(switch_name, host, port_name, username, password, bandwidth):
    tm = switch_name(host, port_name, username, password, bandwidth)
    tm.set_bandwidth()
    return {'response_code':'250'}
    
def on_request(ch, method, props, body): 
    try:
        if read(key_file):
            username, password = json.loads(read(key_file))[localIP]#here is the switch address 
            keys = json.loads(body) 
            switch_name = keys['switch_name']
            print " received from %s" % (switch_name,)
            port_name = keys['port_name']
            host = keys['host']
            bandwidth = keys['bandwidth']
            response = do_command(switch_name, host, port_name, username, password, bandwidth)
            print "拯救地球 !!!"
        else:
            response = {'response_code':'4587'} 
    except:
            response = {'response_code':'4587'}
    ch.basic_publish(exchange='',  
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(correlation_id=\
                                                         props.correlation_id),
                     body=str(response))
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(on_request, queue='rpc_queue')

print " [x] Awaiting RPC requests"
channel.start_consuming()
