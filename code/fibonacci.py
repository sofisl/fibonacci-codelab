def fibonacci_series(n):
    series = []
    for i in range(0, n + 1):
        if i == 0:
            series.append(0)  # F0 = 0
        elif i == 1:
            series.append(1)  # F1 = 1
        else:
            series.append(series[i - 1] + series[i - 2])
    return series

def fibonacci_number_for_index(n):
    fn_2 = 0
    fn_1 = 1
    number = 0
    for i in range(0, n + 1):
        if i <= 1:
            number = i
        else:
            number = fn_1 + fn_2
            fn_2 = fn_1
            fn_1 = number
    return number