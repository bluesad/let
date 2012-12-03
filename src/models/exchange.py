'''
Created on 2012-11-28

@author: huangchong
'''
'''
Created on 2012-9-12

@author: huangchong
'''
from mongokit import Document
import datetime
from db.mongo import Mongo
import uuid
  
@Mongo.db.connection.register
class Exchange(Document):   
     
    use_dot_notation = True
     
    structure = {
                 '_id':unicode,
                 'ename':basestring,
                 'oname':basestring,
                 'ipAddress':basestring,
                 'create_at':datetime.datetime
                 }
    
    @staticmethod  
    def lookup(e_id):
        return Mongo.db.ui.exchanges.find_one({'_id' : e_id})
    
    @staticmethod  
    def get_exchanges(oname):
        return [u for u in Mongo.db.ui.exchanges.find({'oname' : oname})] 
    
    
    @staticmethod
    def insert(ename,oname,ipAddress):
        c = Exchange.instance(ename,oname,ipAddress,datetime.datetime.now())
        return Mongo.db.ui['exchanges'].insert(c)
         
    '''
    creates a new tool instance. unsaved
    '''
    @staticmethod
    def instance(ename,oname,ipAddress,create_at):
        c = Exchange()
        c['_id'] = uuid.uuid1()
        c.ename = ename  
        c.oname = oname
        c.ipAddress = ipAddress
        c.create_at = create_at  
        return c