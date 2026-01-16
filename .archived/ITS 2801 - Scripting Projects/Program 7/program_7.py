def csv_to_dict_list(path):
    raw_csv = open(path, mode='r', encoding='utf-8-sig').readlines()

    parsed_csv = []

    for line in raw_csv:
        parsed_csv.append(line.strip().split(','))

    dict_keys = parsed_csv.pop(0)
    dict_list = []

    for item in parsed_csv:
        _item = {}
        for index in range(len(dict_keys)):
            _item.update({dict_keys[index]: item[index]})
        dict_list.append(_item)

    return dict_list


def dict_list_to_file(dict_list, path):
    report = open(path, 'w')

    for item in dict_list:
        report.write(str(item) + '\n')


people = csv_to_dict_list('Program 7/person.csv')
sales = csv_to_dict_list('Program 7/sales.csv')

# This was my first attempt, it would add the entire sales list to person in the report.txt, I could not figure out why
# for person in people:
#     person.update({'purchases':[]})

# for sale in sales:
#     for person in people:
#         if sale['id'] == person['id']:
#             person['purchases'].append(sale)

for person in people:
    # In JS, I would normally do this:
    # purchases = sales.filter(sale => sale['id'] === person['id'])
    # But because Python is a blight from god, you have to do this keyword nonsense to make a filter

    # In Python, lambdas are the equivalent of JS arrow functions
    # JS: param => (condition)
    # Py: lambda param: (condition)
    # filter() doesn't actually do the filtering, it hands you an iterable you can cram into a list constructor

    purchases = list(filter(lambda sale: sale['id'] == person['id'], sales))
    person.update({'purchases': purchases})

dict_list_to_file(people, 'Program 7/report.txt')

for person in people:
    print(person)
