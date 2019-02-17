from bs4 import BeautifulSoup
import requests
import csv

# def match_field( field, prop, attr ):
#     result = []
#     match =  soup.find_all(field, {prop:attr}, text=True)

#     for i in match[0:-3]:
#         result.append(i.string.strip())
#     return result

def build_url(borough, spec ):

    base_url = 'https://www.doctoralia.com.br/local/' + borough.replace(' ', '-') + '-rio-de-janeiro-rj/' + spec
    return base_url, base_url + '/2'

# names = match_field('span', 'itemprop', 'name')
# addr = match_field('span', 'class', 'street')
# espec = match_field('h4', 'class', 'h3 text-muted text-base-size text-base-weight offset-xs-bottom-0 offset-sm-bottom-0')

# result = []
# for i in espec:
#     aux = i.replace('\n', ' ')
#     result.append((aux.replace('\t', '')))
# print(result)

def scrape( url_list ):

    for url in url_list:
        source = requests.get(url).text

        soup = BeautifulSoup( source, 'lxml')


if __name__ == "__main__":


    csv_output = open('info.csv', 'w')
    csv_writer = csv.writer(csv_output, delimiter=';')
    csv_writer.writerow(['Nome', 'Especialidade', 'Endereco'])


    boroughs = ['recreio dos bandeirantes', 
                'barra da tijuca',
                'campo grande',
                'pedra de guaratiba',
                'ilha de guaratiba',
                'vargem grande',
                'vargem pequena',
                'curicica',
                'taquara'
               ]

    spec = ['pediatra',
            'cardiologista',
            'endocrinologista',
            'dentista',
            'fisioterapeuta',
            'pneumologista'
           ]

    urls = []
    for b in boroughs:
        for s in spec:
            first_page, scnd_page = build_url(b, s)
            urls.append(first_page)
            urls.append(scnd_page)


    # data_pointer = zip(names, result, addr)

    # csv_writer.writerows(data_pointer)
    csv_output.close()

