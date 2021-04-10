from data import *

_a = a0(x[1:], LnY)
a = np.exp(_a)
b = a1(x[1:], LnY)

f = lambda x: a * np.exp(b*x)
fx = f(x[1:])

print(f"M = {M(y[1:], fx)}")
print(f"D = {D(y[1:], fx)}")
print(f"R = {R(y[1:], fx)}")

print(f'y = {round(a, 4)}*exp^({round(b, 4)}*x)', f"R = {round(R(y[1:], fx), 5)}")

fig.canvas.set_window_title('Экспоненциальная аппроксимация')
ax.plot(x[1:], y[1:])
ax.plot(x[1:], fx)

plt.xlabel("X")
plt.ylabel("Y")

ax.text(40, 0.7, f'y = {round(a, 4)}*exp^({round(b, 4)}*x)', rotation=-24, fontsize=9)
ax.text(40, 0.8, f"R = {round(R(y[1:], fx), 5)}", rotation=-24, fontsize=9)

plt.show()
