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
from models.user import User
from views.paginator import Paginator
  
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
        template_values['p_id'] = self.get_argument('p_id', '')
        template_values['yname'] = self.get_argument('yname', '')
        template_values['cname'] = self.get_argument('cname', '')
        template_values['next'] = self.get_argument('next', '/')     
        self.render_template('/site/bandwidth.html', **template_values)
        
        
    def post(self):
        cname = self.get_username()
        yname = self.get_argument("yname", None)
        percent = self.get_argument("percent", None)
        begin_at = self.get_argument("begin_at", None)
        suspended_at = self.get_argument("suspended_at", None)
        self.finish("finished")
        
