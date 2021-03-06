documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006', '5400 028765', '5455 002299'],
    '3': []
}


def get_number():
    doc_number = input('Enter the document number: ')
    return doc_number


def people_output(number_input):
    found = 0
    for document in documents:
        if document["number"] == number_input:
            print(document["name"])
            found = 1
            break
    if not found:
        print('Document not found')


def list_output():
    for document in documents:
        print(document["type"], ' \"', document["number"], '\" \"', document["name"], '\"', sep='')


def shelf_output(number_input):
    found = 0
    for shelf in directories:
        if number_input in directories[shelf]:
            print(shelf)
            found = 1
            break
    if not found:
        print('Document not found')


def add():
    doc_number = get_number()
    doc_type = input('Enter document type: ')
    owner_name = input('Enter name: ')
    shelf = input('Enter directory number: ')
    documents.append({
        "type": doc_type, "number": doc_number, "name": owner_name
    })
    directories[shelf].append(doc_number)
    print('The document has been added')


def delete(number_input):
    found = 0
    for document in documents:
        if document["number"] == number_input:
            documents.remove(document)
            found = 1
            break
    for shelf_content in directories.values():
        if number_input in shelf_content:
            shelf_content.remove(number_input)
            print('The document has been removed')
        break
    for shelf_content in directories.values():
        if number_input in shelf_content:
            shelf_content.remove(number_input)
    if not found:
        print('Document not found')


def add_shelf(shelf_input):
    if shelf_input not in directories.keys():
        directories[shelf_input] = []
    else:
        print('Shelf with this number already exists')


def move(number_input, shelf_input):
    found = 0
    for shelf in directories:
        if number_input in directories[shelf]:
            directories[shelf].remove(number_input)
            found = 1
            if shelf_input not in directories.keys():
                add_shelf(shelf_input)
            directories[shelf_input].append(number_input)
            print('The document has been moved')
            break
    if not found:
        print('Document not found')


def show_owners():
    try:
        for document in documents:
            print(document["name"])
    except KeyError:
        print('No document owner\'s name')


#########################################################################

if __name__ == '__main__':
    command = input('Enter the command: ')
    if command.lower() == 'p':
        number = get_number()
        people_output(number)
    elif command.lower() == 'l':
        list_output()
    elif command.lower() == 's':
        number = get_number()
        shelf_output(number)
    elif command.lower() == 'a':
        add()
    elif command.lower() == 'd':
        number = get_number()
        delete(number)
    elif command.lower() == 'm':
        number = get_number()
        shelf = input('Enter the destination shelf number: ')
        move(number, shelf)
    elif command.lower() == 'as':
        shelf = input('Enter the new shelf number: ')
        add_shelf(shelf)
    elif command.lower() == 'o':
        show_owners()
    else:
        print('Unknown command, please try again')

