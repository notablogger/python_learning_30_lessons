
def print_dictionary(dictionary):
    for key in dictionary:
        print(f"{key}->{dictionary[key]}\n")


programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.",
                          "Function": "A piece of code that you can easily call over and over again."
                          }
print(programming_dictionary)
print_dictionary(programming_dictionary)

programming_dictionary["bug"]= "god help me"
print_dictionary(programming_dictionary)
programming_dictionary={}
print_dictionary(programming_dictionary)
