from django.http import HttpResponse
from pathlib import Path
import importlib








def index(request,page,controller='default'):

    try:

        appName=Path(__file__).parent.name

        page=page.capitalize()

        modulePath=f"{appName}.Controllers.{page}.{page}"

        module=importlib.import_module(modulePath)

        cls=getattr(module,page)(request)

        result=getattr(cls,controller)()

        if isinstance(result,HttpResponse):
            return result

        return HttpResponse(result)





    except ModuleNotFoundError:
        return HttpResponse(f"Page not found: {modulePath}",status=404)

    except AttributeError as e:
        return HttpResponse(f"Controller '{controller}' not found. Error: {e}",status=404)

    except Exception as e:
        return HttpResponse(f"Error: {e}",status=500)


