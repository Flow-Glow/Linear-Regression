import numpy as np
import matplotlib.pyplot as plt


m_array = np.linspace(-10, 15, 100)
b_array = np.linspace(-10, 15, 100)
data = np.array([[1, 2], [2, 5], [3, 7]])
m = -5
b = -5
eta = 0.01

def compute_grad_with_respect_to(m, b, respect=True):
    if respect:
        return (6 * b) + (14 * m) - 33
    else:
        return (6 * m) + (3 * b) - 14

fig2,ax2=plt.subplots(1,1)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')



m_s, b_s = np.meshgrid(m_array, b_array)
e = (m_s + b_s - 2) ** 2 + ((2 * m_s) + b_s - 5) ** 2 + ((3 * m_s) - 7) ** 2
cp = ax2.contourf(m_s, b_s, e)
# print(m,b,e)
fig2.colorbar(cp) # Add a colorbar to a plot
ax2.set_title('Filled Contours Plot')
ax2.set_xlabel('m (cm)')
ax2.set_ylabel('b (cm)')
ax.plot_surface(m_s, b_s, e, rstride=1, cstride=1, edgecolor='none',alpha=.7)

for i in range(500):
    respect_to_b = compute_grad_with_respect_to(m, b, respect=False)
    respect_to_m = compute_grad_with_respect_to(m, b)

    m = m - (eta * respect_to_m)
    b = b - (eta * respect_to_b)
    
    e = (m + b - 2) ** 2 + ((2 * m) + b - 5) ** 2 + ((3 * m) - 7) ** 2


    print(e,m, b, f"{i} point")
    ax.scatter(m, b, e, c='black', marker='o', s=15)
    ax.set_xlabel('m')
    ax.set_ylabel('b')
    ax.set_zlabel('E')
print(f"Error: {e}\nM:{m}\nB:{b}")




plt.grid()
plt.show()
plt.xlim([0,10])
plt.axis("equal")
