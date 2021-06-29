import urllib.request		# fetches raw web pages for us
import bs4		# turns raw web pages into object hierarchy and provides selectors (like CSS and Xpath does)
import csv		# simplifies the process of writing data to Comma Separated Values in a file
pagesToScrape = ['http://fresco-movies.surge.sh/']
csvfile = open('data.csv', 'a')
csvwriter = csv.writer(csvfile)
for URL in pagesToScrape:
  webpage = urllib.request.urlopen(URL)
  soup = bs4.BeautifulSoup(webpage, 'html.parser')	
  #title = soup.find('div', {'class':'movie name'}).string
  for item in soup.select('div.lister-item-content'):
    title = item.select_one('h3.lister-item-header').text.strip()
    runtime = item.select_one('span.runtime').text.strip()
    cat = item.select_one('span.genre').text.strip()
    rating = item.select_one('span.certificate').text.strip()
    description_para = item.select_one('div.ratings-bar > p:first-child')
    description = description_para.text.strip()
    director_para = description_para.find_next_sibling('p')
    director = description_para.find_next_sibling('p').a.text.strip()
    votes_para = director_para.find_next_sibling('p')
    votes = director_para.find_next_sibling('p').find('span').find_next('span').text.strip()

    csvwriter.writerow([title,runtime,cat,rating,description,director,votes])		# write a row in the file
	
