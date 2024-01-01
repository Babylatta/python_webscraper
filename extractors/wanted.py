from playwright.sync_api import sync_playwright
import time
from bs4 import BeautifulSoup


results = []
def extract_wanted_jobs(keyword):
    p = sync_playwright().start()

    browser = p.chromium.launch(headless=True)

    page = browser.new_page()

    page.goto(f"https://www.wanted.co.kr/search?query={keyword}&tab=position") 

    # time.sleep(5)

    # page.click("button.Aside_searchButton__Xhqq3")

    # time.sleep(5)

    # page.get_by_placeholder("검색어를 입력해 주세요.").fill("flutter")

    # time.sleep(5)

    # page.keyboard.down("Enter")

    # time.sleep(5)

    # page.click("a#search_tab_position")


    for x in range(5):

        time.sleep(5)
        page.keyboard.down("End")


    content = page.content()
    

    p.stop()

    soup = BeautifulSoup(content, "html.parser")
    jobs = soup.find_all("div", class_="JobCard_container__FqChn")

    
    
    for job in jobs:
        link = f"https://www.wanted.co.kr{job.find('a')['href']}"
        position = job.find("strong", class_="JobCard_title__ddkwM").text
        company = job.find("span", class_="JobCard_companyName__vZMqJ").text
        location = job.find("span", class_="JobCard_location__2EOr5").text
        job_data = {
            "position":position,
            "company":company,
            "location":location,
            "link":link,
        }
       
        results.append(job_data)
    
    return results

