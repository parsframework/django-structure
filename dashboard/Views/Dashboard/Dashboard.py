from ..View import View



class DashboardView(View):
    def dispatch(self,request,**kwargs):
        html=''
        return self._render(html,'Home.Home',title='')
