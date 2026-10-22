import os
import sys
import requests   
from requests_html import HTML
import pandas as pd

def url_to_txt(url, filename="Top anime.html", save=False):
    r = requests.get(url)
    if r.status_code == 200:
        html_text = r.text
        if save:
            with open(f"Top.html", 'w') as f:
                f.write(html_text)
        return html_text
    print("Failed")
    sys.exit(1)


def parse_and_extract(url ,pages):
    html_text = url_to_txt(url)
    html_r = HTML(html=html_text)
    Table = html_r.find(".top-ranking-table")
    
    parsed_table = Table[0]
    rows = parsed_table.find('tr')
    headers = rows[0]
    headers_name = headers.text.split('\n')[:3]
    data = []
    
    for row in rows[1:]:
        #print(a)
        anime_data = []
        cols = row.find('td')
        for col in cols:
            if col.text == 'N/A' or col.text == 'Add to list':
                continue
            if len(col.text)< 50 :
                anime_data.append(col.text)     
            else:
                anime_data.append(col.text.split("\n")[0])
        data.append(anime_data)
    return (headers_name, data, pages)

def to_csv(url ,pages):
	file_path = f'/home/imad/Document/Projects/Top-anime/Data/Raw Data/Top anime P:{pages+1}.csv'

	if not os.path.exists(file_path):
	    header, Data , pages = parse_and_extract(url, pages)
	    df = pd.DataFrame(Data, columns=header)

	    df.to_csv(file_path, index=False)
	    return True, file_path
	return False, file_path

def run(pages):
    assert isinstance(pages, int)
    for i in range(0, pages):
        limet = i*50
        url = f'https://myanimelist.net/topanime.php?limit={limet}'
        r, file = to_csv(url ,pages=i)
        
        if r :
            print("Complete page: ",file)

        else:
            print("skipped page: ", file)

if __name__ == "__main__":
	run(10000)