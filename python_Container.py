# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# squares= []
# for n in nums:
#     squares.append(n*n)
# print(squares)


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

#7
#8