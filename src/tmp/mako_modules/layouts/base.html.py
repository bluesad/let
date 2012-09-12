# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 8
_modified_time = 1347421103.703
_enable_loop = True
_template_filename = u'E:\\workspacePY\\let\\src/views/layouts/base.html'
_template_uri = u'/layouts/base.html'
_source_encoding = 'utf-8'
from views.filters import Filters, Cycler
_exports = ['scripts', 'page_title', 'head_tags']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        self = context.get('self', UNDEFINED)
        next = context.get('next', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer(u'<!doctype html>\n<!--[if lt IE 7]> <html class="no-js lt-ie9 lt-ie8 lt-ie7" lang="zh-CN"> <![endif]-->\n<!--[if IE 7]>    <html class="no-js lt-ie9 lt-ie8" lang="zh-CN"> <![endif]-->\n<!--[if IE 8]>    <html class="no-js lt-ie9" lang="zh-CN"> <![endif]-->\n<!--[if gt IE 8]><!-->\n<html class="no-js" lang="zh-CN">\n<!--<![endif]-->\n<head>\n\t<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">\n\t<meta charset="utf-8">\n\n\t')
        # SOURCE LINE 13
        __M_writer(u'\n\t<title>\n\t\t')
        # SOURCE LINE 15
        __M_writer(unicode(self.page_title()))
        __M_writer(u'\n\t</title>\n\t\n\t<meta name="keywords" content="" />\n\t<meta name="description" content="">\n\t<meta name="viewport" content="width=768, initial-scale=1.0">\n\t<!--[if lt IE 9]>\n\t\t<script src="http://html5shim.googlecode.com/svn/trunk/html5-els.js"></script>\n\t<![endif]-->\n\t\n\t<link rel="stylesheet" href="/static/css/reset.css?')
        # SOURCE LINE 25
        __M_writer(unicode(Filters.version()))
        __M_writer(u'">\n\t<link rel="stylesheet" href="/static/css/common.css?')
        # SOURCE LINE 26
        __M_writer(unicode(Filters.version()))
        __M_writer(u'">\n\t<link rel="stylesheet" href="/static/css/layout.css?')
        # SOURCE LINE 27
        __M_writer(unicode(Filters.version()))
        __M_writer(u'">\n\t<link rel="stylesheet" href="/static/css/flash-messages.css?')
        # SOURCE LINE 28
        __M_writer(unicode(Filters.version()))
        __M_writer(u'">\n\t<link type="text/css" rel="stylesheet" href="/static/css/menu.css" />\n\t<link type="text/css" rel="stylesheet" href="/static/css/editTable.css" />\n\t<link rel="shortcut icon" href="/static/images/images.ico" type="image/x-icon" />\t\t\n\t<!--link type="text/css" href="/static/css/jquery-ui-1.8.23.custom.css" rel="stylesheet" /-->\n\t<link type="text/css" href="/static/css/jquery.ui.min.css" rel="stylesheet" />\n\t<link rel="stylesheet" media="all" type="text/css" href="/static/css/jquery-ui-timepicker-addon.css" />\n\t\n\t<script src="/static/js/jquery-1.7.1.min.js"></script>\n    <script type="text/javascript" src="http://code.jquery.com/ui/1.8.21/jquery-ui.min.js"></script>\n\t<script src="/static/js/flash-messages.js?')
        # SOURCE LINE 38
        __M_writer(unicode(Filters.version()))
        __M_writer(u'"></script>\n\t\n\t')
        # SOURCE LINE 40
        __M_writer(unicode(self.head_tags()))
        __M_writer(u'\n\t')
        # SOURCE LINE 41
        __M_writer(u'\n</head>\n<body>\n\t<!--[if lt IE 7]><p class=chromeframe>Your browser is <em>ancient!</em> <a href="http://browsehappy.com/">Upgrade to a different browser</a> or <a href="http://www.google.com/chromeframe/?redirect=true">install Google Chrome Frame</a> to experience this site.</p><![endif]-->\n\n\t')
        # SOURCE LINE 46
        __M_writer(unicode(next.body()))
        __M_writer(u'\n\t\n\t<!--<script src="//ajax.googleapis.com/ajax/libs/jquery/1.7.1/jquery.min.js"></script>-->\n\t<!--<script>window.jQuery || document.write(\'<script src="/static/js/jquery-1.7.1.min.js"><\\/script>\')</script>-->\n \n    \n\t\n\t<script type="text/javascript" src="/static/js/menu.js"></script>\n    <script type="text/javascript" src="/static/js/editTable.js"></script>\n    <script type="text/javascript" src="/static/js/jquery-ui-timepicker-addon.js"></script>\n\t<script type="text/javascript" src="/static/js/jquery-ui-sliderAccess.js"></script>\n    \n    <script src="/static/js/whirlwind.js?')
        # SOURCE LINE 58
        __M_writer(unicode(Filters.version()))
        __M_writer(u'"></script>\t\n\t<script src="/static/js/application.js?')
        # SOURCE LINE 59
        __M_writer(unicode(Filters.version()))
        __M_writer(u'"></script>  \n    \n\t')
        # SOURCE LINE 61
        __M_writer(unicode(self.scripts()))
        __M_writer(u' \n\t')
        # SOURCE LINE 62
        __M_writer(u'\n\t\n</body>\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_scripts(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_page_title(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 13
        __M_writer(u'\u541b\u4f17\u79d1\u6280')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_head_tags(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


