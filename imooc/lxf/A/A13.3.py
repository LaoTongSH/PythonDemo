def Y(X):
    return X,X*X
L = [Y(X) for X in range(1,11)]
print(L)
print("****************************************")
L1 = [Y(X) for X in range(1,11) if X%2 == 0 ]
print(L1)

