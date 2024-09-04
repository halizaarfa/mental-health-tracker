from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306211401',
        'name': 'Haliza Arfa',
        'class': 'PBP C'
    }

    return render(request, "main.html", context)
