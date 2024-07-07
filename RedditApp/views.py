from django.shortcuts import render
from django.http import JsonResponse
from prawcore.exceptions import NotFound
from Scripts.reddit_script import RedditData
from Scripts.Configuration import ConfigurationClass


def get_posts_view(request):
    if request.method == "GET":
        return render(request, 'reddit_index.html')

    elif request.method == "POST":
        subreddit = request.POST.get('subreddit')
        limit_posts = request.POST.get('limit')
        filterby = request.POST.get('filterby')

        reddit_data = RedditData()
        try:
            body = reddit_data.make_request(sub=subreddit,limit_posts = limit_posts, filterby = filterby)
        except NotFound:
            error_message = "Please correct your input (remove spaces from subreddit name if any). This subreddit might not exist."
            return render(request, 'error_page.html', {'error_message': error_message})
        return render(request, 'reddit_results.html', {'posts': body})

