import datetime
import instaloader
from dateutil import tz


loader = instaloader.Instaloader()
loader.load_session_from_file("notyouruser20")

account_name = "mindsethub_"

start_date = datetime.datetime.now(tz.UTC) - datetime.timedelta(days=30)
profile = instaloader.Profile.from_username(loader.context, account_name)

posts = profile.get_posts()
mike_tyson_related_posts = []
for post in posts:
    if post.date_local.replace(tzinfo=tz.tzlocal()) > start_date:
        if post.is_video and "miketyson" in post.caption.lower() or "miketyson" in [tag.lower() for tag in post.caption_hashtags]:
            mike_tyson_related_posts.append(post)
            loader.download_reels([post], target="#miketyson_reels")

if not mike_tyson_related_posts:
    print("No posts related to Mike Tyson were found.")
else:
    print(f"{len(mike_tyson_related_posts)} posts related to Mike Tyson were found and their reels were downloaded successfully.")