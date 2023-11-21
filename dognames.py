


dogs = ['Sadie', 'Molly', 'Ella', 'Milo', 'Buddy', 'Rocky', 'Annabelle',
        'Gonzo', 'Sweetie-Pie', 'Diego',]

dogs2 = []


def main():
    how_many = len(dogs)
    print('\nNumber of dogs in the lists: ' + str(how_many))
    print('\nOrginl list of dogs:')
    print(dogs)
    pause = ('\nPress enter to continue')


    dogs.reverse()
    print('\nLists from last to first:')
    print(dogs)
    pause = ('\nPress enter to continue')

    dogs.sort()
    print('\nAlphabetized list:')
    print(dogs)
    pause = ('\nPress enter to continue')

    dogs.sort(reverse = True)
    print('\nList in reverse alphabetized order:')
    print(dogs)
    pause = ('\nPress enter to continue')

    dogs.append('Ranger')
    print('\nAdd a dog to the end of a list:')
    print(dogs)
    pause = ('\nPress enter to continue')

    doggy = dogs.pop(0)
    print('\nPop a dog off (remove) from the front of the list:')
    print(dogs)
    print(doggy + 'was removed from the front of the list.')
    pause = ('\nPress enter to continue')

    another_dog = dogs.pop(3) 
    print('\nNote: Position number in a list begin with 0, not with 1')
    print('Pop a dog off from position 3 (which is the 4th dog) in the list:')
    print(dogs)
    print(another_dog + ' was removed from position 3 in the lists:')
    pause = ('\nPress enter to continue')

    dogs.remove('Annabelle')
    print('\nRemove a dog by name rather than postion in the lists:')
    print(dogs)
    pause = ('\nPress enter to continue')

    dogs2 = dogs 
    print('\nA list can be copied into another list by setting one equal to the other:')
    print(dogs)
    print(dogs2)
    pause = ('\nPress enter to continue')

    print('\nUse a FOR loop to give each dog in the same last name:')
    for i in range(len(dogs)):
        dogs[i] = dogs[i] + ' Timberlake' 
    print(dogs)
    pause = ('\nPress enter to continue')

   
main()
