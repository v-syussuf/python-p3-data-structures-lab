spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    names = [food['name'] for food in spicy_foods]
    return names

spicy_foods = [
    {"name": "Green Curry", "spiciness": "Medium"},
    {"name": "Buffalo Wings", "spiciness": "Hot"},
    {"name": "Mapo Tofu", "spiciness": "Spicy"}
]

result = get_names(spicy_foods)
print(result)

def get_spiciest_foods(spicy_foods):
    spiciest_foods = [food for food in spicy_foods if food.get("heat_level", 0) > 5]
    return spiciest_foods

spicy_foods = [
    {"name": "Green Curry", "cuisine": "Thai", "heat_level": 9},
    {"name": "Buffalo Wings", "cuisine": "American", "heat_level": 3},
    {"name": "Mapo Tofu", "cuisine": "Sichuan", "heat_level": 6}
]

result = get_spiciest_foods(spicy_foods)
print(result)


def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        heat_level = "🌶" * food.get("heat_level", 0)
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_level}")

spicy_foods = [
    {"name": "Green Curry", "cuisine": "Thai", "heat_level": 9},
    {"name": "Buffalo Wings", "cuisine": "American", "heat_level": 3},
    {"name": "Mapo Tofu", "cuisine": "Sichuan", "heat_level": 6}
]

print_spicy_foods(spicy_foods)

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food
    return None  

spicy_foods = [
    {"name": "Green Curry", "cuisine": "Thai", "heat_level": 9},
    {"name": "Buffalo Wings", "cuisine": "American", "heat_level": 3},
    {"name": "Mapo Tofu", "cuisine": "Sichuan", "heat_level": 6}
]

result1 = get_spicy_food_by_cuisine(spicy_foods, "American")
print(result1)

result2 = get_spicy_food_by_cuisine(spicy_foods, "Thai")
print(result2)

def print_spiciest_foods(spicy_foods):
   for food in spicy_foods:
        heat_level = "🌶" * food.get("heat_level", 0)
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_level}")

def get_spiciest_foods(spicy_foods):
    return [food for food in spicy_foods if food.get("heat_level", 0) > 5]

spicy_foods = [
    {"name": "Green Curry", "cuisine": "Thai", "heat_level": 9},
    {"name": "Buffalo Wings", "cuisine": "American", "heat_level": 3},
    {"name": "Mapo Tofu", "cuisine": "Sichuan", "heat_level": 6}
]

spiciest_foods = get_spiciest_foods(spicy_foods)
print_spicy_foods(spiciest_foods)

def get_average_heat_level(spicy_foods):
    total_heat_level = sum(food.get("heat_level", 0) for food in spicy_foods)
    spicy_foods = len(spicy_foods)

    if spicy_foods == 0:
        return 0  

    average_heat = total_heat_level / spicy_foods
    return int(average_heat)


def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)

existing_spicy_foods = [
    {"name": "Green Curry", "cuisine": "Thai", "heat_level": 9},
    {"name": "Buffalo Wings", "cuisine": "American", "heat_level": 3},
    {"name": "Mapo Tofu", "cuisine": "Sichuan", "heat_level": 6}
]

new_spicy_food = {"name": "Spicy Ramen", "cuisine": "Japanese", "heat_level": 7}

create_spicy_food(existing_spicy_foods, new_spicy_food)

print(existing_spicy_foods)
