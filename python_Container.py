

#variables 
fruit = ('apples', 'bananas', 'oranges')
fruit_copy = fruit[:]
print(fruit_copy)
 # 1
students =["bob",'kevin','emily']
print(students[1])
print(students[-1])
#2
foods = ("chicken","cheese","cake")
# for idx, foods in enumerate(foods): # use the enumerate with tuples
#     print( "food goes here is a good food")
for food in foods:
    print(f'{food} is a gooood food')
#3

for i in range(-1,-3,-1):
    print(f'{foods[i]}')

#4 Create a dictionary named home_towncontaining the keys of city, stateand population.
# Print a string with this format:
# "I was born in city, state - population of population"
home_town = {
    'city' : "tulsa",
    'state': 'oklahoma',
    'population' : '2.3 million'
}
print(f"I was born in {home_town['city']}, {home_town['state']} - population of {home_town['population']} ")

#5
for x,val in home_town.items():
    print(f"{x} = {val}")
#6
cohort=[]
if len (students) == len(foods):
    l = len(students)
    for i in range(l):
        cohort.append(dict(student=students[i], fav_foods=foods[i]))
        for student_dict in cohort:
            print(student_dict)
#7
awesome_students = []
for student in students:
   awesome_students.append(student + " is awesome!")
for student in awesome_students:
   print(student)

#8
for food in foods:
   if "a" in food:
      print(food)