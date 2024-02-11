from django.shortcuts import render
from django.http import JsonResponse
from .script import RedditData

def get_posts_view(request):
    if request.method == "GET":
        return render(request, 'reddit_index.html')
    
    elif request.method == "POST":    
        subreddit = request.POST.get('subreddit')
        filter = request.POST.get('filter')
        config_path = 'DjangoProjects/Tools/django_dev_project/config.yaml'
        reddit_data = RedditData(config_path=config_path)
        body = reddit_data.make_request(sub=subreddit, filter=filter)
        body_html = reddit_data.generate_html(body=body)
        return render(request, 'reddit_results.html', {'posts': body})
