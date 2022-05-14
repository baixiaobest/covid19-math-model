import numpy as np
import src.COVIDDynamics_Nigeria as cd
from scipy.integrate import odeint
import matplotlib.pyplot as plt

if __name__ == '__main__':
    covid_dynamics = cd.COVIDDynamics_Nigeria(
        tau=0.0002,
        beta=0.0805,
        delta=1.6728e-5,
        gamma=2.0138e-4,
        eta=0.4478,
        theta=0.0101,
        mu=0.0106,
        nu=3.2084e-4,
        sigma=0.0668,
        lambdaa=0.02537,
        r1=5.7341e-5,
        r2=1.6728e-5)

    S = 0.5
    E = 0.01
    Q = 0
    Ia = 0
    Is = 0
    R = 0

    x0 = [S, E, Q, Ia, Is, R]

    t = np.array(range(0, 120))
    x = odeint(covid_dynamics.dxdt, x0, t)

    titles = ['Susceptible individuals',
              'Exposed individuals',
              'Qurantined individuals',
              'Asymptomatic infected individuals',
              'Symptomatic infected individuals',
              'Recovered individuals']

    for i in range(6):
        plt.figure()
        plt.plot(t, x[:, i])
        plt.gca().set_title(titles[i])
    plt.show()