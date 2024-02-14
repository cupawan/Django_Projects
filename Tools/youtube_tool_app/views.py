from django.shortcuts import render
from .main import YoutubeData


def calculate_length_view(request):
    if request.method == "GET":
        return render(request, 'yt_index.html')
    elif request.method == "POST":
        video_link = request.POST.get("playlist_link")
        print(f"Link$: {video_link}")
        obj = YoutubeData(config_file_path = "/home/cupawan/Django_Projects/Tools/config.yaml")
        df = obj.get_playlist_duration(playlist_link=video_link)
        return render(request, 'yt_result.index')
