import codecademylib
import pandas as pd

inventory = pd.read_csv('inventory.csv')
staten_island = (inventory.head(10))

product_request = staten_island.product_description

seed_request = inventory[(inventory.location == 'Brooklyn') | (inventory.product_type == 'seeds')]

inventory['in_stock'] = lambda x: 'True' if quantity > 0 else 'False'
inventory['total_value'] = inventory.price * inventory.quantity

combine_lambda = lambda row: '{} - {}'.format(row.product_type, row.product_description)

inventory['full_description'] = inventory.apply(combine_lambda, axis=1)

print(inventory.head(10))