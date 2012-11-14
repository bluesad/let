'''
Created on 2012-8-28

@author: zongzong
'''
from core.basehandler import BaseHandler
#import hashlib
from tornado.web import authenticated
from views.decorators import route
from views.decorators import role_required
from models.user import User


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
        
        
 
        
