# Define the group of acquaintances
week3_group = [
    {
        "name": "Jill",
        "age": 26,
        "job": "biologist",
        "connections": [{"name": "Zalika", "relationship": "friend"}, {"name": "John", "relationship": "partner"}]
    },
    {
        "name": "Zalika",
        "age": 28,
        "job": "artist",
        "connections": [{"name": "Jill", "relationship": "friend"}]
    },
    {
        "name": "John",
        "age": 27,
        "job": "writer",
        "connections": [{"name": "Jill", "relationship": "partner"}]
    },
    {
        "name": "Nash",
        "age": 34,
        "job": "chef",
        "connections": [{"name": "John", "relationship": "cousin"}, {"name": "Zalika", "relationship": "landlord"}]
    }
]


# my_group =
# Print function to display information about each person
def print_group_info(group):
    for person in group:
        print(f"{person['name']} is {person['age']}, a {person['job']} and")
        if person["connections"]:
            for connection in person["connections"]:
                print(f" {connection['relationship']} with {connection['name']}")
        else:
            print("has no connections")
        print()  # Blank line for better readability

# for person1 in week3_group:
#         if person1["connection"] forget(person1,person2):
#         for perctions"]:
#             person1.__reduce__()
def max_age():
    eldest = max(week3_group,key=lambda person:person['age'])
    print(f'The eldest person is {eldest['name']} with an age of {eldest['age']}')

def mean_relations():
    for person in week3_group:
        relation_numbers = sum(len (person['connections']) )
# Example usage
print_group_info(week3_group)
max_age()
