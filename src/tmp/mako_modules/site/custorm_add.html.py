# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 7
_modified_time = 1347032323.725137
_template_filename = '/Users/zongzong/Documents/workspace/mgu/src/views/site/custorm_add.html'
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
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer(u'\r\n<style>\r\n.ui-timepicker-div .ui-widget-header { margin-bottom: 8px; }\r\n.ui-timepicker-div dl { text-align: left; }\r\n.ui-timepicker-div dl dt { height: 25px; margin-bottom: -25px; }\r\n.ui-timepicker-div dl dd { margin: 0 10px 10px 65px; }\r\n.ui-timepicker-div td { font-size: 90%; }\r\n.ui-tpicker-grid-label { background: none; border: none; margin: 0; padding: 0; }\r\n</style>\r\n\r\n')
        # SOURCE LINE 63
        __M_writer(u'\r\n\r\n\r\n<a href="http://www.jztech.cn" target="new">\u66f4\u591a\u6280\u672f\u652f\u6301\uff0c\u6b22\u8fce\u8bbf\u95ee\u541b\u4f17\u79d1\u6280\u516c\u53f8\u7f51\u7ad9\uff01</a>   ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_body(context):
    context.caller_stack._push_frame()
    try:
        range = context.get('range', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 12
        __M_writer(u'\r\n<div class="form" style="margin:0 auto 0 auto;width: 300px;">\r\n\r\n<form action="/custorm_add" method="post" >\r\n\t<div class="field">\r\n\t\t<fieldset>\r\n\t\t\t<label for="cname" class="label">\u5ba2\u6237\u540d\u79f0:</label>\r\n\t\t\t<div class="input">\r\n\t\t\t\t<input type="text" id="cname" name="cname"/>\r\n\t\t\t</div>\r\n\t\t\t<br>\r\n\t\t\t<label for="description" class="label">\u63cf\u8ff0:</label>\r\n\t\t\t<div class="input">\r\n\t\t\t\t<input type="text" id="description" name="description"/>\r\n\t\t\t</div>\r\n\t\t\t<br>\t\r\n\r\n\t\t\t<label for="begin_at" class="label">\u5f00\u59cb\u65f6\u95f4\uff1a</label>\r\n\t\t\t<div class="input">\r\n\t\t\t\t <input type="datetime" class="datepicker_date" name="begin_at"/>\t\r\n\t\t\t</div>\r\n\t\t\t<br>\t\r\n\r\n\t\t\t<label for="begin_at" class="label">\u7ed3\u675f\u65f6\u95f4\uff1a</label>\r\n\t\t\t<div class="input">\r\n\t\t\t\t <input type="datetime" class="datepicker_date" name="suspended_at"/>\t\r\n\t\t\t</div>\r\n\t\t\t<br>\t\r\n\t\t\t<label for="type" class="label">\u4ea7\u54c1\u5e26\u5bbd:</label>\r\n\t\t\t<div class="input">\r\n\t\t\t\t <select id="type" name ="type">\r\n')
        # SOURCE LINE 43
        for i in range(1,21):
            # SOURCE LINE 44
            __M_writer(u'\t\t\t\t\t\t <option value=')
            __M_writer(unicode(i))
            __M_writer(u' > ')
            __M_writer(unicode(i))
            __M_writer(u'</option>  \r\n')
            pass
        # SOURCE LINE 46
        __M_writer(u'\t\t\t\t </select>M(\u5355\u4f4d\uff1a\u5146)\r\n\t\t\t</div>\r\n\t\t\t<br>\r\n\t\t\t<label for="continue_to" class="label">\u53ef\u7528\u65f6\uff1a</label>\r\n\t\t\t<div class="input">\r\n\t\t\t\t<input type="text" id="continue_to" name="continue_to"/>h(\u5355\u4f4d\uff1a\u5c0f\u65f6)\r\n\t\t\t</div>\r\n\t\t\t<br>\r\n\t\t\t<div class="buttons">\r\n\t\t\t\t<input type="reset" class="button"/>\r\n\t\t\t\t<input type="submit" class="button" value="\u6dfb\u52a0" />\r\n\t\t\t</div>\r\n\t\t</fieldset>\r\n\t</div>\r\n</form>\r\n\r\n</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


