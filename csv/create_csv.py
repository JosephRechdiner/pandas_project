import pandas as pd

data = {
    "id": list(range(1, 26)),
    "name": [
        "Apple", "Banana", "Orange", "Milk", "Cheese", "Yogurt", "Bread", "Croissant",
        "Butter", "Chicken", "Beef", "Pork", "Rice", "Pasta", "Tomato", "Potato",
        "Carrot", "Lettuce", "Apple Juice", "Orange Juice", "Water", "Soda",
        "Chocolate", "Chips", "Nuts"
    ],
    "price": [
        2.5, 1.2, 3.0, 4.5, 8.0, 3.5, 2.0, 2.8, 5.0, 10.0, 12.0, 9.5, 1.5, 2.0,
        1.8, 1.0, 0.9, 1.5, 3.0, 3.2, 0.8, 1.5, 2.5, 1.7, 4.0
    ],
    "quantity": [
        100, 150, 80, 50, 30, 60, 120, 40, 25, 20, 15, 10, 200, 180, 90, 100, 80, 50,
        70, 65, 300, 150, 60, 80, 40
    ],
    "category": [
        "Fruit", "Fruit", "Fruit", "Dairy", "Dairy", "Dairy", "Bakery", "Bakery",
        "Dairy", "Meat", "Meat", "Meat", "Grain", "Grain", "Vegetable", "Vegetable",
        "Vegetable", "Vegetable", "Beverage", "Beverage", "Beverage", "Beverage",
        "Snack", "Snack", "Snack"
    ]
}

df = pd.DataFrame(data)
df.to_csv("csv\products.csv", index=False)