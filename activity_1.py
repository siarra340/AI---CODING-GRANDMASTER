pasta = ("Pasta Arrabiata", "Italian", 20, "Medium")
biryani = ("Chicken Birynai", "Indian", 45, "Hard")
print("Recipe 1:", pasta)
print(f"Name: {pasta[0]}")
print("Cusine:", pasta[1])
print(f"Difficulity: {pasta[-1]}")

all_recipes = (pasta, biryani)
print("\nFirst recipe name:", all_recipes[0][0])
print("Second recipe time:", all_recipes[1][2], "mins")
print("Pasta details (sliced):", pasta[1:3])

print("\nPasta Recipe details:")
for details in pasta:
    print(" -", details)

pasta_ingredients = {"tomato", "garlic", "olive oil", "chili", "pasta", "garlic"}
biryani_ingredients = {"rice", "chicken", "garlic", "onion", "tomato", "spices"}
print("\nPasta ingredients:", pasta_ingredients)
print(f"Biryani ingredients: {biryani_ingredients}")
print("Total pasta ingredients:", len(pasta_ingredients))

pasta_ingredients.add("parmesan")
pasta_ingredients.discard("chili")
print("\nUpdated pasta ingredients:", pasta_ingredients)

all_ingredients = pasta_ingredients.union(biryani_ingredients)
common = pasta_ingredients.intersection(biryani_ingredients)
only_biryani = biryani_ingredients.difference(pasta_ingredients)
unique_to_each = pasta_ingredients.symmetric_difference(biryani_ingredients)

print("\nAll ingredients (union):", all_ingredients)
print(f"Common ingredients (intersection): {common}")
print(f"Only in Biryani (difference): {only_biryani} ")
print("Not shared (sym. difference):", unique_to_each)
