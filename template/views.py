from django.shortcuts import render
from django.views import View
import requests
import base64
from django.http import HttpResponse

# Create your views here.
def echo(request):
    context = {
        'get': request.GET,
        'post': request.POST,
        'meta': request.META
    }
    return render(request, 'echo.html', context=context)


def filters(request):
    return render(request, 'filters.html', context={
        'a': request.GET.get('a', 1),
        'b': request.GET.get('b', 1)
    })


def extend(request):
    return render(request, 'extend.html', context={
        'a': request.GET.get('a'),
        'b': request.GET.get('b')
    })


class DatasendView(View):
    login = 'alladin'
    password = 'opensesame'
    base_url = 'https://datasend.webpython.graders.eldf.ru'

    def get(self, request):
        return render(request, 'datasend.html')

    def post(self, request):
        response = requests\
            .post(f'{self.base_url}/submissions/1/', headers={'Authorization': f'Basic {self.__get_token(self.login, self.password)}'})\
            .json()

        resp_login = response['login']
        resp_password = response['password']
        resp_path = response['path']

        resp = requests.put(f'{self.base_url}/{resp_path}', headers={'Authorization': f'Basic {self.__get_token(resp_login, resp_password)}'})
        return HttpResponse(resp)

    def __get_token(self, login, password):
        bytes_lw = bytes(f'{login}:{password}', 'utf-8')
        return base64.b64encode(bytes_lw).decode('utf-8')
