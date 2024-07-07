import yaml
import json
import requests
import pandas as pd
from datetime import timedelta
import isodate

class YoutubeData:
    def __init__(self, config_file_path= "/home/cupawan/Django_Projects/Configs/config.yaml"):
        self.config_file_path = config_file_path
        self.api_key = self.load_config().get('GOOGLE', {}).get('GOOGLE_API_KEY', '')
    
    def load_config(self):
        try:
            with open(self.config_file_path, 'r') as conf:
                config = yaml.safe_load(conf)
                return config
        except Exception as e:
            return {}
    
    def get_playlist_title(self, playlist_id):
        api_playlist_title_url = f'https://www.googleapis.com/youtube/v3/playlists?part=snippet&id={playlist_id}&key={self.api_key}'
        response = requests.get(api_playlist_title_url).json()
        title = response['items'][0]['snippet']['title'] if 'items' in response else 'Unknown Title'
        return title

    def get_playlist_duration(self, playlist_link):
        playlist_id = playlist_link.split("=")[-1]
        playlist_title = self.get_playlist_title(playlist_id)
        api_playlist_url = f'https://www.googleapis.com/youtube/v3/playlistItems?part=contentDetails&maxResults=50&fields=items/contentDetails/videoId,nextPageToken&key={self.api_key}&playlistId={playlist_id}'
        video_url = 'https://www.googleapis.com/youtube/v3/videos?&part=contentDetails&key={}&id={}&fields=items/contentDetails/duration'.format(self.api_key, '{}')
        next_page = ''
        total_videos = 0
        total_duration = timedelta(0)
        df = pd.DataFrame()
        df["Property"] = ['Number of videos', 'Average length of video', 'Total length of playlist', 'At 1.25x', 'At 1.50x', 'At 1.75x', 'At 2.00x']

        while True:
            video_ids = []
            results = json.loads(requests.get(api_playlist_url + next_page).text)
            for item in results.get('items', []):
                video_ids.append(item['contentDetails']['videoId'])
            video_ids_str = ','.join(video_ids)
            total_videos += len(video_ids)
            video_details = json.loads(requests.get(video_url.format(video_ids_str)).text)
            for video in video_details.get('items', []):
                total_duration += isodate.parse_duration(video['contentDetails']['duration'])
            if 'nextPageToken' in results:
                next_page = results['nextPageToken']
            else:
                values = [
                    total_videos,
                    total_duration / total_videos,
                    total_duration,
                    total_duration / 1.25,
                    total_duration / 1.5,
                    total_duration / 1.75,
                    total_duration / 2
                ]
                formatted_values = [total_videos] + [self.format_timedelta(td) for td in values[1:]]
                df['Value'] = formatted_values
                playlist_title_df = pd.DataFrame([{'Property': 'Playlist Title', 'Value': playlist_title}])
                df = pd.concat([playlist_title_df, df], ignore_index=True)
                return df
    
    def format_timedelta(self, td):
        total_seconds = td.total_seconds()
        hours, remainder = divmod(total_seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        return f"{int(hours)}:{int(minutes):02}:{seconds:.2f}"

# Example usage
# youtube_data = YoutubeData()
# df = youtube_data.get_playlist_duration("https://www.youtube.com/playlist?list=YOUR_PLAYLIST_ID")
# print(df)

