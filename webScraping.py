from bs4 import BeautifulSoup
import requests
import time

print('Put some skills that you are not familiar with')
unfamiliar_skill = input(">")
print(f'Filtering out {unfamiliar_skill}')


def find_jobs():
    html = requests.get(
        'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=')

    soup = BeautifulSoup(html.text, 'lxml')

    jobs = soup.find_all('li', class_="clearfix job-bx wht-shd-bx")
    for index, job in enumerate(jobs):
        published_date = job.find('span', class_="sim-posted").span.text
        if 'few' in published_date:

            company_name = job.find(
                'h3', class_="joblist-comp-name").text.replace(' ', '')
            skills = job.find(
                'span', class_='srp-skills').text.replace(' ', '')
            more_info = job.header.h2.a['href']
            if unfamiliar_skill not in skills:

                # print(published_date)

                # Writing in tripple quotes will print in separated lines

                # print(f'''
                #       Company Name: {company_name}
                #       Required Skills: {skills}
                #       ''')

                with open(f'posts/{index}.txt', 'w') as file:

                    file.write(f"Company Name: {company_name.strip()}\n")
                    file.write(f"Required Skills: {skills.strip()}\n")
                    file.write(f"More Info: {more_info}\n")
                print(f'File Saved: {index}')


if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f'Waiting {time_wait} minutes...')
        time.sleep(time_wait * 60)
