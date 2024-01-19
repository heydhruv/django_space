from django.shortcuts import render
# Create your views here.


def main(request):
    users = [
                {'name':'dhruv', 'age':22},
                {'name':'jay', 'age':23},
                {'name':'kush', 'age':24},
            ]
    return render(request, 'index.html', context = {'users':users})