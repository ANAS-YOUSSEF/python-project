weather = int(input('please enter the current temperature in celsius:'))

if weather >= 30:
    print("it’s a hot day. stay hydrated!")
elif weather >= 20 and weather <= 30:
    print("it’s a warm day. Enjoy the weather!")
elif weather >= 10 and weather <= 201:
    print("it’s a cool day. Wear a jacket!")
else:
    print("it’s a cold day. Stay warm!")