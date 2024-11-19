import requests
from bs4 import BeautifulSoup
from collections import defaultdict
import csv


def get_animal_count(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    category_groups = soup.find_all(class_='mw-category-group')

    animal_count = defaultdict(int)

    for group in category_groups:
        for li in group.find_all('li'):
            animal_name = li.get_text(strip=True)
            first_letter = animal_name[0].upper()
            animal_count[first_letter] += 1

    return animal_count


def main():
    base_url = "https://ru.wikipedia.org/w/index.php?title=Категория:Животные_по_алфавиту"

    current_url = base_url

    overall_count = defaultdict(int)

    while current_url:
        print(f"Обработка: {current_url}")
        animal_count = get_animal_count(current_url)

        # Обновляем общий счетчик
        for letter, count in animal_count.items():
            overall_count[letter] += count

        response = requests.get(current_url)
        soup = BeautifulSoup(response.text, 'html.parser')
        next_link = soup.find('a', text='Следующая страница')
        current_url = next_link['href'] if next_link else None

        if current_url and not current_url.startswith('http'):
            current_url = f"https://ru.wikipedia.org{current_url}"

    print("Количество животных по буквам алфавита:")
    for letter in sorted(overall_count.keys()):
        print(f"{letter}: {overall_count[letter]}")

    with open('beasts.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Буква', 'Количество']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for letter, count in sorted(overall_count.items()):
            writer.writerow({'Буква': letter, 'Количество': count})


if __name__ == "__main__":
    main()
