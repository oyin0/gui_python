from functions import subject, classmark, location

def choice():
    select = int(input('You have been provided with 3 options. \n \
        Type "1" for subject name. \n \
        Type "2" for a classmark. \n \
        Type "3" for location. Thank you!  '))

    if select == 1:
        subjectin = input('Type in your full or part subject name please: ').upper()
        result = subject(subjectin)
        print(result)

    elif select == 2:
        classmarkin = input('Type in your classmark please: ').upper()
        result = classmark(classmarkin)
        print(result)

    elif select == 3:
        locationin = input('Type in your location please. \n \
        Hint: The locations available at the library include, \n \
                Ground Floor \n \
                Middle Floor \n \
                Top Floor Front Right \n \
                Top Floor Front Left \n \
                Top Floor Back Right \n \
                Top Floor Back Left' ).upper()
        result = location(locationin)
        print(result)

    else:
        print('You have provided an invalid option. Check the instructions given and input a valid option. Thank you')
        return choice()

choice()
        
