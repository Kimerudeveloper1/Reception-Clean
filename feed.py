import feedparser

a=feedparser.parse('https://weather-broker-cdn.api.bbci.co.uk/en/forecast/rss/3day/2643123')

for post in a.entries:
	print post.title+ ":"+post.link+"\n"

