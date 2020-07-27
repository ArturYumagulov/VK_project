class VkParse:
    """Класс для парсинга канала @Yvkurse"""
    import requests
    from bs4 import BeautifulSoup as bs
    import csv

    def __init__(self):
        self.url = "https://vk.com/@yvkurse"
        self.dct = {"article": '', "image_url_1": ''}

    def scaning(self):
        print("Сканирование.....")
        headers = {'accept': '*/*', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) '
                                                  'Gecko/20100101 Firefox/78.0'

                   }
        session = self.requests.Session()
        r = self.requests.get(self.url, headers=headers)
        if r.status_code == 200:
            soup = self.bs(r.content, "html.parser")
            divs = soup.find_all('div', attrs={"class": "author_page_grid_article"})
            filename = 'yvkurse_scan.csv'
            for div in divs:
                with open(filename, 'a', newline='', encoding='utf-8') as file:
                    links = div.find('a')
                    clear_link = links.get("href")
                    req = self.requests.get(f"https://vk.com{clear_link}")
                    req_soup = self.bs(req.content, "html.parser")
                    article = req_soup.find_all("p", attrs={"class": "article_decoration_first article_decoration_last"
                                                                     " article_decoration_before"})
                    clean_article = [x.text for x in article]
                    string = ''
                    for i in clean_article:
                        string += i
                    self.dct['article'] = string
                    image = req_soup.find_all('div', attrs={"class": "article_object_sizer_wrap"})
                    check = 1
                    for i in image:
                        if check <= len(image):
                            clear = i.get('data-sizes')
                            img = clear.rfind('https')
                            end = clear.rfind('"')
                            self.dct[f'image_url_{check}'] = clear[img:end].replace('\/', '/')
                            check += 1
                        columns = [x for x in self.dct.keys()]
                    writer = self.csv.DictWriter(file, fieldnames=columns)
                    writer.writerow(self.dct)
        print("Файл успешно записан!")


if __name__ == '__main__':
    x = VkParse()
    x.scaning()