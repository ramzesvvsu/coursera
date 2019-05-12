from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def echo(request):
    method = request.method.lower()
    strparams = ' '
    statement_value = request.META.get('X-Print-Statement', 'test')
    if request.method == 'GET':
        params = request.GET
    else:
        params = request.POST
    for currentkey in params:
        strparams += f'{currentkey}: {params.get(currentkey)}'
    return render(request, 'echo.html', {'method': method,
                  'params': params, 'statement_value': statement_value,
                                         'params_len': len(params)})
    #if len(params) == 0:
    #    return HttpResponse(f'statement is {statement_value}', status=200)
    #else:
    #    return HttpResponse(f'{method}  {strparams} statement is {statement_value}', status=200)


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
