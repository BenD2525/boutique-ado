from django.shortcuts import render


def profile(request):
    template = 'templates/profiles/profile.html'
    context = {}

    return render(request, template, context)
