import pandas as pd
from pandasql import sqldf

zara_product_dataset = pd.read_csv('/Users/shinena/dev/Taobao-vs-Western-Fashion-Brands/zara.csv', delimiter = ';')
#print(zara_product_dataset.head())

columnslist = zara_product_dataset.columns
#for col in columnslist :
    #print(col)
#print(chosen_data.head())
prices = """
        SELECT name, price
        FROM zara_product_dataset
        """
category_price = sqldf(prices,locals())
print(category_price.head(10))

bigtops = """
        SELECT name, price
        FROM zara_product_dataset
        WHERE name LIKE '%JACKET%'
            OR name LIKE '%SWEATER%'
            OR name LIKE '%COAT%'
            OR name LIKE '%OVERSHIRT%'
        """
bigtops_result = sqldf(bigtops,locals())
print(bigtops_result.head())

shoes = """
        SELECT name, price
        FROM zara_product_dataset
        WHERE name LIKE '%SHOE%'
        or name LIKE '%SNEAKER%'
        or name LIKE '%BOOT%'
        or name LIKE '%SANDAL%'
        or name LIKE '%SLIDES%'
        """

shoes_result = sqldf(shoes, locals())
print(shoes_result.head(10))

bigbottoms = """
        SELECT name, price
        FROM zara_product_dataset
        WHERE name LIKE '%JEANS%'
        or name LIKE '%PANTS%'
        or name LIKE '%TROUSER%'
        or name LIKE '%SWEATPANTS%'
        or name LIKE '%JOGGERS%'
        """
bigbottoms_result = sqldf(bigbottoms, locals())

smallbottoms = """
                SELECT name, price
                FROM zara_product_dataset
                WHERE name LIKE '%SHORTS%'
                        or name LIKE '%SKIRTS%'
                        or name LIKE '%SKORT%'
                """

smallbottoms_result = sqldf(smallbottoms, locals())


