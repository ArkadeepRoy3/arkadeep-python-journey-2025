try:
    print(m)
    5/0
except NameError:
    print("m is not defined")
except ZeroDivisionError:
    print("You can't divide by zero")
except:
    print("Something else went wrong")
else:
    print("Nothing went wrong")
finally:
    print("The 'try except' is finished")