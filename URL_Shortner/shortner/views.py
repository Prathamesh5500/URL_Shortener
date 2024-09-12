from django.shortcuts import render, redirect
from django.http import Http404
from .models import urlData
import string, random

def generate_short_url():
    characters = string.ascii_letters + string.digits
    short_url = ''.join(random.choices(characters, k=6))
    return short_url

def redirect_to_long_url(request, short_url):
    try:
        base_url = request.build_absolute_uri('/')
        full_short_url = base_url + short_url

        url_entry = urlData.objects.get(full_short_url=full_short_url)

        return redirect(url_entry.url)
    except urlData.DoesNotExist:
        raise Http404("Short URL not found")


def HomePage(request):
    if request.method == "POST":
        url = request.POST.get('url')

        if not url.startswith(('http://', 'https://')):
            url = 'http://' + url

        short_code = generate_short_url()
        base_url = request.build_absolute_uri('/')
        full_short_url = base_url + short_code

        while urlData.objects.filter(full_short_url=full_short_url).exists():
            short_code = generate_short_url()
            full_short_url = base_url + short_code

        urlData.objects.create(url=url, full_short_url=full_short_url)

        return render(request, 'home.html', {'shorter': full_short_url})

    return render(request, 'home.html')