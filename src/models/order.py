'''
Created on 2012-9-12

@author: huangchong
'''
from mongokit import Document
import datetime
from db.mongo import Mongo
import uuid
  
@Mongo.db.connection.register
class Order(Document):    
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
        return Mongo.db.ui.orders.find_one({'_id' : c_id})
    
    @staticmethod
    def get_orders_operators(yname):
        return [u for u in Mongo.db.ui.orders.find({'yname' : yname})]
    
    @staticmethod
    def get_orders(p_id):
        return {'users':[{'cname':u['cname'],'percent':u['percent'],'begin_at':u['begin_at'],'suspended_at':u['suspended_at']} for u in Mongo.db.ui.orders.find({'p_id' : p_id})]}
    
    @staticmethod
    def insert(cname,yname,p_id,percent,begin_at,suspended_at):
        c = Order.instance(cname,yname,p_id,percent,begin_at,suspended_at)
        return Mongo.db.ui['orders'].insert(c)
        
    @staticmethod
    def del_order(_cid, status):
        Mongo.db.ui['orders'].remove({"_id":uuid.UUID(_cid)})
             
    '''
    creates a new tool instance. unsaved
    '''
    @staticmethod
    def instance(cname,yname,p_id,percent,begin_at,suspended_at):
        c = Order()
        c['_id'] = uuid.uuid1()
        c.cname = cname  
        c.yname = yname
        c.p_id = p_id
        c.percent = percent
        c.begin_at = begin_at
        c.suspended_at = suspended_at  
        return c