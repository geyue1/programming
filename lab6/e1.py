'''

You are given a list of full names of people. Each full name consists of two words: first name and last name. Using list comprehension, produce two lists:

List of surnames, e.g. ['Johnson', 'Truss', 'Sunak']
List of the initials with surnames, e.g. ['B. Johnson', 'L. Truss', 'R. Sunak']
'''

people = ["Boris Johnson", "Liz Truss", "Rishi Sunak"]

surnames = [str.split(" ")[1] for str in people]

print(f"surnames:{surnames}")

names_with_initials = [list(str)[0]+". "+ str.split(" ")[1] for str in people]

print(f"names_with_initials:{names_with_initials}")
