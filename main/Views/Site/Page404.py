from ..View import View



class Page404View(View):

    def dispatch(self,request,**kwargs):
        html='Page not found'
        return self._render(html,title='404',status=404)
