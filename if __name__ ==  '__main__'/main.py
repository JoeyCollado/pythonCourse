# python interpreter sets "special variables" one of which is __name__
# python will assign the __name__ variable a value of '__main__' if it's
# the initial module being run

#why?
# 1. module can be run as a standalone program
# 2. module can be imported and used by other modules


def main():
    print("Hello")


if __name__ == '__main__': 
    main()                  #calling the method directly in this module
        