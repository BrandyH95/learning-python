name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

answer = input("You're on a dirt road and it comes to an end. You can go left or right. Which way do you want to go? ").lower()
if answer == "left":

    q2 = input("You come to a river and you can walk around it or swim across. Choose walk or swim: ").lower()
    if q2 == "walk":
        print("You walked for many miles and ran out of water. You lose!")
    elif q2 == "swim":
        print("You tried to swim across and were eaten by an alligator. You lose!")
    else:
        print("Not a valid option. You lose.")

elif answer == "right":

    q2 = input("You come to a bridge. It looks wobbly. Do you try to cross it or turn back? Choose cross or back: ").lower()
    if q2 == "back":
        print("You go back and get lost. You lose!")
    elif q2 == "cross":

        q3 = input("You cross the bridge without incident! You meet a stranger on the other side. Do you talk to them? Choose yes or no: ").lower()
        if q3 == "yes":
            print("You made a new friend that gave you directions to the nearest town. You were able to find shelter and resources. You win!")
        elif q3 == "no":
            print("You ignore the other traveler. You walk further away from civilization and get attacked by wildlife. You lose!")
        else:
            print("Not a valid option. You lose.")

    else:
        print("Not a valid option. You lose.")

else:
    print("Not a valid option. You lose.")

print("Thank you for playing", name + "!")