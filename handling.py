try:
    print("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    # i = 0/0
    f = open("abc.txt")
    # zerodivision = 0/0

except FileNotFoundError as e:
    print(e.filename, "is not present")
    print(dir(e))
    
# except (ZeroDivisionError, FileNotFoundError):                                        # except Exception as e:
#     print("You have divided by zero")
#     # print("ZeroDivisionError")
# except RuntimeError:
#     print("This is a Run Time Error")
# except FileNotFoundError:
#     print("File is not found")
# We added Git here just for fun
