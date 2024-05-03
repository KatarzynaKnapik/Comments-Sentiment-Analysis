from app.api_connector import APIConnector
from app.yt_channel_info_getter import OneYTChannelInfoGetter
import pprint

VIDEO_NAME = "Classification Trees in Python from Start to Finish"

if __name__ == "__main__":
    # Connect to YouTube API
    api_connection = APIConnector()
    youtube_con = api_connection.connect()

    # Get channel id 
    channel_info = OneYTChannelInfoGetter(conn=youtube_con)

    # Naruciak info
    search_response = channel_info.get_search_response_for_channel(channel_name = "StatQuest with Josh Starmer")
    channel_id = channel_info.get_channel_id(channel_name="StatQuest with Josh Starmer", 
                                             search_response=search_response)
    print(channel_id)
    
    page = None
    while True:

        search_response_videos = channel_info.get_search_response_for_channel(channelId = channel_id, 
                                                                              type="video",
                                                                              page=page)
        print(search_response_videos)
        videos = channel_info.get_videos(search_response=search_response_videos)
        # print(videos)
        print()

        if VIDEO_NAME in videos.keys():
            video_id = videos[VIDEO_NAME]
            break
        page = search_response_videos["nextPageToken"]

    print(video_id)










