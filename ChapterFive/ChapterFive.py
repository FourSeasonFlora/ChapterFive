#Working from "Python Crash Course" by Eric Matthes
#chapter five - if statments
#
#5-1 conditional tests
print ('Enter treehouse password:')
treehouse = input ()
if treehouse == 'marigold':
    print ('That is correct!\n')
else:
    print ('\nEntry Denied\n')

#5-1b
print ('Enter favorite food:')
favorite_food = input ()
if favorite_food.lower() != 'mac and cheese':
    print ('\nThat is not the best choice\n')
else:
    print ('\nThat is my favorite dish!\n')

#5-1c
print ('Please enter number of cats:')
cat_number = int(input ())
if cat_number < 1:
    print ('That is not enough cats!\n')
elif cat_number > 0 and cat_number < 5:
    print ('That is purrfect!')
else:
    print ('That is too many cats!')