# imports
import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import make_regression


def euclidean_distance_calc(y, data_y):
    """Calculate the euclidean distance between two points"""
    euclidean_l = []

    for i in range(len(data_y)):
        e = (y[i] - data_y[i]) ** 2
        euclidean_l.append(e)
    score = np.sum(np.array(euclidean_l))
    return np.sqrt(score)


def ploting(x, y, data_y, data_x, Loss):
    """This Function plots all the points"""
    plt.plot(x, y, color="r", label=f"Score is {Loss}")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.scatter(data_x, data_y, color="b", label="Data")
    plt.legend(loc='upper left')
    plt.axis("equal")
    plt.grid()


def main(grid_search):
    #Generate data
    x, y = make_regression(n_samples=100, n_features=1, noise=10,random_state=1000)
    y = y*.1

    if grid_search:
        """
        Grid search method:
        
        
        """
        result = []
        best_loss = []
        m_array = np.arange(5, 15, .01)
        b_array = np.arange(-4, 4, .1)
        for m in m_array:
            for b in b_array:
                line_y = (m * x) + b
                Loss = euclidean_distance_calc(line_y, y)
                d = {"Slope": f"{m:.2f}", "Y-Intercept": f"{b:.2f}", "Y": line_y, "X": x, "Loss": f"{Loss:.3f}", }
                result.append(d)
        for i in result:
            best_loss.append(i["Loss"])

        best_loss = np.array(best_loss)
        index = np.argmin(best_loss)
        bestLine = result[index]

        print(type(result[index]))
        with open("Data.txt", "w") as f:
            f.write(str(result[index]))
        ploting(bestLine["X"], bestLine["Y"], y, x, bestLine["Loss"])
    else:
        """
        Least squares method
        """
        ones = np.ones([len(x), 1])
        x = x.reshape(len(x), 1)
        X = np.concatenate((x, ones), axis=1)
        z = np.matmul(np.matmul(np.linalg.inv((np.matmul(X.T, X))), X.T), y)
        line_y = (z[0] * x) + z[1]
        d = {"Slope": f"{z[0]:.2f}", "Y-Intercept": f"{z[1]:.2f}", "Y": line_y, "X": x, "Loss": f"{euclidean_distance_calc(line_y, y):.3f}", }
        with open("Data.txt", "w") as f:
            f.write(str(d))
        ploting(d["X"], d["Y"], y, x, d["Loss"])

if __name__ == "__main__":
    main(grid_search = True)
    plt.show()