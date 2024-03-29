from django.http import HttpResponse, JsonResponse
from django.views.generic import View, TemplateView
import os
from django.conf import settings


class PostListView1(View):
    def get(self,request):
        name = 'jinhyeon'
        html = self.get_template_string().format(name=name)
        return HttpResponse(html)

    def get_template_string(self):
        return '''
        <h1>AskDjango</h1>
        <p>{name}</p>
        <p>여러분의 파이썬&장고 페이스메이커가 되어드리겠습니다.</p>
        '''

post_list1 = PostListView1.as_view()

class PostListView2(TemplateView):
    template_name = 'dojo/post_list2.html'

    def get_context_data(self):
        context = super().get_context_data()
        context['name'] = 'jinhyeon'
        return context

post_list2 = PostListView2.as_view()

class PostListView3(View):
    def get(self, request):
        return JsonResponse(self.get_data(), json_dumps_params={'ensure_ascii':False})

    def get_data(self):
        return {
            'message' : 'hello, django',
            'items' : ['python', 'django', 'Celery', 'Azure', 'AWS']
        }

post_list3 = PostListView3.as_view()

class ExcelDownloadView(View):
    def get(self, request):
        filepath = os.path.join(settings.BASE_DIR, 'test.xls')
        filename = os.path.basename(filepath)
        with open(filepath, 'rb') as f:
            response = HttpResponse(f, content_type='application/vnd.ms-excel')
            response['Content-Disposition']='attachment; filename={}'.format(filename)
            return response

excel_download = ExcelDownloadView.as_view()
