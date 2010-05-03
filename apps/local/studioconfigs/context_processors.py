import settings
from models import StudioConfig, StudioLink

def i18n(request):
    from django.utils import translation
    
    context_extras = {}
    context_extras['LANGUAGES'] = settings.LANGUAGES
    context_extras['LANGUAGE_CODE'] = translation.get_language()
    context_extras['LANGUAGE_CODE_URL'] = translation.get_language().replace('-', '_')
    #context_extras['LANGUAGE_BIDI'] = translation.get_language_bidi()
    #context_extras['LANGUAGE_SMALL'] = context_extras['LANGUAGE_CODE'].split('-')[0]
    
    return context_extras


def studio_base(request):
    """Put studio base information and friend links into generic Context"""
    
    context_studio_base = {}
    try:
        context_studio_base['STUDIO_INFO']  = StudioConfig.objects.filter(active=True)[0]
    except IndexError:
        context_studio_base['STUDIO_INFO']  = None
    try:
        context_studio_base['STUDIO_LINKS'] = StudioLink.objects.filter(active=True).order_by('-weight')
    except:
        context_studio_base['STUDIO_LINKS'] = None

    return context_studio_base

def media(request):
	context_media = {}
	context_media['MEDIA_URL'] = settings.MEDIA_URL
	
	return context_media