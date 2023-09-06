""""
У нас есть функции для работы с пользователем, но хочется работать с ним через класс.

Задания:
    1. Создайте класс User и перенесите всю логику работы с пользователем туда.
"""





def generate_short_user_description(username: str, user_id: int, name: str):
    return f'User with id {user_id} has {username} username and {name} name'


class User:
    # Я не очень понял задание, как по мне правильнее просто в объявлении атрибутов, просто бахнуть self.username = username.capitalized() и не париться
    def __init__(self, user_id: int, username: str, name: str):
        self.user_id = user_id
        self.username = username
        self.name = name
    
    def make_username_capitalized(self):
        self.username = self.username.capitalize()

    def generate_short_user_description(self):
        return f'User with id {self.user_id} has {self.username} username and {self.name} name'    
    
if __name__ == '__main__':
    person = User(1, 'billiejinn', 'pavel')
    print(person.make_username_capitalized())
    print(person.generate_short_user_description())