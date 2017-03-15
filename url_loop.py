# Generates URL's for scraping
import sys
from config import *

manifest_url = url

sys.stdout = open('url.txt', 'w')

for i in range(499, 12093):
    string = str(i)
    print manifest_url + string
