def main():
    try:
        concat_string = 'John' + ' ' + 'Doe'
        print(concat_string)
        # add_num = 4+'hi'
        # divide_num = 5/0
        # print(divide_num)
    # except ValueError as e:
    #     print(f"Something went wrong: {e}")
    # except TypeError as te:
    #     print(f"Type error: {te}")
    # except ZeroDivisionError as ze:
    #     print(f"Division error: {ze}")
    except Exception as e:
        print(f"Something went wrong: {e}")
main()