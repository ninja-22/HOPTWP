even_list = filter(lambda x: x % 2 == 0, [1, 2, 3, 4])          # filters out elements of list that return true for particular condition. First argument is function/lambda, second argument is the list or iterable
print(list(even_list))