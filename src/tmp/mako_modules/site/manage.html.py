# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 8
_modified_time = 1347451695.873
_enable_loop = True
_template_filename = 'D:\\ishida\\wwwroot\\workspace\\let\\src/views/site/manage.html'
_template_uri = '/site/manage.html'
_source_encoding = 'utf-8'
from views.filters import Filters, Cycler
_exports = ['body']


# SOURCE LINE 27
 
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
        status = context.get('status', UNDEFINED)
        paginator = context.get('paginator', UNDEFINED)
        cname = context.get('cname', UNDEFINED)
        request = context.get('request', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer(u'\r\n<script type="text/javascript">\r\n\tfunction _do_del(c_id){\r\n\t    if(confirm(\'\u60a8\u786e\u5b9a\u6ce8\u9500\u8be5\u5ba2\u6237\u5417\uff1f\')) \r\n\t\t$.ajax({\r\n\t\t\turl:\'custorm_del?c_id=\'+c_id,\r\n\t\t\ttype:\'post\',\t\t\t\r\n\t\t\tsuccess:success,\t\t\t\r\n\t\t\tstatusCode: {\r\n\t\t\t\t404: function() {\r\n    \t\t\t\talert(\'page not found\');\r\n  \t\t\t\t}\r\n\t\t\t},\r\n\t\t\terror:function(jqXHR, textStatus, errorThrown){\r\n\t\t\t\talert(textStatus);\r\n\t\t\t}\r\n\t\t});\r\n\t}\r\n\t\r\n\tfunction success(){\r\n\t\r\n\t}\r\n</script>\r\n\r\n')
        # SOURCE LINE 29
        __M_writer(u'\r\n<div id="page-header">\r\n\t<div class="title">\r\n\t\t\u8fd0\u8425\u5546\u7ba1\u7406\u754c\u9762\r\n\t</div>\r\n\t<div class="subtitle">\r\n\t    \u7528\u6237\u4fe1\u606f\r\n\t</div>\r\n</div>\r\n<form action="/manage" method="post" >\r\n\t<table>\t\t \r\n\t\t<tr>\r\n\t\t\t<td><label for="cname" class="label">\u5ba2\u6237\u540d\u79f0:</label></td>\r\n\t\t\t<td>\r\n\t\t\t\t<input type="text" id="cname" name="cname" value="')
        # SOURCE LINE 43
        __M_writer(unicode(cname))
        __M_writer(u'" />\r\n\t\t\t</td>\r\n\t\t\t<td><label for="status" class="status">\u72b6\u6001:</label></td>\r\n\t\t\t<td>\r\n\t\t\t\t<select id="status" name ="status">\r\n')
        # SOURCE LINE 48
        if status == 0:
            # SOURCE LINE 49
            __M_writer(u'\t\t\t\t\t  <option value=0  selected >\u6fc0\u6d3b</option>  \r\n\t\t\t\t\t  <option value=1 >\u6ce8\u9500</option> \r\n')
            # SOURCE LINE 51
        else:
            # SOURCE LINE 52
            __M_writer(u'\t\t\t\t\t  <option value=0 > \u6fc0\u6d3b</option>  \r\n\t\t\t\t\t  <option value=1 selected >\u6ce8\u9500</option> \r\n')
        # SOURCE LINE 55
        __M_writer(u'\t\t\t\t</select>\r\n\t\t\t</td>\r\n\t\t\t<td><input type="submit"  class="button" value="\u67e5\u8be2" /></td>\r\n\t\t</tr>\r\n\t</table>\r\n</form>\r\n<br>\r\n<div class="field">\r\n\t<table>\r\n\t\t<tbody>\r\n\t\t\t<tr>\r\n\t\t\t\t<th align="center">\u7f16\u53f7</th>\r\n\t\t\t\t<th align="center">\u5ba2\u6237\u540d\u79f0</th>\r\n\t\t\t\t<th align="center">\u5ba2\u6237\u5730\u5740</th>\r\n\t\t\t\t<th align="center">\u5ba2\u6237\u7535\u8bdd</th>\r\n\t\t\t\t<th align="center">\u72b6\u6001</th>\r\n\t\t\t\t<th align="center">\u4ea7\u54c1\u5e26\u5bbd</th>\r\n\t\t\t\t<th align="center">\u5269\u4f59\u65f6\u95f4</th>\r\n\t\t\t\t<th align="center">\u6ce8\u518c\u65f6\u95f4</th>\r\n\t\t\t\t<th align="center">\u8d77\u59cbip</th>\r\n\t\t\t\t<th align="center">\u7ed3\u675fip</th>\r\n\t\t\t\t<th align="center">\u4ef7\u683c</th>\r\n\t\t\t\t<th align="center">\u4f7f\u7528\u8d77\u59cb</th>\r\n\t\t\t\t<th align="center">\u4f7f\u7528\u7ed3\u675f</th>\r\n\t\t\t\t<th align="center">\u64cd\u4f5c</th>\t\t\t\t\r\n\t\t\t</tr>\r\n\t\t\t')
        # SOURCE LINE 81
        i=1 
        
        __M_writer(u'\r\n')
        # SOURCE LINE 82
        for c in paginator.page:
            # SOURCE LINE 83
            __M_writer(u'\t\t\t<tr>\r\n\t\t\t\t<td align="center">')
            # SOURCE LINE 84
            __M_writer(unicode(i))
            __M_writer(u'</td>\r\n\t\t\t\t')
            # SOURCE LINE 85
            i=i+1 
            
            __M_writer(u'\r\n\t\t\t\t<td>')
            # SOURCE LINE 86
            __M_writer(unicode(c['cname']))
            __M_writer(u'</td>\r\n\t\t\t\t<td>')
            # SOURCE LINE 87
            __M_writer(unicode(c['address']))
            __M_writer(u'</td>\r\n\t\t\t    <td>')
            # SOURCE LINE 88
            __M_writer(unicode(c['phonenum']))
            __M_writer(u'</td>\r\n\t\t\t\t<td>\r\n')
            # SOURCE LINE 90
            if c['status']==1: 
                # SOURCE LINE 91
                __M_writer(u'\t\t\t\t\t\t  \u6ce8\u9500\r\n')
                # SOURCE LINE 92
            else: 
                # SOURCE LINE 93
                __M_writer(u'\t\t\t\t\t\t  \u6fc0\u6d3b\r\n')
            # SOURCE LINE 95
            __M_writer(u'\t\t\t\t</td>\r\n\t\t\t\t \r\n\t\t\t\t<td align="right" >')
            # SOURCE LINE 97
            __M_writer(unicode(c['ctype']))
            __M_writer(u'M</td>\r\n\t\t\t\t')
            # SOURCE LINE 98
            ct = c['created_at'].strftime("%y-%m-%d %H:%M:%S") 
            
            __M_writer(u'\r\n\t\t\t\t')
            # SOURCE LINE 99
            cn=c['cname'] 
            
            __M_writer(u'\r\n\t\t\t\t<td align="right">')
            # SOURCE LINE 100
            __M_writer(unicode(c['continue_to']))
            __M_writer(u'h</td>\r\n\t\t\t\t<td>')
            # SOURCE LINE 101
            __M_writer(unicode(ct))
            __M_writer(u'</td>\t\r\n\t\t\t\t\r\n\t\t\t\t<td>')
            # SOURCE LINE 103
            __M_writer(unicode(c['begin_ip']))
            __M_writer(u'</td>\r\n\t\t\t\t<td>')
            # SOURCE LINE 104
            __M_writer(unicode(c['suspended_ip']))
            __M_writer(u'</td>\r\n\t\t\t\t\r\n\t\t\t\t<td>')
            # SOURCE LINE 106
            __M_writer(unicode(c['price']))
            __M_writer(u'</td>\r\n\t\t\t\t<td>')
            # SOURCE LINE 107
            __M_writer(unicode(c['begin_at']))
            __M_writer(u'</td>\r\n\t\t\t\t<td>')
            # SOURCE LINE 108
            __M_writer(unicode(c['suspended_at']))
            __M_writer(u'</td>\r\n\t\t\t\t\r\n\t\t\t\t<td align="center">\r\n\n\t\t\t\t\t<input type="button" class="button" value="\u6ce8\u9500" onclick="_do_del(\'')
            # SOURCE LINE 112
            __M_writer(unicode(c['_id']))
            __M_writer(u'\')" \t  />  \n\t\t\t\t\t<input type="button" class="button" value="\u6fc0\u6d3b" />\r\n\t\t\t\t</td>\r\n\t\t\t</tr>\r\n')
        # SOURCE LINE 117
        __M_writer(u'\t\t\t<br>\r\n\t\t</tbody>\r\n\t</table>\r\n</div>\r\n<div>\r\n\t\t\t\u7b2c ')
        # SOURCE LINE 122
        __M_writer(unicode(paginator.current_page))
        __M_writer(u' \u9875  \uff5c \u5171 ')
        __M_writer(unicode(paginator.page_count))
        __M_writer(u'\u9875   \r\n\t\t\t\r\n\t\t\t<!-- if there is a previous page print a back link -->\r\n')
        # SOURCE LINE 125
        if paginator.has_previous:
            # SOURCE LINE 126
            __M_writer(u'                  <a href="')
            __M_writer(unicode(paginator.previous_page_link(request)))
            __M_writer(u'"><< back</a>\r\n')
        # SOURCE LINE 128
        __M_writer(u'\r\n            <!-- if there is a previous and a next page print a divider -->\r\n')
        # SOURCE LINE 130
        if paginator.has_previous and paginator.has_next:
            # SOURCE LINE 131
            __M_writer(u'                  | \r\n')
        # SOURCE LINE 133
        __M_writer(u'\r\n            <!-- if there is a next page print a next link -->\r\n')
        # SOURCE LINE 135
        if paginator.has_next:
            # SOURCE LINE 136
            __M_writer(u'                    <a href="')
            __M_writer(unicode(paginator.next_page_link(request)))
            __M_writer(u'">next >></a>\r\n')
        # SOURCE LINE 138
        __M_writer(u'            </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


