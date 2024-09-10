import matplotlib.pyplot as plt
import seaborn as sns


def plot_graph(data, filter_condition, hue, title, xlabel, filename):
    plt.figure(figsize=(8, 6))
    sns.lineplot(
        x='x', y='u', data=data[filter_condition],
        hue=hue, palette='deep'
    )
    sns.despine()
    plt.xlim(0, 1)
    plt.grid(True)

    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel("")

    plt.savefig(f'{filename}')
    plt.close()


def plot_with_fixed_and_varying(data, fixed_param, fixed_value, varying_param, varying_values):
    """
    Строит график u(x) с одним фиксированным параметром и одним варьируемым.

    Параметры:
    data (pandas.DataFrame): Данные для построения графика.
    fixed_param (str): Название столбца с фиксированным параметром.
    fixed_value: Значение фиксированного параметра.
    varying_param (str): Название столбца с варьируемым параметром.
    varying_values (list): Список значений варьируемого параметра.
    """
    # Создание условия фильтрации
    filter_condition = (data[fixed_param] == fixed_value) & (
        data[varying_param].isin(varying_values))

    # Определение параметра hue
    hue = varying_param

    # Форматирование строк для заголовка и метки оси X
    varying_values_str = ', '.join(map(str, varying_values))
    title = f'График u(x) при {varying_param} = {varying_values_str}'
    xlabel = f'{fixed_param} = {fixed_value}'

    # Формирование имени файла
    varying_values_str_short = ','.join(map(str, varying_values))
    filename = f'{fixed_param}({fixed_value})_{varying_param}({
        varying_values_str_short}).png'

    plot_graph(data, filter_condition, hue, title, xlabel, filename)
