'''
Created on 2012-8-28

@author: zongzong
'''
from core.basehandler import BaseHandler
from tornado.web import authenticated
from views.decorators import route
from views.decorators import role_required
from models.user import User
from models.exchange import Exchange
from client.rpc_client import TelnetRpcClient
from tornado.options import options 
import json

@route('/get_users')
class OperatersHandler(BaseHandler):

    @authenticated
    @role_required('/get_operaters')
    def post(self): 
        template_values = {}
        template_values['users'] = User.getUsers(2)
        template_values['usertype']=2
        self.render_template('/site/users.html', **template_values)

    @authenticated
    @role_required('/get_users')
    def get(self):
        template_values = {}
        template_values['users'] = User.getUsers(2)  
        template_values['usertype']=2
        self.render_template('/site/users.html', **template_values)
        
@route('/get_administrators')
class AdministratorsHandler(BaseHandler):

    @authenticated
    @role_required('/get_admin')
    def post(self):
        template_values = {}
        template_values['users'] = User.getUsers(1)
        template_values['usertype']=1
        self.render_template('/site/users.html', **template_values)

    @authenticated
    @role_required('/get_admin')
    def get(self):
        template_values = {}
        template_values['users'] = User.getUsers(1)
        template_values['usertype']=1
        self.render_template('/site/users.html', **template_values)

@route('/telnet_key')
class TelnetKeyHandler(BaseHandler):
    
    @authenticated
#   @role_required('/telnetkey')
    def get(self):  
        template_values = {}
        template_values['next'] = self.get_argument('next', '/')
        self.render_template('/account/telnetkey.html', **template_values)
    
    @authenticated
#   @role_required('/telnetkey')
    def post(self):          
        self.flash.success = "Successfully updated password"
        self.redirect('/login')     
        
@route('/add_exchange')
class AddExchangeHandler(BaseHandler):
    
    @authenticated
    def get(self):
        template_values = {}
        template_values['next'] = self.get_argument('next', '/')
        self.render_template('/site/exchange.html', **template_values)
    
    @authenticated
    def post(self):  
        oname = self.get_username()
        ipAddress = self.get_argument("ipAddress", None)
        ename = self.get_argument("ename", None)
        tusername = self.get_argument("tusername", None)
        tpassword = self.get_argument("tpassword", None)
        rpc = TelnetRpcClient(options.service_ip)
        Exchange.insert(ename,oname,ipAddress)
        response = rpc.call("key_queue",json.dumps({'fileadd':options.telnet_key_dir,'ipadd':ipAddress,'username':tusername,"password":tpassword}))
        self.redirect("/manage")     
        
        
        
        