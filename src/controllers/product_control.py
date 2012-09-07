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
from models.customer import Custormer
from models.user import User
from views.paginator import Paginator
  
@route('/product')
class ProductHandler(BaseHandler):

    @authenticated
    @role_required('/product')
    def get(self):
        user = self.get_username()
        custormers = Custormer.getProducts(user)
        
        #page info
        page = self.get_argument('page',1)
        page = page if page >= 1 else 1  
        #get the document count param
        count = self.get_argument('count',2)
        count = count if count >= 1 else 2
        paginator = Paginator(custormers,page,count,len(custormers))
        
        template_values = {}
        template_values['paginator'] = paginator
        self.render_template('/site/product.html', **template_values)
