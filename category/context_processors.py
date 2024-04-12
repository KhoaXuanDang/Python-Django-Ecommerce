from .models import Category
# Remember to configure in settings TEMPLATES
# fectch all categories in db and store in a dictionary links
def menu_links(request):
    links = Category.objects.all()
    return dict(links=links)
