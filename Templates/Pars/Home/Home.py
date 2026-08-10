from ..Template import Template
from ..Header.Header import Header
from ..Footer.Footer import Footer




class Home(Template):

    @classmethod
    def run(cls,request,data=None,**kwargs):
        html=cls.getHeader(request,data,**kwargs)

        html+=f'''
Hello World
'''

        html+=cls.getFooter(request,data,**kwargs)
        return html
