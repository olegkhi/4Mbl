import os
import numpy as np
import pandas as pd
from solution import find_answer
from plotting import plot_with_fixed_and_varying


def f(x, u, alpha):
    return np.exp(u) - alpha * np.sin(x ** 2)


def f_derivative(u):
    return np.exp(u)


def main():
    possible_alphas = [0.1, 1, 2, 5, 10]
    possible_ns = [10, 20, 1000]

    results = []
    for alpha in possible_alphas:
        for n in possible_ns:
            x = np.linspace(0, 1, n + 1)
            u = find_answer(alpha, n, f, f_derivative)
            results.append(pd.DataFrame({'alpha': alpha,
                                         'n': n,
                                         'x': x,
                                         'u': u,
                                         }))
    data = pd.concat(results, ignore_index=True)
    # print(data.head())

    # Изменение текущей рабочей директории, чтобы графики лежали в этой же папке
    os.chdir(os.path.dirname(__file__))

    # Строим графики при фиксированной альфе, варьируя n, и наоборот
    for n in [10, 1000]:
        plot_with_fixed_and_varying(
            data,
            fixed_param='n',
            fixed_value=n,
            varying_param='alpha',
            varying_values=possible_alphas
        )
    for alpha in [0.1, 1, 10]:
        plot_with_fixed_and_varying(
            data,
            fixed_param='alpha',
            fixed_value=alpha,
            varying_param='n',
            varying_values=possible_ns
        )


if __name__ == '__main__':
    main()
