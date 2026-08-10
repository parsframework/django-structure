import importlib



class Template:

    @classmethod
    def getHeader(cls,request,data,**kwargs):
        if hasattr(cls,'Header'):
            return cls.Header(request,data,**kwargs)
        modulePath=importlib.import_module('.Header.Header',package=__package__)
        obj=getattr(modulePath,'Header')
        return obj.run(request,data,**kwargs)

    @classmethod
    def getFooter(cls,request,data,**kwargs):
        if hasattr(cls,'Footer'):
            return cls.Footer(request,data,**kwargs)
        modulePath=importlib.import_module('.Footer.Footer',package=__package__)
        obj=getattr(modulePath,'Footer')
        return obj.run(request,data,**kwargs)
