from .models import Category
# Remember to configure in settings TEMPLATES

def menu_links(request):
    links = Category.objects.all()
    return dict(links=links)
