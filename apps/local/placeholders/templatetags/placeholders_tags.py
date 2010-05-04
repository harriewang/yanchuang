from django import template
from placeholders.models import Placeholder, Box

register = template.Library()

@register.tag(name='placeholder')
def load_placeholder(parser, token):
	bits = list(token.split_contents())
	if len(bits) != 2:
		raise template.TemplateSyntaxError, "%r tag requires a single argument" % bits[0]
	return PlaceholderNode(parser.compile_filter(bits[1]))
	
class PlaceholderNode(template.Node):
	def __init__(self, name):
		self.name = name
		
	def render(self, context):
		name = self.name.resolve(context)
		placeholder, created = Placeholder.objects.get_or_create(name=name)
		if placeholder.active:
			boxes = placeholder.boxes.filter(active=True)
			placeholder = ''.join([item.content for item in boxes])
		else:
			placeholder = ''
		return template.Template(placeholder).render(context)

@register.tag(name='box')
def load_box(parser, token):
	bits = list(token.split_contents())
	if len(bits) != 2:
		raise template.TemplateSyntaxError, "%r tag requeirs a single argument" % bits[0]
	return BoxNode(parser.compile_filter(bits[1]))
	
class BoxNode(template.Node):
	def __init__(self, name):
		self.name = name
		
	def render(self, context):
		name = self.name.resolve(context)
		box, created = Box.objects.get_or_create(name=name)
		if box.active:
			box = box.content
		else:
			box = ''
		return template.Template(box).render(context)
		
@register.tag(name="list")
def do_list(parser, token, noempty=False):
    """
    Creates a list of the given parameters and put it in the context.
    Useful for generating a list usable by template filters such as random or join.
    
    Examples:
        {% list "string" 1 object.attribute as mylist %}
    """

    bits = list(token.split_contents())
    if len(bits) < 4 or bits[-2] != "as":
        raise template.TemplateSyntaxError("%r expected format is 'value1 value2 ... as name'" % bits[0])
    items = bits[1:-2]
    asvar = bits[-1]
    return ListNode(items, asvar, noempty)

@register.tag(name="listne")
def do_list_noempty(parser, token):
    """
    Same as do_list. But leaves out values that evaluate to False.
    """
    return do_list(parser, token, True)

class ListNode(template.Node):
    def __init__(self, items, asvar, noempty):
        self.items = items
        self.asvar = asvar
        self.noempty = noempty
    
    def render(self, context):
        items = []
        for item in self.items:
            item = template.Variable(item).resolve(context)
            if not self.noempty or item:
                items.append(item)
        context[self.asvar] = items
        return ''