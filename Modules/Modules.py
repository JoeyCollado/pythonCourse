# module = a file containing python code. may contain functions, classes, etc.
#          used with modular programming, which is to separate program into parts
# help("modules") #shows all built in different modules that we can use
# alternative is = you can go to python module index website

import Messages as msg # import the other module to inherit all its function(python code)
                       # as gives a new nickname to the module file for better practice

msg.hello()
msg.bye()