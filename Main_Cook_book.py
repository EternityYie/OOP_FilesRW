cook_book = {}

with open('recipes.txt', 'rt', encoding='utf-8') as file:
    for line in file:
        dish_name = line.strip()
        new_list = []
        count = file.readline()
        for i in range(int(count)):
            dish_list = file.readline()
            ingredient_name, quantity, measure = dish_list.strip().split(' | ')
            new_list.append({'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure})
            dep = {dish_name: new_list}
        separate = file.readline()
        cook_book.update(dep)


def list_of_stores_with_ingredients(dishes, person_count):
    total = {}
    for dish in dishes:
        if dish in cook_book:
            for e in cook_book[dish]:
                total: {'measure': cook_book['measure'], 'quantity': (int(cook_book['quantity'])*int(person_count))}
            else:
                print(f'Блюдо "{dish}" не найдено')
    return total

list_of_stores_with_ingredients(["Омлет"], 2)
