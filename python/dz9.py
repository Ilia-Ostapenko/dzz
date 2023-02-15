#def greeting(user):
    #return f'dobriy den,{user}, v yaku gru vu hochete pograti zaraz?-->'


def menu():
    print( """
    menu:
        dodati novu gru: add_game
        vivesti vsi igri: show_games
        vivesti vsi isnuuchi kategorii: show_categories
        vivesti igri po kategorii: show_games_category
    """)

def greeting(user):
    return f'dobriy den,{user}, v yaku gru vu hochete pograti zaraz?-->'


def add_game():
    game_name = input('Enter game name: ')
    category = input('Enter game category: ')
    price = int(input('Enter game price: '))
    description = input('Enter game description: ')
    new_game = {'name': game_name, 'category': category, 'price': price, 'description': description }
    catalog.append(new_game)
    print(f'{game_name} added')
    

def game_categories():
    category = [catalog[category]]
    return category

catalog = []

username = input('enter ur name-->')
print(greeting(username))

while True:
    menu()
    choice = input('choice:')
    if choice == 'add_game':
        add_game()
    elif choice == 'show_games':
        print(catalog)
    elif choice == 'show_categories':
        game_categories()
    else:
        print('Sorry u nas nemae takoi funkctii')

