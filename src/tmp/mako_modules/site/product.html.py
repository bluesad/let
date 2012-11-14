# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 8
_modified_time = 1351659692.671
_enable_loop = True
_template_filename = 'E:\\workspacePY\\sod\\src/views/site/product.html'
_template_uri = '/site/product.html'
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
        # SOURCE LINE 119
        __M_writer(u'\r\n\r\n')
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
        __M_writer(u'\r\n')
        # SOURCE LINE 4
        __M_writer(u'\r\n<div id="page-header">\r\n\t<div class="title">\r\n\t\t\u4ea7\u54c1\u7ba1\u7406\u754c\u9762\r\n\t</div>\r\n\t<div class="subtitle">\r\n\t    \u4ea7\u54c1\u4fe1\u606f\r\n\t</div>\r\n</div>\r\n<div class="field">\r\n\t<table id="product" class="table table-hover">\r\n\t\t\t<tbody>\r\n\t\t\t\t<tr>\r\n\t\t\t\t\t<th align="center">\u7f16\u53f7</th>\r\n\t\t\t\t    <th align="center">\u5ba2\u6237\u540d\u79f0</th>\r\n\t\t\t\t    <th align="center">\u5ba2\u6237\u5730\u5740</th>\r\n\t\t\t\t    <th align="center">\u5ba2\u6237\u7535\u8bdd</th>\r\n\t\t\t\t    <th align="center">\u72b6\u6001</th>\r\n\t\t\t\t    <th align="center">\u4ea7\u54c1\u5e26\u5bbd</th>\r\n\t\t\t\t    <th align="center">\u6ce8\u518c\u65f6\u95f4</th>\r\n\t\t\t\t    <!--<th align="center">\u8d77\u59cbip</th>\r\n\t\t\t\t    <th align="center">\u7ed3\u675fip</th>-->\r\n\t\t\t\t    <th align="center">\u64cd\u4f5c</th>\t\t\t\t\t\t\t\t\r\n\t\t\t\t</tr>\r\n')
        # SOURCE LINE 28
        for c in paginator.page:
            # SOURCE LINE 29
            __M_writer(u'\t\t\t\t')
            i=1 
            
            __M_writer(u'\r\n\t\t\t\t<tr style="cursor:pointer">\r\n\t\t\t\t    <td align="center" >')
            # SOURCE LINE 31
            __M_writer(unicode(i))
            __M_writer(u'</td>\r\n\t\t\t\t    ')
            # SOURCE LINE 32
            i=i+1 
            
            __M_writer(u'\r\n\t\t\t\t\t<td>')
            # SOURCE LINE 33
            __M_writer(unicode(c['cname']))
            __M_writer(u'</td>\r\n\t\t\t\t\t<td>')
            # SOURCE LINE 34
            __M_writer(unicode(c['address']))
            __M_writer(u'</td>\r\n\t\t\t\t\t<td>')
            # SOURCE LINE 35
            __M_writer(unicode(c['phonenum']))
            __M_writer(u'</td>\r\n\t\t\t\t\t<td>\r\n')
            # SOURCE LINE 37
            if c['status']==0: 
                # SOURCE LINE 38
                __M_writer(u'\t\t\t\t\t              \u6ce8\u9500\r\n')
                # SOURCE LINE 39
            else: 
                # SOURCE LINE 40
                __M_writer(u'\t\t\t\t\t              \u6fc0\u6d3b    \r\n')
            # SOURCE LINE 42
            __M_writer(u'\t\t\t\t\t</td>\r\n\t\t\t\t\t<td align="right" >')
            # SOURCE LINE 43
            __M_writer(unicode(c['ctype']))
            __M_writer(u'M</td>\r\n\t\t\t\t\t')
            # SOURCE LINE 44
            ct = c['created_at'].strftime("%y-%m-%d %H:%M:%S") 
            
            __M_writer(u'\r\n\t\t\t\t\t<td>')
            # SOURCE LINE 45
            __M_writer(unicode(ct))
            __M_writer(u'</td>\r\n\t\t\t\t\t<td align="center">\r\n')
            # SOURCE LINE 47
            if c['status']==1:
                # SOURCE LINE 48
                __M_writer(u'\t\t\t\t\t\t<input type="button" class="button" value="\u64cd\u4f5c" />\r\n\t\t\t\t\t\t<input type="hidden" class="cid" value="')
                # SOURCE LINE 49
                __M_writer(unicode(c['_id']))
                __M_writer(u'" />\r\n')
            # SOURCE LINE 51
            __M_writer(u'\t\t\t\t\t</td>\r\n\t\t\t\t</tr>\r\n')
        # SOURCE LINE 54
        __M_writer(u'\t\t        <tr id="ui-detail-row" >\r\n\t\t        \t<td colspan="10">\r\n\t\t        \t\t<table id="ui-detail-content">\t\t        \t\t\t\r\n\t\t        \t\t</table>\r\n\t\t        \t</td>\r\n\t\t        </tr>\r\n\t\t\t</tbody>\r\n\t</table>\r\n</div>\r\n<div>\r\n\t\t\t\u7b2c ')
        # SOURCE LINE 64
        __M_writer(unicode(paginator.current_page))
        __M_writer(u' \u9875  \uff5c \u5171 ')
        __M_writer(unicode(paginator.page_count))
        __M_writer(u'\u9875   \r\n\t\t\t<!-- if there is a previous page print a back link -->\r\n')
        # SOURCE LINE 66
        if paginator.has_previous:
            # SOURCE LINE 67
            __M_writer(u'                  <a href="')
            __M_writer(unicode(paginator.previous_page_link(request)))
            __M_writer(u'"><< back</a>\r\n')
        # SOURCE LINE 69
        __M_writer(u'            <!-- if there is a previous and a next page print a divider -->\r\n')
        # SOURCE LINE 70
        if paginator.has_previous and paginator.has_next:
            # SOURCE LINE 71
            __M_writer(u'                  | \r\n')
        # SOURCE LINE 73
        __M_writer(u'            <!-- if there is a next page print a next link -->\r\n')
        # SOURCE LINE 74
        if paginator.has_next:
            # SOURCE LINE 75
            __M_writer(u'                    <a href="')
            __M_writer(unicode(paginator.next_page_link(request)))
            __M_writer(u'">next >></a>\r\n')
        # SOURCE LINE 77
        __M_writer(u'</div>\r\n<div id="dialog" title="\u6807\u9898">\r\n\t<iframe src="about:blank" id="sl-product-frame"\r\n\t\tonresize="this.height=this.contentWindow.document.body.scrollHeight"\r\n\t\tstyle="padding: 0;"\r\n\t\twidth="100%" height="0"\r\n\t\tframeBorder=0 scrolling=yes\r\n\t\tonload="this.height=this.contentWindow.document.body.scrollHeight"></iframe>\r\n</div>\r\n<script>\t\r\n\tfunction closeDialog(){\r\n\t\tsetTimeout(\'clozeDialog()\',1000);\t\t\r\n\t}\r\n\tfunction clozeDialog(){\r\n\t\t//$( "#dialog" ).dialog("close");\r\n\t\twindow.location.reload();\r\n\t}\r\n\t$(function(){\r\n\t\t$( "#dialog" ).dialog({\r\n\t\t\tautoOpen: false,\r\n\t\t\theight: 300,\r\n\t\t\twidth: 350,\r\n\t\t\tclose: function(event, ui) {\r\n\t\t\t\t$(\'#sl-product-frame\').attr(\'src\',\'about:blank\');\r\n\t\t\t},\r\n\t\t\tmodal: true\r\n\t\t});\r\n\t\t$(\'input[value="\u64cd\u4f5c"]\').click(function(){\r\n\t\t\t$(\'#sl-product-frame\').attr(\'src\',\'/bandwidth?p_id=\'+$(this).parent().find(\'.cid\').val());\r\n\t\t\t$( "#dialog" ).dialog("open");\t\t\r\n\t\t});\r\n\t    $(\'#product tr:gt(0) td:lt(9)\').click(function(){\t\t\r\n\t\t\t$.getJSON(\'/bandwidthlog?p_id=\'+$(this).parent().find(\'.cid\').val(), function(json){\r\n\t\t\t\tfor (i=0;i<json.users.length;i++){\r\n\t\t\t\t   var tpl =tpl + \'<tr><td>\u5ba2\u6237\u540d\u79f0:</td><td>{0}</td><td>\u767e\u5206\u6bd4:</td><td>{1}</td><td>\u5f00\u59cb\u65f6\u95f4:</td><td>{2}</td><td>\u7ed3\u675f\u65f6\u95f4:</td><td>{3}</td></tr>\';\r\n\t\t\t\t   tpl=tpl.format(json.users[i].cname,json.users[i].percent,json.users[i].begin_at,json.users[i].suspended_at);\r\n\t\t\t\t}\r\n\t\t\t\t$(\'#ui-detail-content\').html(tpl);\r\n\t\t\t}); \t\t\t\r\n\t    });\r\n\t});\r\n</script>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


