class VkParse:
    import requests
    from bs4 import BeautifulSoup as bs

    def __init__(self, url: str):
        self.url = url
        self.dct = {"article": '', "image_url_1": '', "image_url_2": ''}

    def run(self) -> dict:
        """requesting func"""
        headers = {'accept': '*/*', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) '
                                                  'Gecko/20100101 Firefox/78.0'

                   }
        session = self.requests.Session()
        r = self.requests.get(self.url, headers=headers)
        if r.status_code == 200:
            soup = self.bs(r.content, "html.parser")
            divs = soup.find_all('div', attrs={"class": "author_page_grid_article"})
            for div in divs:
                links = div.find('a')
                clear_link = links.get("href")
                req = self.requests.get(f"https://vk.com{clear_link}")
                req_soup = self.bs(req.content, "html.parser")
                article = req_soup.find_all("p", attrs={"class": "article_decoration_first article_decoration_last"
                                                                 " article_decoration_before"})
                clean_article = [x.text for x in article]
                print(clean_article)

    def writer_csv(self, file):
        # import csv
        #
        # FILENAME = "users.csv"
        #
        # users = [
        #     {"name": "Tom", "descriptions": "blablablablablbalbalba", "age": 28},
        #     {"name": "Alice", "descriptions": "blablablablablbalbalba", "age": 23},
        #     {"name": "Bob", "descriptions": "blablablablablbalbalba", "age": 34}
        # ]
        #
        # with open(FILENAME, "w", newline="") as file:
        #     columns = ["name", "descriptions", "age"]
        #     writer = csv.DictWriter(file, fieldnames=columns)
        #     # writer.writeheader()
        #
        #     # запись нескольких строк
        #     writer.writerows(users)
        #
        #     # user = {"name": "Sam", "age": 41}
        #     # # запись одной строки
        #     # writer.writerow(user)
        pass


if __name__ == '__main__':
    x = VkParse("https://vk.com/@yvkurse")
    x.run()