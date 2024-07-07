import requests
import json
import os
from datetime import timedelta
import isodate
import pandas as pd
import yaml
# from tabulate import tabulate

class YoutubeData:
    def __init__(self, config_file_path):
        self.config_file_path = config_file_path
        self.api_key = self.load_config()['GOOGLE_API_KEY']
    def load_config(self):
        try:
            with open(self.config_file_path, 'r') as conf:
                config = yaml.safe_load(conf)
                return config
        except Exception as e:
            d = {}
            return d
    def get_playlist_duration(self, playlist_link):
        playlist_id = playlist_link.split("=")[-1]
        api_playlist_url = f'https://www.googleapis.com/youtube/v3/playlistItems?part=contentDetails&maxResults=50&fields=items/contentDetails/videoId,nextPageToken&key={self.api_key}&playlistId={playlist_id}'
        video_url = 'https://www.googleapis.com/youtube/v3/videos?&part=contentDetails&key={}&id={}&fields=items/contentDetails/duration'.format(self.api_key, '{}')
        next_page = ''
        total_videos = 0
        total_duration = timedelta(0)
        df = pd.DataFrame()
        df["Property"] = ['Number of videos','Average length of video','Total length of playlist','At 1.25x','At 1.50x','At 1.75x','At 2.00x']
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
                values = [total_videos,total_duration / total_videos,total_duration,total_duration / 1.25,total_duration / 1.5,total_duration / 1.75,total_duration / 2]
                df['Value'] = values
                return df
                break
