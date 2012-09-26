'''
Created on 2012-9-12

@author: huangchong
'''
from mongokit import *
import datetime
import hashlib, hmac, base64, re
from db.mongo import Mongo
from tornado import options  
import uuid
  
@Mongo.db.connection.register
class Bandwidth(Document):  
    structure = {
                 '_id':unicode,
                 'p_id':unicode,
                 'cname':basestring,
                 'yname':basestring,
                 'percent':int,
                 'begin_at':datetime.datetime,
                 'suspended_at':datetime.datetime
                 }
    use_dot_notation = True

    @staticmethod
    def lookup(c_id):
        return Mongo.db.ui.bandwidths.find_one({'_id' : c_id})
    
    @staticmethod
    def getProducts(cname):
        return [u for u in Mongo.db.ui.bandwidths.find({'cname' : cname})]
    
    @staticmethod
    def getBwLogs(p_id):
        return {'users':[{'cname':u['cname'],'percent':u['percent'],'begin_at':u['begin_at']} for u in Mongo.db.ui.bandwidths.find({'p_id' : p_id})]}
    
    @staticmethod
    def insert(cname,yname,p_id,percent,begin_at,suspended_at):
        c = Bandwidth.instance(cname,yname,p_id,percent,begin_at,suspended_at)
        Mongo.db.ui['bandwidths'].insert(c)
        
  
        
    @staticmethod
    def delBandwidth(_cid, status):
        Mongo.db.ui['bandwidths'].remove({"_id":uuid.UUID(_cid)})
             
    '''
    creates a new tool instance. unsaved
    '''
    @staticmethod
    def instance(cname,yname,p_id,percent,begin_at,suspended_at):
        c = Bandwidth()
        c['_id'] = uuid.uuid1()
        c.cname = cname  
        c.yname = yname
        c.p_id = p_id #custormer's name 1 for alive / 0 for died
        c.percent = percent
        c.begin_at = begin_at
        c.suspended_at = suspended_at  
        return c