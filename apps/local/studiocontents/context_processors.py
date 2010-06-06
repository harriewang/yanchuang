from models import Navigation, News

def navigations(request):
	context_navigations = {}
	navigation_top = Navigation.objects.filter(position='top', active=True)
	navigation_bottom = Navigation.objects.filter(position='bottom', active=True) 

	context_navigations['navigation_top'] = navigation_top
	context_navigations['navigation_bottom'] = navigation_bottom
	
	return context_navigations
	
	
