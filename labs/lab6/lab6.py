from bs4 import BeautifulSoup
import requests
def analyze_news_page(url):
      response = requests.get(url)
      soup = BeautifulSoup(response.content, 'html.parser')
      words = soup.get_text().split()
      word_counts = {}
      for word in words:
          word_counts[word] = word_counts.get(word, 0) + 1
      num_tags = len(soup.find_all())
      num_links = len(soup.find_all('a'))
      num_images = len(soup.find_all('img'))
      return word_counts, num_tags, num_links, num_images
url = "https://www.example.com/news"
results = analyze_news_page(url)
print("Частота слів:", results[0])
print("Кількість HTML-тегів:", results[1])
print("Кількість посилань:", results[2])
print("Кількість зображень:", results[3])