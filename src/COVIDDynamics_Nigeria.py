import numpy as np

class COVIDDynamics_Nigeria:
    def __init__(self, tau, beta, delta, gamma, eta, theta, mu, nu, sigma, lambdaa, r1, r2):
        self.tau = tau
        self.beta = beta
        self.delta = delta
        self.gamma = gamma
        self.eta = eta
        self.theta = theta
        self.mu = mu
        self.nu = nu
        self.sigma = sigma
        self.lambdaa = lambdaa
        self.r1 = r1
        self.r2 = r2

    def dxdt(self, x, args):
        x_dot = np.zeros(6)
        S, E, Q, Ia, Is, R = x
        x_dot[0] = self.lambdaa - (self.tau + self.mu)*S - self.beta*S*E
        x_dot[1] = self.beta*S*E - (self.gamma + self.mu + self.eta + self.sigma)*E
        x_dot[2] = self.tau*S + self.gamma*E - (self.mu + self.nu + self.theta)*Q
        x_dot[3] = self.sigma*E + self.theta*Q - (self.mu + self.r1)*Ia
        x_dot[4] = self.eta*E + self.nu*Q - (self.delta + self.mu + self.r2)*Is
        x_dot[5] = self.r1*Ia + self.r2*Is - self.mu*R

        return x_dot