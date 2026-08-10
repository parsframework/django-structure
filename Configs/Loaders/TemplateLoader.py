from django.http import HttpResponse,Http404
import importlib



class TemplateLoader:

    @classmethod
    def run(cls,request,data,templatePath=None,**kwargs):
        if isinstance(data,HttpResponse):
            return data
        templateName='Pars'
        kwargs['template']=templateName
        className=templatePath.split('.')[-1]
        try:
            modulePath=f'Templates.{templateName}.{templatePath}'
            module=importlib.import_module(modulePath)
            obj=getattr(module,className)
            result=obj.run(request,data,**kwargs)
            return HttpResponse(result)
        except Exception:
            raise Http404('Template not found')
