'''
"hello", відповідає у консоль "How can I help you?"
"add ...". За цією командою бот зберігає у пам'яті (у словнику наприклад) новий контакт. Замість ... користувач вводить ім'я та номер телефону, обов'язково через пробіл.
"change ..." За цією командою бот зберігає в пам'яті новий номер телефону існуючого контакту. Замість ... користувач вводить ім'я та номер телефону, обов'язково через пробіл.
"phone ...." За цією командою бот виводить у консоль номер телефону для зазначеного контакту. Замість ... користувач вводить ім'я контакту, чий номер треба показати.
"show all". За цією командою бот виводить всі збереженні контакти з номерами телефонів у консоль.
"good bye", "close", "exit" по будь-якій з цих команд бот завершує свою роботу після того, як виведе у консоль "Good bye!".
'''

contacts = {}

def input_error_decorator(func):

    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "This name does not exist."
        except ValueError:
            return "Please enter the name and phone number correctly."
        except IndexError:
            return "Give me a name and a phone number, please."
        
    return wrapper


def hello(*args):
    return "How can I help you?"


@input_error_decorator
def add_contact(data):
    name, phone = data.split()
    contacts[name] = phone
    return f"Added {name} with phone number {phone}"


@input_error_decorator
def change_contact(data):
    name, phone = data.split()
    if name in contacts:
        contacts[name] = phone
        return f"Changed {name}'s phone number to {phone}"
    else:
        return "This name does not exist."


@input_error_decorator
def get_phone(data):
    name = data.strip()
    if name in contacts:
        return f"{name}'s phone number is {contacts[name]}"
    else:
        return "This name does not exist."


def show_all(*args):
    if contacts:
        return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])
    else:
        return "No contacts found."


def exit_bot(*args):
    return "Good bye!"


def main():

    commands = {
        "hello": hello,
        "add": add_contact,
        "change": change_contact,
        "phone": get_phone,
        "show all": show_all,
        "good bye": exit_bot,
        "close": exit_bot,
        "exit": exit_bot
    }

    while True:
        user_input = input("Enter command: ").strip().lower()
        command = None
        data = ""

        for cmd in commands:
            if user_input.startswith(cmd):
                command = cmd
                data = user_input[len(cmd):].strip()
                break

        if command in commands:
            result = commands[command](data)
            print(result)
            if command in ["good bye", "close", "exit"]:
                break
        else:
            print("Unknown command, please try again.")


if __name__ == "__main__":
    main()