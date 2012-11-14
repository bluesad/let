# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 8
_modified_time = 1351654563.359
_enable_loop = True
_template_filename = 'E:\\workspacePY\\sod\\src/views/site/custorm_add.html'
_template_uri = '/site/custorm_add.html'
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
    return runtime._inherit_from(context, u'/layouts/content.html', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer(u'\r\n<style>\r\n.ui-timepicker-div .ui-widget-header { margin-bottom: 8px; }\r\n.ui-timepicker-div dl { text-align: left; }\r\n.ui-timepicker-div dl dt { height: 25px; margin-bottom: -25px; }\r\n.ui-timepicker-div dl dd { margin: 0 10px 10px 65px; }\r\n.ui-timepicker-div td { font-size: 90%; }\r\n.ui-tpicker-grid-label { background: none; border: none; margin: 0; padding: 0; }\r\n</style>\r\n')
        # SOURCE LINE 104
        __M_writer(u'\r\n<a href="http://www.jztech.cn" target="new">\u66f4\u591a\u6280\u672f\u652f\u6301\uff0c\u6b22\u8fce\u8bbf\u95ee\u541b\u4f17\u79d1\u6280\u516c\u53f8\u7f51\u7ad9\uff01</a>   ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_body(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 11
        __M_writer(u'\r\n<script type="text/javascript">\r\n$(\'#fileTab\').tabs({\r\n\t\tajaxOptions: {\r\n\t\t\terror: function( xhr, status, index, anchor ) {\r\n\t\t\t\t$( anchor.hash ).html("\u8be5\u9875\u65e0\u6cd5\u663e\u793a\uff0c\u6ca1\u6cd5\u534e\u4e3d\u626f\u6de1\uff01" );\r\n\t\t\t}\r\n\t\t},\r\n\t\tselect:function(obj,tab){\t\t\r\n\t\t\tvar subWeb = document.frames ? document.frames[tab.panel.id].document : document.getElementById(tab.panel.id).contentDocument;\r\n\t\t\tswitch(tab.panel.id)\r\n\t\t\t{\r\n\t\t\tcase "thisMonth":$(tab.panel).find(\'iframe\').attr(\'src\',\'/manage\');/*$(tab.panel).find(\'iframe\').attr("height",subWeb.body.scrollHeight);*/break;\r\n\t\t\tdefault:$(tab.panel).find(\'iframe\').attr(\'src\',\'\');break;\r\n\t\t\t}\t\t\r\n\t\t}\r\n\t});\r\n</script>\r\n<div id="page-header">\r\n\t<div class="title">\r\n\t\t\u6dfb\u52a0\u7528\u6237\u754c\u9762\r\n\t</div>\r\n\t<div class="subtitle">\r\n\t    \u7528\u6237\u4e0e\u4ea7\u54c1\u4fe1\u606f\r\n\t</div>\r\n</div>\n<div class="form" style="margin:0 auto 0 auto;width: 300px;">\n<form action="/custorm_add" method="post" >\r\n\t<div class="field">\r\n\t\t<fieldset>\r\n\t\t\t<label for="cname" class="label">\u5ba2\u6237\u540d\u79f0:</label>\r\n\t\t\t<div class="input">\r\n\t\t\t\t<input type="text" id="cname" name="cname" class="required"/>\r\n\t\t\t</div>\t\r\n\t\t\t<label for="address" class="label">\u5730\u5740:</label>\r\n\t\t\t<div class="input">\r\n\t\t\t\t<input type="text" id="address" name="address" class="required"/>\r\n\t\t\t</div>\r\n\t\t\t<label for="phonenum" class="label">\u8054\u7cfb\u7535\u8bdd:</label>\r\n\t\t\t<div class="input">\r\n\t\t\t\t<input type="text" id="phonenum" name="phonenum" class="required integer"/>\r\n\t\t\t</div>\r\n\t\t\t<label for="device" class="label">\u8bbe\u5907\u7c7b\u578b:</label>\r\n\t\t\t<div class="select">  \r\n\t\t\t\t  <select id="device" name="device" class="required">\r\n\t\t\t\t      <option value=\'211.147.81.50\' >Cisco 3560</option>\r\n\t\t\t\t\t  <option value=\'211.147.81.50\' >H3C</option>\r\n\t\t\t\t  <select/>\r\n\t\t\t</div>\r\n\t\t\t<label for="port" class="label">\u5bf9\u5e94\u7aef\u53e3:</label>\r\n\t\t\t<div class="input">  \r\n\t\t\t\t  <input type="text" id="port" name="port" class="required"/>\r\n\t\t\t</div>\r\n\t\t\t<label for="type" class="label">\u4ea7\u54c1\u5e26\u5bbd:</label>\r\n\t\t\t<div class="input">\r\n\t\t\t\t<input type="text" id="type" name="type" class="required integer"/>M(\u5355\u4f4d\uff1a\u5146)\r\n\t\t\t</div>\r\n\t\t\t<label for="continue_to" class="label">\u53ef\u7528\u65f6\u95f4\uff1a</label>\r\n\t\t\t<div class="input">\r\n\t\t\t\t<input type="text" id="continue_to" name="continue_to" class="required integer"/>h(\u5355\u4f4d\uff1a\u5c0f\u65f6)\r\n\t\t\t</div>\r\n\t\t\t<!--<label for="begin_ip" class="label">\u5f00\u59cbip:(\u683c\u5f0f***.***.***.***)</label>  \r\n\t\t\t<div class="input">  \r\n\t\t\t\t <input type="text" id="begin_ip" name="begin_ip" class="required 2ip"/>  \r\n\t\t\t</div>\r\n\t\t\t<label for="suspended_ip" class="label">\u7ed3\u675fip:(\u683c\u5f0f***.***.***.***)</label>\r\n\t\t\t<div class="input">  \r\n\t\t\t\t  <input type="text" id="suspended_ip" name="suspended_ip" class="required 2ip"/>\r\n\t\t\t</div>-->\r\n\t\t\t<label for="begin_at" class="label">\u5f00\u59cb\u65f6\u95f4:</label>  \r\n\t\t\t<div class="input">\r\n\t\t\t\t <input type="datetime" class="datepicker_date" name="begin_at" class="required"/>\t\r\n\t\t\t</div>\r\n\t\t\t<label for="suspended_at" class="label">\u8fc7\u671f\u65f6\u95f4:</label> \r\n\t\t\t<div class="input">\r\n\t\t\t\t <input type="datetime" class="datepicker_date" name="suspended_at" class="required"/>\t\r\n\t\t\t</div>\t\r\n\t\t\t<label for="price" class="label">\u4ef7\u683c:</label>\r\n\t\t\t<div class="input">\r\n\t\t\t\t<input type="text" id="price" name="price" class="required integer"/>Y(\u5355\u4f4d\uff1a\u5143)\r\n\t\t\t</div>\r\n\t\t\t<div class="buttons">\r\n\t\t\t\t<input type="reset" class="button"/>\r\n\t\t\t\t<input type="submit" class="button" value="\u6dfb\u52a0"/>   \r\n\t\t\t</div>\r\n\t\t</fieldset>\r\n\t</div>\r\n</form>\r\n</div>\t\t\t\t\r\n<div class="tab-footer clear">\r\n\t   <div class="pager fr">\r\n       </div>\r\n</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


