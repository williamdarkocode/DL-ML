import argparse

argument_pass = argparse.ArgumentParser()

argument_pass.add_argument("-n", "--name", required=True, help="name of the user is required!") 
# -n is the shorthand for --name where either may be used in the cmd line
# help string would give additional info in ther terminal when executed with the --help flag

arguments = vars(argument_pass.parse_args())
# vars function turns the parsed cmd line args to python dictionary where the key to access the value is the name of the argument,
# thus in this case is 'name'

print(arguments)

# -a boolean args option
# -b string args option
# -c integer args option


# display a message using the arguments passed via cmd line input
print("Hello {}, welcome to your virtual world, where all things are possible.".format(arguments["name"]))
# args['key'] gives you the value associated with the given key in the dictionary
# new dir