from django.shortcuts import render
from Scripts.yt_script import YoutubeData

def calculate_length_view(request):
    if request.method == "GET":
        return render(request, 'yt_index.html')
    elif request.method == "POST":
        video_link = request.POST.get("playlist_link")
        print(f"Link$: {video_link}")
        obj = YoutubeData()
        df = obj.get_playlist_duration(playlist_link=video_link)
        
        # Extract playlist title and remove it from the DataFrame
        playlist_title = df.loc[df['Property'] == 'Playlist Title', 'Value'].values[0]
        df = df[df['Property'] != 'Playlist Title']
        
        return render(request, 'yt_results.html', {'df': df, 'playlist_title': playlist_title})

