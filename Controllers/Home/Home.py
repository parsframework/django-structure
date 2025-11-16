from ..Controller import Controller
from ...Models.Home.Home import Home as Model
from ...Views.Home.Home import Home as View







class Home(Controller):






    def __init__(self,request):

        super().__init__(request)

        self.model=Model(request)

        self.view=View(request)





