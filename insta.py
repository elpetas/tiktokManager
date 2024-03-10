import datetime
import instaloader
from dateutil import tz

loader = instaloader.Instaloader()
loader.load_session_from_file("notyouruser20")

account_name = "mindsethub_"
start_date = datetime.datetime.now(tz.UTC) - datetime.timedelta(days=7)

profile = instaloader.Profile.from_username(loader.context, account_name)
posts = profile.get_posts()

mindsethub_last_week_posts = []
for post in posts:
    if post.date_local.replace(tzinfo=tz.tzlocal()) > start_date:
        mindsethub_last_week_posts.append(post)
        loader.download_post(post, target="#mindsethub_last_week_posts")

if not mindsethub_last_week_posts:
    print("No posts were found from mindsethub_ account in the last week.")
else:
    print(f"{len(mindsethub_last_week_posts)} posts were found from mindsethub_ account in the last week and downloaded successfully.")
