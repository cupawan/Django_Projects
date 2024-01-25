# views.py

from django.shortcuts import render
from .news import News
from django.http import JsonResponse
from .forms import NewsForm

def dainik_bhaskar(request):
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            state = form.cleaned_data['state']
            city = form.cleaned_data['city']
            cat = form.cleaned_data['category']
            response = News(state=state, city=city).fetch_bhaskar_news(category=cat)
            data = {'result': 'OK', 'data': response}
            return render(request, 'news_app/results.html', {'data': data['data'],'selected_category': cat})
    else:
        form = NewsForm()

    return render(request, 'news_app/news_form.html', {'form': form})
