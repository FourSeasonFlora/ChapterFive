#5-1c
garden_veg = ['corn','cabage','kale','beet']
vegetable = input ('Please enter the vegetable you would like to check: ')
if vegetable.lower() in garden_veg:
    print (f'{vegetable.title()} is avaliable\n')
else:
    print ('\nThat option is not avaliable\n')

#5-1d
fruit_plants = ['strawberry','strawberries','blueberry', 'blueberries', 'apples','apple','grapes','grape']
fruits = input ('Please enter the fruit plants you would like to check for: ')
if fruits.lower() not in fruit_plants:
    print ('\nThe selected fruit is/are not avaliable to grow.\n')
else:
    print(f'{fruits.title()} is/are avaliable to grow.\n')

#5-2
age = int(input ('Please enter your age: '))
if age <= 10:
    print ('Your admission is free!\n')
elif age <= 16:
    print ('Your admission cost is $2.\n')
elif age >= 60:
    print ('Your admission is free!')
else:
    print ('Your admission cost is $5.\n')

#5-3
grocries = input ('\nPlease enter the item needed:')
if grocries.lower() == 'milk':
    print (f'{grocries.title()} is on the permanent list.\n')
elif grocries.lower() == 'eggs':
    print (f'{grocries.title()} are on the permanent list.\n')
else:
    print ('\nThis item can not be added to the list.\n')

#5-3b
grocery = ['milk', 'eggs', 'bread', 'cheese']
food = input ('Please enter the item needed: ')
if food.lower() in grocery:
    print (f'{food.title()} is already on the list.\n')
if food.lower() not in grocery:
    print (f'{food.title()} is not on the list.\n')

#5-3c
foods = input ('Please enter the item needed: ')
if foods.lower () in grocery:
    print (f'{foods.title()} is already on the list.\n')
else:
   print (f'{foods.title()} is not on the list.\n')

avaliable = ['marigolds', 'calendula', 'nastirtums', 'lupine']
flowers = input ("Please enter the flowers you would like to grow:\n")
if flowers in avaliable:
        print (f'{flowers.title()} is avaliable to plant.')
else:
        print (f'{flowers.title ()} is not avaliable to plant.')