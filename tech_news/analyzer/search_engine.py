from tech_news.database import search_news
from datetime import datetime


# Requisito 7
def search_by_title(title):
    query = {"title": {"$regex": title, "$options": "i"}}
    news = search_news(query)

    result = []
    for new in news:
        title = new["title"]
        url = new["url"]
        result.append((title, url))

    return result


# Requisito 8
def search_by_date(date):
    try:
        date_obj = datetime.strptime(date, "%Y-%m-%d")
        date_str = date_obj.strftime("%d/%m/%Y")

        query = {"timestamp": {"$eq": date_str}}
        news = search_news(query)

        result = []
        for new in news:
            title = new["title"]
            url = new["url"]
            result.append((title, url))

        return result

    except ValueError:
        raise ValueError("Data inválida")


# Requisito 9
def search_by_category(category):
    query = {"category": {"$regex": category, "$options": "i"}}

    news = search_news(query)

    result = []
    for new in news:
        title = new["title"]
        url = new["url"]
        result.append((title, url))

    return result
