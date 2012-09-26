# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 8
_modified_time = 1348625407.39
_enable_loop = True
_template_filename = 'E:\\workspacePY\\let\\src/views/account/login.html'
_template_uri = '/account/login.html'
_source_encoding = 'utf-8'
from views.filters import Filters, Cycler
_exports = ['body']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'/layouts/base.html', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer(u'\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_body(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        next = context.get('next', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 5
        __M_writer(u'\n\t<style type="text/css">\n\t\tbody{background:#231815;/*url(/static/images/bg.jpg);*/ color:#997e54; overflow:hidden; }\n\t\t.row{float:none; clear:both; zoom:1;}\n\t\t.divider{border-bottom:3px dotted #997e54; margin:5px 0;}\n\t</style>\n\t\n\t<form action="/login" method="post"> \n\t\t<input type="hidden" name="next" value="')
        # SOURCE LINE 13
        __M_writer(unicode(next))
        __M_writer(u'" />\n\t\t<div style="margin-left:auto; margin-right:auto; width:443px; height:238px; margin-top:150px; text-align:center;">\n\t\t\t<div class="row">\n\t\t\t\t<img src="http://www.jztec.cn/Images/logo.gif" alt="logo" style="border:0; display:inline-block; " />\n\t\t\t\t<div class="pull-left" style="display:inline-block; vertical-align:middle; ">\u541b\u4f17\u7f51\u7edc\u7ba1\u7406\u7cfb\u7edf<br />\n\t\t\t\t\t<small style="font-size:10px;">version 1.0.0 beta</small>\n\t\t\t\t</div>\n\t\t\t</div>\n\t\t\t<div class="row divider"></div>\n\t\t\t<div class="row">\n\t\t\t\t\n\t\t\t\t<div style="float:left; text-align:left;  width:290px;">\n\t\t\t\t\t<input type="text" id="username" name="username" style="border:0; none; background:url(/static/images/input.png) no-repeat; width:198px; height:35px; padding-left:80px; color:white; margin:5px 0;" />\n\t\t\t\t\t<input type="password" id="password" name="password" style="border:0; none; background:url(/static/images/input_pw.png) no-repeat; width:198px; height:35px; padding-left:80px; color:white;margin:5px 0;" />\n\t\t\t\t\t<div class="field">\n\t\t\t\t\t\t<label for="keep_logged_in"><input type="checkbox" name="keep_logged_in" id="keep_logged_in" /> keep me logged in</label>\n\t\t\t\t\t</div> \t\t\t\t\t\n\t\t\t\t</div>\n\t\t\t\t<div style="float:left; vertical-align:middle; padding:30px 0;">\n\t\t\t\t\t<input type="image" src="/static/images/button.png" value="Login" style="width:115px; height:30px;" />\n\t\t\t\t</div>\n\t\t\t</div>\n\t\t</div>\n\t</form>\n\t\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


