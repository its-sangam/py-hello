# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# print_hi('hello')
a_var = 5
b_var = 7


def outer_foo():
    global a_var
    a_var = 3
    b_var = 9

    def inner_foo():
        global a_var
        a_var = 4
        b_var = 8
        print('a_var inside inner_foo :', a_var)
        print('b_var inside inner_foo :', b_var)

    inner_foo()
    print('a_var inside outer_foo :', a_var)
    print('b_var inside outer_foo :', b_var)


outer_foo()
print('a_var outside all functions :', a_var)
print('b_var outside all functions :', b_var)
