
from bs4 import BeautifulSoup

FILE_FUTURES_PRICES = "Three-Month SOFR Futures Quotes - CME Group.html"
FILE_EXPIRY_DATES = "Three-Month SOFR Futures Calendar - CME Group.html"

MONTHS = ('mar', 'jun', 'sep', 'dec')

def get_futures_prices(fname: str):
    d = {}

    with open(fname, encoding='utf8') as f:  
        soup = BeautifulSoup(f, 'html.parser')
    
    table = soup.tbody
    for row in table.contents:
        tds = row.find_all('td')
        month = row.b.string.lower()
        price = float(tds[5].div.string)
        
        d[month] = price

        if any(substring in month for substring in MONTHS):
            print(price)
    
    return d

def get_expiry_dates(fname: str):
    with open(fname, encoding='utf8') as f:
        soup = BeautifulSoup(f, 'html.parser')

    table = soup.tbody

    lst = []
    for row in table.contents:
        tds = row.find_all('td')
        month = tds[0].string.lower()
        date = tds[3].string.lower()

        lst.append((month, date))

    relevant_months_lst = [row for row in lst if any(substring in row[0] for substring in MONTHS)]
    for row in relevant_months_lst:
        print(row[1])
    
    return relevant_months_lst

def main(): 
    d = get_futures_prices(FILE_FUTURES_PRICES)
    lst = get_expiry_dates(FILE_FUTURES_PRICES)

if __name__ == "__main__":
    main()

