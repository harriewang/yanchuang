import settings
from models import StudioConfig, StudioLink

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
