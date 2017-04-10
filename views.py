from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View

from rest_framework.renderers import JSONRenderer

from .models import Spider
# Create your views here.

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)



import random
class SpiderDebugView(View):
    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            try:
                domain = request.POST.get('domain')
                if domain:
                    spider = Spider.objects.get(domain=domain)
                    status = self._fire(spider)
                    spider.status = status
                    spider.save()
                    return JSONResponse({'ret': 0, 'api_status': status, 'result': '{"status": "ok"}'})
                else:
                    return JSONResponse({'ret': 1})
            except Exception as e:
                print(e)
                return JSONResponse({'ret': -1})

        return JSONResponse({'ret': 99})

    def _fire(self, spider):
        status = ['success', 'debug', 'error'][random.randint(0, 1)]

        return status


