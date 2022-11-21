# If you
import random
# then use random.randrange(2).

# If you do
from random import randrange
# then use randrange(2)
# directly.

# You could use
import random as r


# to create a shorthand or an alias for random.

def blackjack_hand(player_hand, dealer_hand):
    '''Print "The player wins!" under the condition
    that the player hand is greater than the dealer hand
    and the player hand is less than or equal to 21.'''
    if (player_hand > dealer_hand) and (player_hand <= 21):
        print("The player wins!")
    # A function always returns at the end.
    # We could show this explicitly.
    return


# blackjack_hand(17, 21)

# blackjack_hand(21, 17)

def blackjack_hand2(player_hand, dealer_hand):
    '''Return the string "The player wins!" under the condition
    that the player hand is greater than the dealer hand
    and the player hand is less than or equal to 21.'''
    if (player_hand > dealer_hand) and (player_hand <= 21):
        return "The player wins!"
    else:
        return "Inconclusive"


def main():
    # The returned value from the type function
    # replaces the function call.
    type("The player loses!")

    # You have to print a returned value in order to see it.
    print(type("The player loses!"))

    # The returned value from the randrange function
    # replaces the function call.
    r.randrange(2)

    # You have to print a returned value in order to see it.
    print(r.randrange(2))


# The returned value from the blackjack_hand2 function
# replaces the function call.
# blackjack_hand2(21, 17)

# You have to print a returned value in order to see it.
# print(blackjack_hand2(21, 17))

# print(blackjack_hand2(17, 21))

def blackjack_hand3(player_hand, dealer_hand):
    '''Return the boolean True under the condition
    that the player hand is greater than the dealer hand
    and the player hand is less than or equal to 21.
    Otherwise, it returns False.'''
    if (player_hand > dealer_hand) and (player_hand <= 21):
        return True
    else:
        return False


# print(blackjack_hand3(21, 17))

# print(blackjack_hand3(17, 21))

# print(f'The condition was met for a win: {blackjack_hand3(21, 17)}')
# print(f'The condition was met for a win: {blackjack_hand3(17, 21)}')


def blackjack_hand4(player_hand, dealer_hand):
    '''Return whether the condition is met
    that the player hand is greater than the dealer hand
    and the player hand is less than or equal to 21.'''
    return (player_hand > dealer_hand) and (player_hand <= 21)


# print(blackjack_hand4(21, 17))

# print(blackjack_hand4(17, 21))

# print(f'The condition was met for a win: {blackjack_hand4(21, 17)}')
# print(f'The condition was met for a win: {blackjack_hand4(17, 21)}')

def blackjack_hand5(player_hand, dealer_hand):
    '''Return whether the condition is met
    that the player hand is greater than the dealer hand
    and the player hand is less than or equal to 21.'''
    # x is only a local value.
    # It's only known in the context of the function.
    # It's not known outside of the function call to blackjack_hand5.
    # In addition, for appropriately streamlined code,
    # return the value directly from the function, rather than
    # introducing an intermediate variable like x, as is
    # unnecessarily done here:
    x = (player_hand > dealer_hand) and (player_hand <= 21)
    return x


print(blackjack_hand5(21, 17))

print(blackjack_hand5(17, 21))

print(f'The condition was met for a win: {blackjack_hand5(21, 17)}')
print(f'The condition was met for a win: {blackjack_hand5(17, 21)}')


# print(x)

def blackjack_hand6(player_hand, dealer_hand):
    '''Return whether the condition is met
    that the player hand is greater than the dealer hand
    and the player hand is less than or equal to 21.'''
    # Returning a value directly is more streamlined
    # than first storing the value in an intermediate variable like x.
    return (player_hand > dealer_hand) and (player_hand <= 21)
