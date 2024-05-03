import argparse

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


class OneYTChannelInfoGetter():
    def __init__(self, conn):
        self.youtube_con = conn 

    def get_search_response_for_channel(self, channel_name: str = None, type: str = "channel", channelId: str = None, page: str = None) -> dict:
        """
        Parameters:
            type: str
            channel, video, playlist, default = "channel"
        """
        return self.youtube_con.search().list(
                    q    = channel_name,
                    part = 'snippet',
                    maxResults = 50,
                    type = type,
                    channelId = channelId,
                    pageToken = page
                ).execute()

    def get_channel_id(self, search_response: dict, channel_name: str) -> str:
        channels = list()
        for search_result in search_response.get('items', []):
            if search_result['id']['kind'] == 'youtube#channel' and search_result['snippet']['title'] == channel_name:
                channels.append((search_result['snippet']['title'], search_result['id']['channelId']))

        return channels[0][1]

    def get_videos(self, search_response: dict):
        videos = dict()
        for search_result in search_response.get('items', []):
            if search_result['id']['kind'] == 'youtube#video':
                videos[search_result['snippet']['title']] = search_result['id']['videoId']
                                 
        return videos
        

        
