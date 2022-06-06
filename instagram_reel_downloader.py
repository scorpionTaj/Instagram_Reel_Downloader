from instascrape import Reel
import time
SESSIONID = "32086552208%3AXPZ2m1hVX9amRS%3A22"

headers = {
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
	AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.74 \
	Safari/537.36 Edg/79.0.309.43",
	"cookie": f'sessionid={SESSIONID};'
}
insta_reel = Reel('Reel Lien Paste In Here')

insta_reel.scrape(headers=headers)

insta_reel.download(fp=f"C:\\Users\\bourh\\Desktop\\reel{int(time.time())}.mp4")

# printing success Message
print('Downloaded Successfully.')
