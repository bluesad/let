# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 8
_modified_time = 1351673654.671
_enable_loop = True
_template_filename = 'E:\\workspacePY\\sod\\src/views/site/bandwidth.html'
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
        __M_writer(u'<style>\r\n.ui-timepicker-div .ui-widget-header { margin-bottom: 8px; }\r\n.ui-timepicker-div dl { text-align: left; }\r\n.ui-timepicker-div dl dt { height: 25px; margin-bottom: -25px; }\r\n.ui-timepicker-div dl dd { margin: 0 10px 10px 65px; }\r\n.ui-timepicker-div td { font-size: 90%; }\r\n.ui-tpicker-grid-label { background: none; border: none; margin: 0; padding: 0; }\r\n</style>\r\n<link type="text/css" href="/static/css/jquery.ui.min.css" rel="stylesheet" />\r\n<link rel="stylesheet" media="all" type="text/css" href="/static/css/jquery-ui-timepicker-addon.css" />\r\n<script src="/static/js/jquery-1.7.1.min.js"></script>\r\n<script type="text/javascript" src="http://code.jquery.com/ui/1.8.21/jquery-ui.min.js"></script>\r\n<script src="/static/js/application.js?')
        # SOURCE LINE 14
        __M_writer(unicode(Filters.version()))
        __M_writer(u'"></script>\r\n<script type="text/javascript" src="/static/js/menu.js"></script>\r\n<script type="text/javascript" src="/static/js/jquery-ui-timepicker-addon.js"></script>\r\n<script type="text/javascript" src="/static/js/jquery-ui-sliderAccess.js"></script>\r\n')
        # SOURCE LINE 56
        __M_writer(u' ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_body(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        cname = context.get('cname', UNDEFINED)
        p_id = context.get('p_id', UNDEFINED)
        oname = context.get('oname', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 18
        __M_writer(u'\r\n<div class="form" style="margin:0 auto 0 auto;width: 300px;">\t\r\n<form action="/bandwidth" method="post" > \r\n\t<div class="field">\r\n\t\t<fieldset>\r\n\t\t    <input type="hidden" id="p_id" name="p_id" value="')
        # SOURCE LINE 23
        __M_writer(unicode(p_id))
        __M_writer(u'"  class="required"/>\r\n\t\t    <input type="hidden" id="cname" name="cname" value="')
        # SOURCE LINE 24
        __M_writer(unicode(cname))
        __M_writer(u'"  class="required"/>\r\n\t\t    <input type="hidden" id="oname" name="yname" value="')
        # SOURCE LINE 25
        __M_writer(unicode(oname))
        __M_writer(u'"  class="required"/>\r\n\t\t    <label for="cname" class="label">\u5ba2\u6237\u540d\u79f0:')
        # SOURCE LINE 26
        __M_writer(unicode(cname))
        __M_writer(u'</label>\r\n\t\t    <br>\r\n\t\t    <label for="oname" class="label">\u8fd0\u8425\u5546\u540d\u79f0:')
        # SOURCE LINE 28
        __M_writer(unicode(oname))
        __M_writer(u'</label>  \r\n\t\t    <br>\r\n\t\t\t<label for="percent" class="label">\u589e\u52a0\u5e45\u5ea6:<select id="percent" name="percent" class="required"/>\r\n\t\t\t\t      <option value=100>100</option>\r\n\t\t\t\t      <option value=50>50</option>\r\n\t\t\t\t      <option value=20>20</option>\r\n\t\t\t</select>%(\u5355\u4f4d\uff1a\u767e\u5206\u6bd4)</label>\r\n\t\t\t<br>\r\n\t\t\t<label for="begin_at" class="label">\u5f00\u59cb\u65f6\u95f4:</label>\r\n\t\t\t<div class="input">\r\n\t\t\t\t <input type="datetime" id="begin_at" name="begin_at" class="datepicker_date"/>\t\r\n\t\t\t</div>\r\n\t\t\t<!--<label for="suspended_at" class="label">\u7ed3\u675f\u65f6\u95f4:</label>\r\n\t\t\t<div class="input">\r\n\t\t\t\t <input type="datetime" id="suspended_at" name="suspended_at" class="datepicker_date"/>\t\r\n\t\t\t</div>\t-->\r\n\t\t\t<label for="begin_at" class="label">\u5f00\u59cb\u65f6\u95f4:</label>\r\n\t\t\t<div class="input">\r\n\t\t\t\t <input type="datetime" id="begin_at" name="begin_at" class="required"/>\t\r\n\t\t\t</div>\r\n\t\t\t<div class="buttons">\r\n\t\t\t\t<input type="reset" class="button"/>\r\n\t\t\t\t<input type="submit" class="button" value="\u786e\u5b9a" />\r\n\t\t\t</div>\r\n\t\t</fieldset>\r\n\t</div>\r\n</form>\t\r\n</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


