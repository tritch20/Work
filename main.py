import requests

shop_url = "https://cyclingupgrades.com/products.json"
response = requests.get(shop_url)

if response.status_code == 200:
    data = response.json()
    for product in data["products"]:
        # print(product["title"], "-", product["handle"])
        print(product["title"], "-", product["handle"], "-", product["variants"][0]["price"])

else:
    print("Failed to retrieve products")
