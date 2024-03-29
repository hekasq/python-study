import requests


class Scraper:
    base_url = "https://www.billboard.com/charts/hot-100/"

    def scrape(self, date):
        try:
            response = requests.get(self.base_url+date, verify=0)
            with open('outputs.txt', mode='w+') as output:
                output.write(str(response.text))
            return response.text

        except Exception as e:
            "Error, error"
            print(e)
