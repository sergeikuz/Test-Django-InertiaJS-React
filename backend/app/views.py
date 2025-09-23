from inertia import render


def index(request):
    return render(request, "Index", props={"description": "Демо Django + InertiaJS + React"})


def about(request):
    return render(request, "About", props={"description": "Демо Django + InertiaJS + React, для лучшего понимания SPAшки"})