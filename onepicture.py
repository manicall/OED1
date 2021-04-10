from data import *

a = a0(x, y)
b = a1(x, y)

print(a, b)

f = lambda x: a+b*x
fx = f(x)

h = np.sum([(y[i] + fx[i]) / 2 for i in range(len(y))]) / len(y)
print(h)
v = 1 - SumSquare(y - fx) / SumSquare([y[i] - h for i in range(len(y))])

print(SquareSum(y - fx) / SquareSum([y[i] - h for i in range(len(y))]))
print(f"D = {D(y, fx)}")
print(f"R = {R(y, fx)}")

size = 3

fig.canvas.set_window_title('Линейная аппроксимация')
ax.plot(x, y, color='black')
ax.scatter(x, fx, s = size)

plt.xlabel("X")
plt.ylabel("Y")

ax.text(75, 0.7, f'y = {round(b, 4)}x+{round(a,4)}', rotation = -23, fontsize = 9)
ax.text(75, 0.7, f"R = {round(R(y, fx), 5)}", rotation = -23, fontsize = 9)



_a = a0(LnX, LnY)
a = np.exp(_a)
b = a1(LnX, LnY)

def f(x):
    return a * x ** b
fx = f(x[1:])

print(f"M = {M(y[1:], fx)}")
print(f"D = {D(y[1:], fx)}")
print(f"R = {R(y[1:], fx)}")

ax.scatter(x[1:], fx, s = size)

plt.xlabel("X")
plt.ylabel("Y")

ax.text(140, 0.6, f'y = {round(a,4)}*{round(b, 4)}^x', rotation = -5, fontsize=9)
ax.text(140, 0.5, f"R = {round(R(y[1:], fx), 5)}", rotation = -5, fontsize=9)

_a = a0(x[1:], LnY)
a = np.exp(_a)
b = a1(x[1:], LnY)

f = lambda x: a * np.exp(b*x)
fx = f(x[1:])

print(f"M = {M(y[1:], fx)}")
print(f"D = {D(y[1:], fx)}")
print(f"R = {R(y[1:], fx)}")
print(f"{round(a, 4)}*exp^({round(b, 4)}*x")

fig.canvas.set_window_title('Экспоненциальная аппроксимация')
ax.scatter(x[1:], fx, s = size)

plt.xlabel("X")
plt.ylabel("Y")

ax.text(40, 0.7, f'y = {round(a, 4)}*exp^({round(b, 4)}*x)', rotation=-24, fontsize=9)
ax.text(40, 0.8, f"R = {round(R(y[1:], fx), 5)}", rotation=-24, fontsize=9)

plt.show()