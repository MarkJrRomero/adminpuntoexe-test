from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ImproperlyConfigured

class HomePageView(LoginRequiredMixin, TemplateView):
  template_name='base/home.html'

  def get(self, request, *args, **kwargs):
    context = self.get_context_data(**kwargs)
    user = self.request.user
    context['info_user'] = user
    return self.render_to_response(context)
    

class MenuView(HomePageView, LoginRequiredMixin, TemplateView):
    """
    Vista para generar un menu de forma dinámica.
    Se debe definir el parámetro menu_options, como una lista de diccionarios con las opciones:
    title, description, url, url_param, icon, icon_color
    """
    template_name = "base/menu.html"
    title = "Menu"
    menu_options = None
    breadcrumb_list = None
    menu_option_defaults = {
        'title': None,
        'description': None,
        'url': None,
        'url_param': False,
        'permission': False,
        'test': False,
        'icon': None,
        'icon_color': 'primary',
        'badge': 0,
    }

    def __init__(self, **kwargs):
        if self.menu_options is None:
            self.menu_options = kwargs.get('menu_options')
        if self.breadcrumb_list is None:
            self.breadcrumb_list = kwargs.get('breadcrumb_list')
        super().__init__(**kwargs)

    def validate_options(self, option_list):
        new_options = []
        for i, option in enumerate(option_list):
            for key, default in self.menu_option_defaults.items():
                if key not in option:
                    if default is None:
                        raise ImproperlyConfigured(f"Parámetro '{key}' faltante en la opción {i}")
                    option[key] = default
            if option['test']:
                if not hasattr(self, 'test_func'):
                    raise ImproperlyConfigured(f"Debe implementar la función test_func")
                if self.test_func():
                    new_options.append(option)
            else:
                new_options.append(option)
                    
        return new_options

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = self.title
        context['options'] = self.validate_options(self.menu_options)
        context['breadcrumb_list'] = self.breadcrumb_list
        return context