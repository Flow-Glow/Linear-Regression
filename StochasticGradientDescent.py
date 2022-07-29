import numpy as np
import matplotlib.pyplot as plt


data = np.array([[1, 2], [2, 5], [3, 7]])


eta = 0.1
epoch = 10000

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

def compute_grad_with_respect_to_M(m, b,x,y):
    return (m*x+b-y)*x

def compute_grad_with_respect_to_B(m, b,x,y):
    return (m*x+b-y)

def main(eta,data):
    m = np.random.randint(0, 10)
    b = np.random.randint(0, 10)
    print(m, b)
    print("_" * 10)
    for i in range(epoch):
        for point in data:
            x = point[0]
            y = point[1]
            y_hat = (m * x + b)
            e = 1/2 * (y_hat - y) ** 2
            m = m - (eta*compute_grad_with_respect_to_M(m,b,x,y))
            b = b - (eta*compute_grad_with_respect_to_B(m,b,x,y))
            print(m, b)
            print(e)
            print("_" * 10)
            ax.scatter(m, b, e, c='black', marker='o', s=15)
            ax.set_xlabel('m')
            ax.set_ylabel('b')
            ax.set_zlabel('E')




main(eta,data)
plt.show()
