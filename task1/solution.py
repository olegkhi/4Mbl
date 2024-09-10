import numpy as np


def find_answer(alpha, n, f, f_derivative):
    EPS = 1e-4
    # Количество узловых точек m = |{1, ..., n - 1}|
    m = n - 1
    x = np.linspace(0, 1, n + 1)[1:-1]
    # Для первой итерации алгоритма Ньютона заполняем вектор u нулями
    u = np.zeros(m, dtype=float)

    A = create_A(m)
    H = np.empty(m, dtype=float)
    H_derivative = np.zeros((m, m), dtype=float)

    while True:
        calculate_H(H, f, x, u, alpha)
        calculate_H_derivative(H_derivative, f_derivative, u)
        y = np.linalg.solve(A + H_derivative, -(A @ u + H))
        if np.linalg.norm(y, ord=np.inf) < EPS:
            break
        u += y

    return np.pad(u, pad_width=(1, 1), mode='constant', constant_values=0)


def create_A(m):
    A = np.zeros((m, m), dtype=float)
    np.fill_diagonal(A, 2)
    np.fill_diagonal(A[:, 1:], -1)
    np.fill_diagonal(A[1:, :], -1)
    return A


def calculate_H(H, f, x, u, alpha):
    h = 1 / (len(H) + 1)
    for i in range(len(H)):
        H[i] = (h ** 2) * f(x[i], u[i], alpha)


def calculate_H_derivative(H_derivative, f_derivative, u):
    h = 1 / (len(H_derivative) + 1)
    new_diagonal = [
        h ** 2 * f_derivative(u[i])
        for i in range(len(H_derivative))
    ]
    np.fill_diagonal(H_derivative, new_diagonal)
