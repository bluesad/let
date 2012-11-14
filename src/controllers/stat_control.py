'''
Created on 2012-10-17

@author: huangchong
'''
from core.basehandler import BaseHandler
from views.decorators import route 
from models.order import Order
from views.paginator import Paginator
       
@route('/bwstat')
class BwStatHandler(BaseHandler):  
    
    def get(self):
        p_id = self.get_current_user()['_id']
        print p_id
        bandwidths = Order.get_orders(p_id)
        #page info
        page = self.get_argument('page', 1)
        page = page if page >= 1 else 1  
        #get the document count param
        count = self.get_argument('count', 5)
        count = count if count >= 1 else 5
        paginator = Paginator(bandwidths, page, count, len(bandwidths))
        template_values={}
        template_values['paginator'] = paginator
        self.render_template('/site/stat_bw.html', **template_values)
      
    def post(self):
        p_id = self.get_current_user()
        print p_id
        bandwidths = Order.get_orders(p_id)
        #page info
        page = self.get_argument('page', 1)
        page = page if page >= 1 else 1  
        #get the document count param
        count = self.get_argument('count', 5)  
        count = count if count >= 1 else 5
        paginator = Paginator(bandwidths, page, count, len(bandwidths))
        template_values={}
        template_values['paginator'] = paginator
        self.render_template('/site/stat_bw.html', **template_values)