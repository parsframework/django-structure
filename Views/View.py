class View:




    def __init__(self,request):

       self.post=dict(request.POST)

       self.get=dict(request.GET)








    def __getattr__(self,methodName):
        def cb(*args,**kwargs):
            return '404'
        return cb



