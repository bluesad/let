# -*- coding: utf-8 -*-
'''
Created on 2012-11-12

@author: huangchong
'''
import os.path

# for read file
def read(file_name):
    path, = os.path.split(file_name)
    if not os.path.exists(path):  
        os.mkdir(path)          
    if not os.path.exists(file_name):  
        mkfile(file_name)               
    with open(file_name) as f:
        return f.readline()
    
# for write file
def write(arg,file_path,file_name):
    if not os.path.exists(file_path):  
        os.mkdir(file_path)                 
    with open(file_path+file_name,"wt") as f:
        f.write(arg)

def mkfile(filename, body=None):
    with open(filename, 'w' ) as f:
        f.write(body)
    return  

'''demo for telnet'''
#if read('e:/aa/huangchong.txt'):
#    b = json.loads(read('e:/aa/huangchong.txt'))
#b['192.168.0.3']=[u'admin7', u'admin8']  
#write(json.dumps(b),'e:/aa/','huangchong.txt')
#a,c = json.loads(read('e:/aa/huangchong.txt'))['192.168.0.5']

#try:
#  if read('e:/aa/','huangchong2.txt'):
#      username,password = json.loads(read('e:/aa/','huangchong.txt'))['192.168.0.5']
#else:  
#        response = "username or password error!!!"    
#   
#print response 
    
    
    