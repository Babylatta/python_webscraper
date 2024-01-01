import requests
from bs4 import BeautifulSoup


results = []


def extract_remoteOK_jobs(keyword):
    base_url = "https://remoteok.com/remote-"
    response = requests.get(
        f"{base_url}{keyword}-jobs",
        headers={
            "User-Agent":
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        })

    soup = BeautifulSoup(response.content, 'html.parser')
    jobs = soup.find("table", id="jobsboard").find_all("tr", class_="job")

    for job in jobs:
      company = job.find("h3", itemprop="name")
      position = job.find("h2", itemprop="title")
      location = job.find("div", class_="location")
      link = job.find("a", class_="preventLink")['href']

      job_data = {
          "company": company.text.strip(),
          "position": position.text.strip(),
          "location": location.text.strip(),
          "link": f"https://remoteok.com{link}",
      }

      results.append(job_data)

    return results
