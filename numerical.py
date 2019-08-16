from numpy import loadtxt
# from pylab import figure, plot, xlabel, grid, hold, legend, title, savefig, show
# from matplotlib.font_manager import FontProperties
from scipy.integrate import odeint


def vectorfield(w, t, p):
    u, v, x, y = w
    a, b = p

    f = [u,
         - a * u - b * y,
         v,
         - a * v + b * x]
    return f

x = 0.5
u = 0.0
y = 0.5
v = 0.0
w0 = [x, u, y, v]

abserr = 1.0e-8
relerr = 1.0e-6
stoptime = 10.0
numpoints = 250

t = [stoptime * float(i) / (numpoints - 1) for i in range(numpoints)]

a = -1000
b = -10
p = [a, b]

# Call the ODE solver.
wsol = odeint(vectorfield, w0, t, args=(p,),
              atol=abserr, rtol=relerr)

with open('two_springs.dat', 'w') as f:
    for t1, w1 in zip(t, wsol):
        print >> f, t1, w1[0], w1[1], w1[2], w1[3]

t, x, u, y, v = loadtxt('two_springs.dat', unpack=True)
print x[-1]
print y[-1]

# figure(1, figsize=(6, 4.5))

# xlabel('t')
# grid(True)
# hold(True)
# lw = 1

# plot(t, x, 'b', linewidth=lw)
# plot(t, y, 'g', linewidth=lw)

# legend((r'$x_1$', r'$x_2$'), prop=FontProperties(size=16))
# # title('Mass Displacements for the\nCoupled Spring-Mass System')
# show(figure)
