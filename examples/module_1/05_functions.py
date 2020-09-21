# Function definition.
# Format: def <function_name>(parameters)


def my_function(parameter, number=None):
    print("Running function with: " + parameter)
    print("Number " + str(number))
    return 10, 25


# Re-use the logic defined on my_function
my_function("Test1")


# Re-use the logic defined on my_function
my_function("Test2", 20)


# Re-use the logic defined on my_function
my_function("Test3")

