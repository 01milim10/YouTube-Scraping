from bs4 import BeautifulSoup

with open('home.html', 'r') as html_file:
    content = html_file.read()

    soup = BeautifulSoup(content, 'lxml')

    courses_html_tags = soup.find_all('h5')
    for course in courses_html_tags:
        print(course.text)

    courses_price_tag = soup.find_all('a')
    for price in courses_price_tag:
        print(price.text)

    courses_cards = soup.find_all('div', class_='card')
    for card in courses_cards:
        course_name = card.h5.text
        course_price = card.a.text.split()[-1]
        print(f'{course_name} costs {course_price}')
