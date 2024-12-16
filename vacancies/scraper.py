```python
import httpx
from bs4 import BeautifulSoup

def scrape_work_ua(query):
    base_url = "https://www.work.ua/jobs/"
    params = {"q": query}
    response = httpx.get(base_url, params=params)
    soup = BeautifulSoup(response.text, "html.parser")

    vacancies = []
    for vacancy in soup.select(".job-link"):
        title = vacancy.select_one("h2").text.strip()
        link = "https://www.work.ua" + vacancy["href"]
        company = vacancy.select_one(".add-top-xs").text.strip()
        vacancies.append({"title": title, "company": company, "link": link, "source": "Work.ua"})

    return vacancies

def scrape_rabota_ua(query):
    base_url = "https://rabota.ua/zapros/"
    search_query = query.replace(" ", "-")
    url = f"{base_url}{search_query}"
    response = httpx.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    vacancies = []
    for vacancy in soup.select(".card-body"):
        title = vacancy.select_one(".card-title a").text.strip()
        link = "https://rabota.ua" + vacancy.select_one(".card-title a")["href"]
        company = vacancy.select_one(".company-name").text.strip()
        vacancies.append({"title": title, "company": company, "link": link, "source": "Rabota.ua"})

    return vacancies