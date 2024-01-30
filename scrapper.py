### libraries
import csv
import requests
from bs4 import BeautifulSoup

filename = "movies.csv"
with open(filename, "w", newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Titre", "Réalisateur", "Date de sortie", "Genres", "Résumé", "Note"])

    url_site = 'https://www.senscritique.com/films/sondages'
    response_site = requests.get(url_site)
    html_content_site = response_site.text

    soup_site = BeautifulSoup(html_content_site, "html.parser")


    for link_sondage in soup_site.find_all("a", class_="sc-e6f263fc-0 sc-a0949da7-0 iZcnfH cYbaKn sc-7f2e5247-3 gVquGs"):
        href_sondage = link_sondage.get('href')

        url_sondage = f'https://www.senscritique.com{href_sondage}'

        if (url_sondage == 'https://www.senscritique.com/top/resultats/les_films_les_plus_attendus_de_2024/3637547'):
            print('break')
            continue

        response_sondage = requests.get(url_sondage)
        html_content_sondage = response_sondage.text

        soup_sondage = BeautifulSoup(html_content_sondage, "html.parser")

        for link_film in soup_sondage.find_all("a", class_="sc-e6f263fc-0 sc-a0949da7-1 cTitej eGjRhz sc-4495ecbb-3 hCRsTs"):

            href_film = link_film.get('href')

            url_film = f'https://www.senscritique.com{href_film}'

            response_film = requests.get(url_film)
            html_content_film = response_film.text

            soup_film = BeautifulSoup(html_content_film, "html.parser")


            title = soup_film.find('h1', class_="sc-e6f263fc-1 sc-842a8720-1 bwGoop dBdZmZ").text
            realisateur = soup_film.find('a', class_="sc-e6f263fc-0 sc-a0949da7-0 GItpw eShzae").text
            date = soup_film.find('p', class_="sc-e6f263fc-1 sc-842a8720-13 dkHTDU cuIThM").text
            genres = []
            for genre in soup_film.find('span', class_="sc-fa5905bc-4 dnsVaH").find_all('a', class_="sc-e6f263fc-0 sc-a0949da7-0 iZcnfH eShzae"):
                genres.append(genre.text)
            description = soup_film.find('p', class_="sc-e6f263fc-0 sc-2249ea1-0 iZcnfH eqBLlB").text
            note = soup_film.find('div', class_="sc-8251ce8c-5 fdoSxm").text

            print([title, realisateur, date, genres, description, note])
            writer.writerow([title, realisateur, date, genres, description, note])
