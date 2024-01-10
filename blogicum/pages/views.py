from django.shortcuts import render

"""В чем ошибка? рендер используется в возврате функции"""

def about(request):
    template = 'pages/about.html'
    return render(request, template)


def rules(request):
    template = 'pages/rules.html'
    return render(request, template)
