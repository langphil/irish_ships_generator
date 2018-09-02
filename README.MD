# Scraper / Tweet generator for Irish Ships
Scripts for scraping, formatting and tweeting for the Irish Ships Twitter bot.

## Scraping (scraper.py)
Loops through a range of URL's, identifies table element and scrapes 50 rows, writing them to CSV.

## Formatting (formatter.py)
Manipulates CSV data and outputs .txt file with individual tweets per row.

## Tweeting (tweeter.py)
Update Twitter status with row from .txt file.

## Dependencies
* Selemium
* BeautifulSoup 4
* Pandas
* Tweepy

### Notes
* Scraped up to page 1994 (20180902)
