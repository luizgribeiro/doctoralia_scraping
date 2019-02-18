from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd

def match_field( field, prop, attr, bs4handler ):
    result = []
    match =  bs4handler.find_all(field, {prop:attr}, text=True)

    for i in match[0:-3]:
        result.append(i.string.strip())
    return result

def build_url(borough, spec ):

    base_url = 'https://www.doctoralia.com.br/local/' + borough.replace(' ', '-') + '-rio-de-janeiro-rj/' + spec
    return base_url, base_url + '/2'

def scrape(url):

    htm_params = [
                    ['span', 'itemprop', 'name'],
                    ['span', 'class', 'street'],
                    ['h4', 'class', 'h3 text-muted text-base-size text-base-weight offset-xs-bottom-0 offset-sm-bottom-0']
                 ]

    try:
        source = requests.get(url).text
        soup = BeautifulSoup( source, 'lxml')

        columns = []
        for param in htm_params: 
            if param[0] == 'h4':
                aux = []
                for string in match_field(*param, soup):
                    aux.append(string.replace('\n', ' ').replace('\t', ''))
                columns.append(aux)
            else:
                columns.append(match_field(*param, soup))
        return columns
    except:
        print("Exception raised")
        pass


if __name__ == "__main__":


    csv_output = open('info.csv', 'w')
    csv_writer = csv.writer(csv_output, delimiter=';')
    csv_writer.writerow(['Nome', 'Endereco', 'Especialidade'])


    boroughs = ['recreio dos bandeirantes', 
                'barra da tijuca',
                'campo grande',
                'pedra de guaratiba',
                'ilha de guaratiba',
                'vargem grande',
                'vargem pequena',
                'curicica',
                'taquara',
                'campo grande',
                'freguesia'
               ]

    spec = ['pediatra',
            'cardiologista',
            'endocrinologista',
            'fisioterapeuta',
            'pneumologista',
            'otorrino'
           ]

    urls = []
    for b in boroughs:
        for s in spec:
            first_page, scnd_page = build_url(b, s)
            urls.append(first_page)
            urls.append(scnd_page)

    counter = 1 
    for url in urls:
        
        print(url)
        result = scrape(url)
        data = zip(*result)
        print(f"------------------------ couter = {counter} of  {len(urls)}")
        counter = counter + 1

        for row in data:
            csv_writer.writerows(data)

    csv_output.close()
