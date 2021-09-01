def lambdaFunction(x):
    return (lambda y: x * y)

secondLambda = lambdaFunction(1000)
print(secondLambda(1000))
