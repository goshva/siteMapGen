from msSqlApi import getItems
from sitemapGen import registerSiteMaps

limit= 10
offset=8476423
if __name__ == '__main__':
    registerSiteMaps(getItems(limit,offset))
