import matplotlib.pyplot as plt


def f(x) :

    return [i*2 for i in x]



X = [1, 2, 3, 4, 5]
y = f(X)

print(f(X))


plt.plot(X,y)
plt.show()