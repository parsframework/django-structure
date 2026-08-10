from ..View import View
from .Home import *
from .Page404 import *



class SiteView(View):

    def dispatch(self,request,**kwargs):
        html=''
        return self._render(html,title='')
