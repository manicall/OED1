from data import *

_a = a0(LnX, LnY)
a = np.exp(_a)
b = a1(LnX, LnY)

def f(x):
    return a * x ** b
fx = f(x[1:])

print(f"M = {M(y[1:], fx)}")
print(f"D = {D(y[1:], fx)}")
print(f"R = {R(y[1:], fx)}")

print(f'y = {round(b, 4)}^(x)*{round(a,4)}', f"R = {round(R(y[1:], fx), 5)}")

fig.canvas.set_window_title('Степенная аппроксимация')
ax.plot(x[1:], y[1:])
ax.plot(x[1:], fx)

plt.xlabel("X")
plt.ylabel("Y")

ax.text(140, 0.6, f'y = {round(b, 4)}^(x)*{round(a,4)}', rotation = -5, fontsize=9)
ax.text(140, 0.5, f"R = {round(R(y[1:], fx), 5)}", rotation = -5, fontsize=9)


plt.show()
