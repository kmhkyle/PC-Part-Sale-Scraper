
import praw
import urllib, requests



def sendAlert(message):
    url = 'https://api.telegram.org/bot%s/sendMessage?chat_id=%s&text=%s' % ('', '', urllib.parse.quote_plus(message)) # removed api info in github
    _ = requests.get(url, timeout=10)


oldPosts = []
f = open('C:/Users/Kyle/Documents/python_stuff/scraper/oldPosts.csv', 'r')
for line in f:
    oldPosts.append(line.strip('\n'))
f.close()

# Read-only instance
redditReadOnly = praw.Reddit(client_id='',         # client id removed api info in github
                               client_secret='',      # client secret removed api info in github
                               user_agent='scrapping')        # user agent 
 
 
subreddit = redditReadOnly.subreddit('buildapcsales')


productSearch = ['cpu', 'gpu', 'bundle']
newFile = open('C:/Users/Kyle/Documents/python_stuff/scraper/oldPosts.csv', 'w')


for post in subreddit.new(limit=10):
    title = post.title
    newFile.write(title)
    newFile.write('\n')
    if title not in oldPosts and 'AMD Ryzen 7 5700X3D - $209.99 (Sold & Shipped by Amazon)' not in title :
        postType = title[title.find('[')+1:title.find(']')]
        if postType.lower() in productSearch:
            sendAlert(postType + ' Sale - ' + title)

newFile.close()

    