import argparse

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

class APIConnector:
    def __init__(self):
        self.DEVELOPER_KEY = 'AIzaSyDvzwE3KbRYJcF8eePhdhauiY1BDg1YUYY'
        self.YOUTUBE_API_SERVICE_NAME = 'youtube'
        self.YOUTUBE_API_VERSION = 'v3'
    
    def connect(self):
        """
        Connects to Youtube API.

        Returns:
            A Resource object with methods for interacting with the service.
        """
        return build(serviceName  = self.YOUTUBE_API_SERVICE_NAME, 
                     version      = self.YOUTUBE_API_VERSION,
                     developerKey = self. DEVELOPER_KEY)