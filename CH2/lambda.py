#!/usr/local/bin/python

l1 = [1, 2, 3, 4]
sq_lambda = list(map(lambda x: x ** 2, l1))         # lambda function passed into map and the second argument is the list (l1)

print(sq_lambda)