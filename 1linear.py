from data import *

a = a0(x, y)
b = a1(x, y)

f = lambda x: a+b*x
fx = f(x)

print(f"M = {M(y, fx)}")
print(f"D = {D(y, fx)}")
print(f"R = {R(y, fx)}")
print(f'y = {round(b, 4)}x+{round(a,4)}')


fig.canvas.set_window_title('Линейная аппроксимация')
ax.plot(x, y)
ax.plot(x, fx)

plt.xlabel("X")
plt.ylabel("Y")

ax.text(75, 0.7, f'y = {round(b, 4)}x+{round(a,4)}', rotation = -23, fontsize = 9)
ax.text(75, 0.7, f"R = {round(R(y, fx), 5)}", rotation = -23, fontsize = 9)

plt.show()
