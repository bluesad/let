# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 8
_modified_time = 1347592952.39
_enable_loop = True
_template_filename = 'E:\\workspacePY\\let\\src/views/site/bandwidth.html'
_template_uri = '/site/bandwidth.html'
_source_encoding = 'utf-8'
from views.filters import Filters, Cycler
_exports = ['body']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer(u'<style>\r\n.ui-timepicker-div .ui-widget-header { margin-bottom: 8px; }\r\n.ui-timepicker-div dl { text-align: left; }\r\n.ui-timepicker-div dl dt { height: 25px; margin-bottom: -25px; }\r\n.ui-timepicker-div dl dd { margin: 0 10px 10px 65px; }\r\n.ui-timepicker-div td { font-size: 90%; }\r\n.ui-tpicker-grid-label { background: none; border: none; margin: 0; padding: 0; }\r\n</style>\r\n')
        # SOURCE LINE 46
        __M_writer(u' ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_body(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        cname = context.get('cname', UNDEFINED)
        p_id = context.get('p_id', UNDEFINED)
        yname = context.get('yname', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 10
        __M_writer(u'\r\n<div class="form" style="margin:0 auto 0 auto;width: 300px;">\t\r\n<form action="/bandwidth" method="post" >\r\n\t<div class="field">\r\n\t\t<fieldset>\r\n\t\t    <input type="hidden" id="p_id" name="p_id" value="')
        # SOURCE LINE 15
        __M_writer(unicode(p_id))
        __M_writer(u'"  class="required"/>\t\r\n\t\t    <label for="cname" class="label">\u5ba2\u6237\u540d\u79f0:</label>\r\n\t\t     <input type="text" class="cname" name="cname" value="')
        # SOURCE LINE 17
        __M_writer(unicode(cname))
        __M_writer(u'" class="required"/>\t\r\n\t\t    <br>\r\n\t\t    <label for="yname" class="label">\u8fd0\u8425\u5546\u540d\u79f0:</label>\r\n\t\t     <input type="text" class="yname" name="yname" value="')
        # SOURCE LINE 20
        __M_writer(unicode(yname))
        __M_writer(u'" class="required"/>\t\r\n\t\t     <br>\r\n\t\t\t<label for="percent" class="label">\u589e\u52a0\u5e45\u5ea6:</label>\r\n\t\t\t<div class="select">\r\n\t\t\t\t<select id="percent" name="percent" class="required"/>\r\n\t\t\t\t      <option value=100>100</option>\r\n\t\t\t\t      <option value=50>50</option>\r\n\t\t\t\t      <option value=20>20</option>\r\n\t\t\t\t</select>%(\u5355\u4f4d\uff1a\u767e\u5206\u6bd4)\r\n\t\t\t</div>\t\r\n\t\t\t<label for="begin_at" class="label">\u5f00\u59cb\u65f6\u95f4:</label>\r\n\t\t\t<div class="input">\r\n\t\t\t\t <input type="datetime" class="datepicker_date" name="begin_at" class="required"/>\t\r\n\t\t\t</div>\r\n\t\t\t<label for="suspended_at" class="label">\u7ed3\u675f\u65f6\u95f4:</label>\r\n\t\t\t<div class="input">\r\n\t\t\t\t <input type="datetime" class="datepicker_date" name="suspended_at" class="required"/>\t\r\n\t\t\t</div>\r\n\t\t\t<div class="buttons">\r\n\t\t\t\t<input type="reset" class="button"/>\r\n\t\t\t\t<input type="submit" class="button" value="\u786e\u5b9a" />\r\n\t\t\t</div>\r\n\t\t</fieldset>\r\n\t</div>\r\n</form>\t\r\n</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


