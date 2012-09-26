# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 8
_modified_time = 1348625078.203
_enable_loop = True
_template_filename = u'E:\\workspacePY\\let\\src/views/shared/header.html'
_template_uri = u'/shared/header.html'
_source_encoding = 'utf-8'
from views.filters import Filters, Cycler
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        is_logged_in = context.get('is_logged_in', UNDEFINED)
        current_user = context.get('current_user', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer(u'<header id="header">\n\t<div id="header-inner">\t    \n\t\t<div id="logo">\n\t\t\t<h1>\n\t\t\t\t<a href="/">\u7f51\u7edc\u5e26\u5bbd\u7ba1\u7406\u7cfb\u7edf</a>\n\t\t\t</h1>\n\t\t</div>\n\t\t<div id="user-menu">\n')
        # SOURCE LINE 10
        if is_logged_in : 
            # SOURCE LINE 11
            __M_writer(u'\t\t\t')
            __M_writer(unicode(current_user['_id'].strip()))
            __M_writer(u' : <a href="/logout">log-out</a>\n')
            # SOURCE LINE 12
        else :
            # SOURCE LINE 13
            __M_writer(u'\t\t\t\t<a href="/login">log-in</a>\n')
        # SOURCE LINE 15
        __M_writer(u'\t\t</div>\n\t\t<div class="clear"></div>\n\t</div>\n</header>')
        return ''
    finally:
        context.caller_stack._pop_frame()


