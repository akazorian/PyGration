from Integral import Integral
from Simpson import *
from math import *
from os import *
import subprocess as sp


def setup_integral(user_input):
    index, bounds = 0, []
    if len(user_input) > 8 or len(user_input) < 8:
        print(
            "Please use syntax of the form 'integrate f from a to b with n subintervals'.")
        return
    while index < len(user_input):
        if index == 0:
            f = user_input[index]
        elif index == 1 and not (user_input[index] == "from"):
            return
        elif (index == 2 or index == 4):
            bounds.append(user_input[index])
        elif index == 3 and not (user_input[index] == "to"):
            return
        elif index == 5 and not(user_input[index] == "with"):
            return
        elif index == 6:
            n = eval(user_input[index])
        elif index == 7 and not(user_input[index] == "subintervals"):
            return
        index += 1
    integral = Integral(lambda x: eval(f), eval(bounds[0]), eval(bounds[1]))
    Simpson = Simpson_Rule(integral, n)
    return Simpson.Simpson_approx()


def Main():
    while True:
        try:
            new_line, index = input(">>> ").split(), 0
            word = new_line[0]
            if word in global_func and word != "integrate":
                global_func[word]()
            elif word == "integrate":
                print(setup_integral(new_line[1:]))
            else:
                raise SyntaxError(
                    "{} is not defined. Please use syntax of the form 'integrate f from a to b with n subintervals'.".format(word))
        except (ZeroDivisionError, SyntaxError, AssertionError) as err:
            print("Error:", err)
        except KeyboardInterrupt:
            print()
            print("KeyboardInterrupt")
        except EOFError:
            print()
            return

global_func = {
    "integrate": setup_integral,
    "exit": sp.sys.exit,
    "clear": lambda: sp.call('clear', shell=True),
    "help": lambda: print("To integrate a function f using Simpson's approximation rule, use the following syntax: integrate f from a to b with n subintervals."),
}

if __name__ == '__main__':
    Main()
