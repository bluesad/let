'''
Created on 2012-8-28

@author: zongzong
'''
from core.basehandler import BaseHandler
from db.mongo import Mongo
import datetime, hashlib
from tornado.web import authenticated
from views.decorators import route
from views.decorators import role_required
from models.product import Product
from models.bandwidth import Bandwidth
from views.paginator import Paginator
import json  
import client.henlian as henlian
  
  
@route('/product')
class ProductHandler(BaseHandler):

    @authenticated
    @role_required('/product')
    def get(self):
        user = self.get_username()
        products = Product.getProduct(user)
        
        #page info
        page = self.get_argument('page', 1)
        page = page if page >= 1 else 1  
        #get the document count param
        count = self.get_argument('count', 5)
        count = count if count >= 1 else 5
        paginator = Paginator(products, page, count, len(products))
        
        template_values = {}
        template_values['paginator'] = paginator
        self.render_template('/site/product.html', **template_values)
        
        
        
        
@route('/bandwidth')
class BandwidthHandler(BaseHandler):
    
    def get(self):
        template_values = {}
        p_id = self.get_argument('p_id', '')
        product = Product.lookup(p_id)
        template_values['p_id'] = product['_id'] 
        template_values['yname'] = product['yname']
        template_values['cname'] = product['cname'] 
        template_values['next'] = self.get_argument('next', '/')     
        self.render_template('/site/bandwidth.html', **template_values)

        
    def post(self):
        cname = self.get_argument("cname", None)
        yname = self.get_argument("yname", None)
        percent = self.get_argument("percent", None)
        begin_at = self.get_argument("begin_at", None)
        suspended_at = self.get_argument("suspended_at", None)
        p_id = self.get_argument("p_id", None)
        Bandwidth.insert(cname,yname,p_id,percent,begin_at,suspended_at)
        
        if yname == '':
             henlian.control_bandwidth(host, port, user, password, id, bandwidth)
     
        self.finish("finished<script>parent.closeDialog();</script>")  
        
         
@route('/bandwidthlog')
class BwLogHandler(BaseHandler):
    
    def get(self):
        template_values = {}
        p_id = self.get_argument("p_id", None)
        bandwidths = Bandwidth.getBwLogs(p_id)
        print json.dumps(bandwidths)  
        self.finish(json.dumps(bandwidths))  
      
        
    def post(self):
        template_values = {}
        p_id = self.get_argument("p_id", None)
        bandwidths = Bandwidth.getBwLogs(p_id)
        print json.dumps(bandwidths)  
        self.finish(json.dumps(bandwidths))  
