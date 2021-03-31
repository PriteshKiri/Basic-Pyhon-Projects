import requests 
from bs4 import BeautifulSoup #BS helps us convert into a object which we can manpulate and use
import pprint # pretty print is used to print in nice manner

res = requests.get('https://news.ycombinator.com/news')
res2 = requests.get('https://news.ycombinator.com/')#requests is a web browser without a window
soup = BeautifulSoup(res.text, 'html.parser')
soup2 = BeautifulSoup(res2.text, 'html.parser')
# print(soup.body)
# print(soup.body.contents)
# print(soup.find_all('a'))
# print(soup.title)
# print(soup.a) # is same as print(soup.find(a)) # both finds the first of whatever you need
# print(soup.find(id='score_26539673'))
 #css selectors are used to grab different elements on HTML page
# print(soup.select('.score')) #gives the list of elements with class score ('.' means class)
# print(soup.select('#score_26539673'))
links = soup.select('.storylink') + soup2.select('.storylink')
subtext = soup.select('.subtext') + soup2.select('.subtext')

def sort_stories_by_vote(hnlist):
	return sorted(hnlist, key = lambda k : k['points'] , reverse=True) #common pattern to sort dictionary



def create_custom_hn(links, subtext):
	hn = []
	for idx, item in enumerate(links):
		title = item.getText()
		href = item.get('href', None)
		vote = subtext[idx].select('.score')
		if vote:
			points = int(vote[0].getText().replace(' points', ''))
			if points > 99:

				hn.append({'title': title ,  'link': href, 'points' : points})
	return sort_stories_by_vote(hn)

pprint.pprint(create_custom_hn(links, subtext))
