import math
import matplotlib.pyplot as plt


def main():
    x_kutt, y_kutt, kutt = runge_kutt(0.1)
    print("Runge–Kutt")
    for item in kutt:
        print (item)
    x_adam, y_adam, adam = adams(0.1)
    print("\nAdams–Bashforth")
    for item in adam:
        print (item)
    
    print("\n BOTH METHODS RESULTS:")
    for i in range(len(kutt)):
        print("%.2f" % kutt[i][0], kutt[i][1], adam[i][1])
        
    err_kutt, x_k = error(kutt)
    err_adams, x_a = error(adam)
    print("\n Errors\n ")
    for i in range(len(err_kutt)):
      print(err_kutt[i], err_adams[i])
    y_exact = []
    for i in range(len(x_kutt)):
      y_exact.append(y_(x_kutt[i]))
    print("\n Exact Function\n")
    for i in range(len(y_exact)):
      print("%.2f" % x_kutt[i], y_exact[i])

    plot_three_functions(x_kutt, y_kutt, x_adam, y_adam, x_kutt, y_exact, "Function")
    plot_two_functions(x_k, err_kutt, x_a, err_adams, "Errors")
    
def f(x, y):
    return (1 - x ** 2) * y + math.cos(x) - (1 - x ** 2) * math.sin(x)

def runge_kutt(h):
    x = [float(i) * h for i in range(35)]
    y = [0]
    for x_i in x:
        k1 = h * f(x_i, y[-1])
        k2 = h * f(x_i + h / 2, y[-1] + k1 / 2)
        k3 = h * f(x_i + h / 2, y[-1] + k2 / 2)
        k4 = h * f(x_i + h, y[-1] + k3)
        y.append(y[-1] + (k1 + 2 * k2 + 2 * k3 + k4) / 6)

    return x, y[:-1], list(zip(x, y))

def adams(h):
    runge_kutt_ = runge_kutt(h)[2][:4]
    x = [float(i)*h for i in range(35)]
    y = [i[1] for i in runge_kutt_]
    for i in range(3, len(x)):
        y.append(y[i] + (55 * f(x[i], y[i]) -
                         59 * f(x[i - 1], y[i - 1]) +
                         37 * f(x[i - 2], y[i - 2]) -
                         9 * f(x[i - 3], y[i - 3])) * h / 24)
    return x, y[:-1], list(zip(x, y))

def error(ar):
    err = []
    x_ar = []
    for i in range(len(ar)):
        x = ar[i][0]
        e_i = abs(ar[i][1] - y_(x))
        err.append(e_i)
        x_ar.append(x)
    return err, x_ar

def y_(x):
    return math.sin(x)


def plot_two_functions(x1, y1, x2, y2, title):
    plt.plot(x1, y1, label = "Runge-Kutt")
    plt.plot(x2, y2, label = "Adams-Bashforth")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(f'{title}')
    plt.legend()
    plt.show()

def plot_three_functions(x1,y1,x2,y2,x3,y3,title):
    plt.plot(x1,y1,label = "Runge - Kutt")
    plt.plot(x2,y2,label = "Adams–Bashforth")
    plt.plot(x3,y3, label = "Original")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(f'{title}')
    plt.legend()
    plt.show()

if __name__ == '__main__':
    main()
