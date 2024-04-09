from celery import shared_task
import requests, pytz, locale, os
from bs4 import BeautifulSoup, Tag
from pprint import pprint
from datetime import datetime, timedelta


locale.setlocale(locale.LC_TIME, 'ru_RU.UTF-8') # the ru locale is installed

def string_to_datetime(time_str):

    # Current date and time
    now = datetime.now(tz = pytz.timezone("Asia/Aqtau"))

    # Extract the date part (either "Сегодня" or "Вчера") and the time part
    date_split = time_str.split()

    date_part = date_split[0]

    if date_part != "Сегодня" and date_part != "Вчера":
        # raise ValueError("Date part must be either 'Сегодня' or 'Вчера'.")
        news_datetime = datetime.strptime(time_str, "%d %B %Y %H:%M")
        # tzinfo = pytz.timezone("Asia/Aqtau")
        # news_datetime = news_datetime.replace(tzinfo = tzinfo)

        return news_datetime

    time_part = date_split[1]

    if date_part == "Сегодня":
        date = now.date()
    elif date_part == "Вчера":
        date = now.date() - timedelta(days=1)

    # Parse the time part
    time = datetime.strptime(time_part, "%H:%M").time()

    # Combine the date and time into a datetime object
    news_datetime = datetime.combine(date, time)
    # tzinfo = pytz.timezone("Asia/Aqtau")
    # news_datetime = news_datetime.replace(tzinfo = tzinfo)

    return news_datetime



@shared_task
def parse_news():
    DOMAIN = "https://tengrinews.kz"

    BACKEND_URL = "http://backend:8000"
    # BACKEND_URL = os.environ.get("BACKEND_URL")

    url = "https://tengrinews.kz/news/"
    page = requests.get(url)

    soup = BeautifulSoup(page.text, "html.parser")

    content_main_item_divs = soup.find_all('div', class_='content_main_item')

    news_urls = []

    # Iterate through each found div and find all 'a' tags within each
    for div in content_main_item_divs:
        # a_tags = div.find_all('a')
        a_tag = div.select_one(".content_main_item_title a")
        img_tag = div.select_one(".content_main_item_img")

        url = f"{DOMAIN}{a_tag.get('href')}"
        image_url = f"{DOMAIN}{img_tag.get('src')}"

        response = requests.post(f"{BACKEND_URL}/api/news/check_url/", data = {
            "url": url
        })

        print(response)
        if response.ok:
            news_urls.append({
                'url': url,
                "image_url": image_url
            })
        else:
            break


    for news_url in news_urls:

        news_page = requests.get(news_url['url'])

        soup = BeautifulSoup(news_page.text, "html.parser")

        title = soup.select_one(".head-single").get_text()
        annotation = soup.select_one(".content_main_desc p").get_text()
        date_time = soup.select_one(".date-time").get_text()
        content = soup.select_one(".content_main_text")

        tags = soup.select(".content_main_text_tags span a")

        filtered_content = []

        for element in content.contents:
            # Check if the element is a Tag and if it's either a <p> or <blockquote>
            if isinstance(element, Tag) and element.name in ['p', 'blockquote']:
                # Append the HTML of the element to the list
                filtered_content.append(str(element))

        news_tags = []

        for tag in tags:
            news_tags.append(tag.get_text())

        news_url.update({
            'title': title,
            'annotation': annotation,
            'datetime': string_to_datetime(date_time),
            'content': " ".join(filtered_content),
            'validated_tags': news_tags
        })

        # pprint(news_url)

        response = requests.post(f"{BACKEND_URL}/api/news/", data = news_url)

        if response.ok:
            print("News inserted!")
        else:
            print("News is not inserted")

        print("\n_______________________________________________________________\n")
