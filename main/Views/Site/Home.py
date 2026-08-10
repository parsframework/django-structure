from ..View import View



class HomeView(View):

    def dispatch(self,request,**kwargs):

        data={}
        return self._render(data,'Home.Home',title='')
