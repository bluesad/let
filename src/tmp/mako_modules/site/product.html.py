# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 8
_modified_time = 1347442894.578
_enable_loop = True
_template_filename = 'E:\\workspacePY\\let\\src/views/site/product.html'
_template_uri = '/site/product.html'
_source_encoding = 'utf-8'
from views.filters import Filters, Cycler
_exports = ['body']


# SOURCE LINE 5
 
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
        request = context.get('request', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer(u'\r\n\r\n')
        # SOURCE LINE 7
        __M_writer(u'\r\n<div id="page-header">\r\n\t<div class="title">\r\n\t\t\u8fd0\u8425\u5546\u7ba1\u7406\u754c\u9762\r\n\t</div>\r\n\t<div class="subtitle">\r\n\t    \u7528\u6237\u4fe1\u606f\r\n\t</div>\r\n</div>\r\n<div class="field">\r\n\t<table>\r\n\t\t\t<tbody>\r\n\t\t\t\t<tr>\r\n\t\t\t\t\t<th align="center">\u7f16\u53f7</th>\r\n\t\t\t\t    <th align="center">\u5ba2\u6237\u540d\u79f0</th>\r\n\t\t\t\t    <th align="center">\u5ba2\u6237\u5730\u5740</th>\r\n\t\t\t\t    <th align="center">\u5ba2\u6237\u7535\u8bdd</th>\r\n\t\t\t\t    <th align="center">\u72b6\u6001</th>\r\n\t\t\t\t    <th align="center">\u4ea7\u54c1\u5e26\u5bbd</th>\r\n\t\t\t\t    <th align="center">\u6ce8\u518c\u65f6\u95f4</th>\r\n\t\t\t\t    <th align="center">\u8d77\u59cbip</th>\r\n\t\t\t\t    <th align="center">\u7ed3\u675fip</th>\r\n\t\t\t\t    <th align="center">\u64cd\u4f5c</th>\t\t\t\t\t\t\t\t\r\n\t\t\t\t</tr>\r\n')
        # SOURCE LINE 31
        for c in paginator.page:
            # SOURCE LINE 32
            __M_writer(u'\t\t\t\t')
            i=1 
            
            __M_writer(u'\r\n\t\t\t\t\r\n\t\t\t\t<tr>\r\n\t\t\t\t    <td align="center">')
            # SOURCE LINE 35
            __M_writer(unicode(i))
            __M_writer(u'</td>\r\n\t\t\t\t    ')
            # SOURCE LINE 36
            i=i+1 
            
            __M_writer(u'\r\n\t\t\t\t\t<td>')
            # SOURCE LINE 37
            __M_writer(unicode(c['cname']))
            __M_writer(u'</td>\r\n\t\t\t\t\t<td>')
            # SOURCE LINE 38
            __M_writer(unicode(c['address']))
            __M_writer(u'</td>\r\n\t\t\t\t\t<td>')
            # SOURCE LINE 39
            __M_writer(unicode(c['phonenum']))
            __M_writer(u'</td>\r\n\t\t\t\t\t<td>\r\n')
            # SOURCE LINE 41
            if c['status']==0: 
                # SOURCE LINE 42
                __M_writer(u'\t\t\t\t\t          \u6fc0\u6d3b\r\n')
                # SOURCE LINE 43
            else: 
                # SOURCE LINE 44
                __M_writer(u'\t\t\t\t\t          \u6ce8\u9500\r\n')
            # SOURCE LINE 46
            __M_writer(u'\t\t\t\t\t</td>\r\n\t\t\t\t\t<td align="right" >')
            # SOURCE LINE 47
            __M_writer(unicode(c['ctype']))
            __M_writer(u'M</td>\r\n\t\t\t\t\t')
            # SOURCE LINE 48
            ct = c['created_at'].strftime("%y-%m-%d %H:%M:%S") 
            
            __M_writer(u'\r\n\t\t\t\t\t<td>')
            # SOURCE LINE 49
            __M_writer(unicode(ct))
            __M_writer(u'</td>\r\n\t\t\t\t\t<td>')
            # SOURCE LINE 50
            __M_writer(unicode(c['begin_ip']))
            __M_writer(u'</td>\r\n\t\t\t\t\t<td>')
            # SOURCE LINE 51
            __M_writer(unicode(c['suspended_ip']))
            __M_writer(u'</td>\r\n\t\t\t\t\t<td align="center"><input type="button" class="button" value="\u64cd\u4f5c" /></td>\r\n\t\t\t\t</tr>\r\n')
        # SOURCE LINE 55
        __M_writer(u'\t\t\t</tbody>\r\n\t</table>\r\n</div>\r\n<div>\r\n\t\t\t\u7b2c ')
        # SOURCE LINE 59
        __M_writer(unicode(paginator.current_page))
        __M_writer(u' \u9875  \uff5c \u5171 ')
        __M_writer(unicode(paginator.page_count))
        __M_writer(u'\u9875   \r\n\t\t\t\r\n\t\t\t<!-- if there is a previous page print a back link -->\r\n')
        # SOURCE LINE 62
        if paginator.has_previous:
            # SOURCE LINE 63
            __M_writer(u'                  <a href="')
            __M_writer(unicode(paginator.previous_page_link(request)))
            __M_writer(u'"><< back</a>\r\n')
        # SOURCE LINE 65
        __M_writer(u'\r\n            <!-- if there is a previous and a next page print a divider -->\r\n')
        # SOURCE LINE 67
        if paginator.has_previous and paginator.has_next:
            # SOURCE LINE 68
            __M_writer(u'                  | \r\n')
        # SOURCE LINE 70
        __M_writer(u'\r\n            <!-- if there is a next page print a next link -->\r\n')
        # SOURCE LINE 72
        if paginator.has_next:
            # SOURCE LINE 73
            __M_writer(u'                    <a href="')
            __M_writer(unicode(paginator.next_page_link(request)))
            __M_writer(u'">next >></a>\r\n')
        # SOURCE LINE 75
        __M_writer(u'            </div>\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


