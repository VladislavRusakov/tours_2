from django.shortcuts import render


def MainView(request):
    return render(request, 'index.html')


def DepartureView(request, departure):
    return render(request, 'departure.html')


def TourView(request, id):
    return render(request, 'tours.html')


def NotFoundHandler(request, exception):
    return render(request, '404.html')


