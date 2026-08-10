from django.views import View as DjangoView
from Configs.Loaders.TemplateLoader import TemplateLoader




class View(DjangoView):

    def setup(self,request,**kwargs):
        super().setup(request,**kwargs)
        self._request=request


    def _render(self,response,templatePath=None,**kwargs):
        return TemplateLoader.run(self._request,response,templatePath,**kwargs)
