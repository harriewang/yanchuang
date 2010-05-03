#coding:utf8
"""This is a TinyMCE config, we can import this to project's settings.py """

import os
import settings

TINYMCE_JS_URL = settings.MEDIA_URL + 'js/tiny_mce/tiny_mce.js'
TINYMCE_JS_ROOT = os.path.join(settings.MEDIA_ROOT, 'js/tiny_mce')
TINYMCE_DEFAULT_CONFIG = {
		# General options
		'mode' : "textareas",
		'theme' : "advanced",
		'plugins' : "safari,pagebreak,style,layer,table,advhr,advimage,advlink,emotions,iespell,inlinepopups,insertdatetime,preview,media,searchreplace,contextmenu,paste,directionality,noneditable,visualchars,nonbreaking,xhtmlxtras",

		# Theme options
		'theme_advanced_buttons1' : "bold,italic,underline,strikethrough,|,justifyleft,justifycenter,justifyright,justifyfull,styleselect,formatselect,fontselect,fontsizeselect",
		'theme_advanced_buttons2' : "paste,pastetext,pasteword,|,search,replace,|,bullist,numlist,|,outdent,indent,blockquote,|,undo,redo,|,link,unlink,anchor,image,cleanup,code,|,insertdate,inserttime,preview,|,forecolor,backcolor",
		'theme_advanced_buttons3' : "tablecontrols,|,hr,removeformat,visualaid,|,sub,sup,|,charmap,emotions,iespell,media,advhr,ltr,rtl",
		'theme_advanced_buttons4' : "insertlayer,moveforward,movebackward,absolute,|,styleprops,|,cite,abbr,acronym,del,ins,attribs,|,visualchars,nonbreaking,template,pagebreak",
		'theme_advanced_toolbar_location' : "top",
		'theme_advanced_toolbar_align' : "left",
		'theme_advanced_statusbar_location' : "bottom",
		'theme_advanced_resizing' : True,
		
		'relative_urls' : False,

}
TINYMCE_SPELLCHECKER = False
TINYMCE_COMPRESSOR = False
