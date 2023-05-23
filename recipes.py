from pattern.text.en import singularize 
recipes={ 
    "omlette": ["egg", "oil","salt"], 
    "chicken fry": ["chicken", "salt", "chilly", "oil"], 
    "samber": [ "tomato", "onion", "potatoes", "garlic"], 
    "sandwich":["bread","cucmber","onion","mayios","tomato sase"],
    "Milk shake":["milk","sugar","mango"] 
    } 

def find_recipes(ingredients): 
    possible_recipes = [] 
    for recipe, recipe_ingredients in recipes.items(): 
        if any(ingredient in ingredients for ingredient in recipe_ingredients): 
            possible_recipes.append(recipe) 
    return possible_recipes 
input_ingredients = singularize(input("Enter the ingredients please separated it by commas: ").replace(" ","").lower())
possible_recipes = find_recipes(input_ingredients) 
if len(possible_recipes) == 0: 
    print("Sorry,no recipe is matched.") 
else: 
    for recipe in possible_recipes: 
        print("With the mentioned Ingredients you can prepare these recipes:",recipe ) 
         

 