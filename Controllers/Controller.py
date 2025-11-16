class Controller:





    def __init__(self,request):

       self.post=dict(request.POST)

       self.get=dict(request.GET)

       self.request=request








    def __getattr__(self,methodName):
        def cb(*args,**kwargs):
            return getattr(self.view,methodName)()
        return cb



