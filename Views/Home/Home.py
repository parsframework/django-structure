from ..View import View
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
#from django.urls import reverse







class Home(View):





    def __init__(self,request):

        super().__init__(request)









    def default(self,args={}):
       #x=self.get['z']
       #x=self.get.get("z",'nist')
        #return 'i am t'
        #return redirect('/Home/?id=88')
        #return redirect('home',page='Home')
        #return redirect('index',page='Home',controller='default')
        args={
        'tt':1,
        **args}
        post={
        't':1,
        **self.post}
        get={
        'invoice_id':88,
        **self.get}
        html='ok '
        html+='is okay'
        #h=get['id']
        # return(f"Invoice ID: {args['invoice_id']}")
        return html




