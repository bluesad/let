# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 8
_modified_time = 1350461627.843
_enable_loop = True
_template_filename = 'E:\\workspacePY\\let\\src/views/site/stat_bw.html'
_template_uri = '/site/stat_bw.html'
_source_encoding = 'utf-8'
from views.filters import Filters, Cycler
_exports = ['body']


# SOURCE LINE 4
import time 

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
        __M_writer(u'\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_body(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        paginator = context.get('paginator', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer(u'\r\n')
        # SOURCE LINE 4
        __M_writer(u'\r\n<div id="page-header">\r\n\t<div class="title">\r\n\t\t\u7edf\u8ba1\u754c\u9762\r\n\t</div>\r\n\t<div class="subtitle">\r\n\t          \u4f7f\u7528\u4fe1\u606f\u7edf\u8ba1\r\n\t</div>\r\n</div>\r\n\t<table>\r\n\t\t<tbody>\r\n\t\t\t\t<tr>\r\n\t\t\t\t\t<th align="center">\u7f16\u53f7</th>\r\n\t\t\t\t    <th align="center">\u5ba2\u6237\u540d\u79f0</th>\r\n\t\t\t\t    <th align="center">\u63d0\u5347\u6bd4\u7387</th>\r\n\t\t\t\t    <th align="center">\u8d77\u59cb\u65f6\u95f4</th>\r\n\t\t\t\t    <th align="center">\u7ed3\u675f\u65f6\u95f4</th>\t\t\t\t\t\t\t\r\n\t\t\t\t</tr>\r\n')
        # SOURCE LINE 22
        for c in paginator.page:
            # SOURCE LINE 23
            __M_writer(u'\t\t\t\t')
            i=1 
            
            __M_writer(u'\r\n\t\t\t\t<tr style="cursor:pointer">\r\n\t\t\t\t    <td align="center" >')
            # SOURCE LINE 25
            __M_writer(unicode(i))
            __M_writer(u'</td>\r\n\t\t\t\t    ')
            # SOURCE LINE 26
            i=i+1 
            
            __M_writer(u'\r\n\t\t\t\t\t<td>')
            # SOURCE LINE 27
            __M_writer(unicode(c['cname']))
            __M_writer(u'</td>\r\n\t\t\t\t\t<td>')
            # SOURCE LINE 28
            __M_writer(unicode(c['percent']))
            __M_writer(u'%</td>\r\n\t\t\t\t\t<td>')
            # SOURCE LINE 29
            __M_writer(unicode(c['begin_at']))
            __M_writer(u'</td>\r\n\t\t\t\t\t<td>')
            # SOURCE LINE 30
            __M_writer(unicode(c['suspended_at']))
            __M_writer(u'</td>\r\n\t\t\t\t</tr>\r\n')
        # SOURCE LINE 33
        __M_writer(u'\t\t        <tr id="ui-detail-row" >\r\n\t\t        \t<td colspan="10">\r\n\t\t        \t\t<table id="ui-detail-content">\t\t        \t\t\t\r\n\t\t        \t\t</table>\r\n\t\t        \t</td>\r\n\t\t        </tr>\r\n\t\t\t</tbody>\r\n\t</table>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


