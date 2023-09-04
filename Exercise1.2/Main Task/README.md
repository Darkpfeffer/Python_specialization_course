## Inner Container Data Type Consideration
I decided to use dictionaries to store the recipes' data since I can use every data as a key-value pair, which makes it clear to everyone which value belongs to which key. As I imagined using a list or tuple to solve the problem, it seemed too complicated to execute. For ‘ingredients’ I used list as a value, but if there will be a measurement of the ingredient, I would use dictionary there as well.

## Outer Container Data Type Consideration
For the outer container, I chose to add recipes to a list, since they don’t need keys to be identified (they already have a ‘name’ key inside the recipe), and lists are modifiable, so updating later won’t be a challenge.