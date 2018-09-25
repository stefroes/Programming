import xmltodict

with open('../xml/products.xml') as file:
    articles = xmltodict.parse(file.read())

    for article in enumerate(articles['artikelen']['artikel']):
        print(article[1]['naam'])
