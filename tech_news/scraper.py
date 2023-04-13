import time
import requests
from parsel import Selector


# Requisito 1
def fetch(url):
    time.sleep(1)
    try:
        page = requests.get(url, headers={"user-agent": "Fake user-agent"},
                            timeout=3)
        if page.status_code == 200:
            return page.text
        else:
            return None
    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_updates(html_content):
    selector = Selector(text=html_content)
    container = selector.css("div.archive-main h2 a::attr(href)").getall()
    if container:
        return container
    else:
        return []


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    next_page_url = selector.css(
        "div.nav-links a.next.page-numbers::attr(href)"
        ).get()
    return next_page_url


# Requisito 4
def scrape_news(html_content):
    selector = Selector(text=html_content)

    url = selector.css("head link[rel=canonical]::attr(href)").get()

    title = selector.css(
        "div.entry-header-inner h1.entry-title::text"
        ).get().strip()

    timestamp = selector.css(
        "div.entry-header-inner ul.post-meta li.meta-date::text"
        ).get()

    writer = selector.css(
        "div.entry-header-inner ul.post-meta li.meta-author a.url.fn.n::text"
        ).get()

    reading_time = selector.css(
        "div.entry-header-inner ul.post-meta li.meta-reading-time::text"
        ).get().strip()
    reading_time = int(reading_time.split()[0]) if reading_time else 0

    summary = selector.css(
        "div.entry-content p"
        ).xpath("string()").get().strip()

    category = selector.css(
        "div.entry-header-inner a.category-style span.label::text"
        ).get()

    news_dict = {
            'url': url,
            'title': title,
            'timestamp': timestamp,
            'writer': writer,
            'reading_time': reading_time,
            'summary': summary,
            'category': category
        }

    return news_dict


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
