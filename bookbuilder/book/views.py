from django.views.generic import TemplateView
from os.path import exists


class PageView(TemplateView):

    def get_template_names(self):
        template_name = self.kwargs.get('template','index.html')
        if not exists('templates/' + template_name):
            template_name = 'missing.html'
        return template_name
