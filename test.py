from tiktok_uploader.upload import upload_video, upload_videos
from tiktok_uploader.auth import AuthBackend

# single video
upload_video('video1.mp4', description='#motivation', cookies='cookies.txt')

# Multiple Videos
videos = [
    {'path': 'video1.mp4', 'description': 'this is my description'}
]
auth = AuthBackend(cookies='cookies.txt')
upload_videos(videos=videos, auth=auth)