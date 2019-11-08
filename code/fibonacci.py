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
    if n <= 1:
        return n
    else:
        return fibonacci_number_for_index(n - 1) + fibonacci_number_for_index(n - 2)
    
    //Adding this thing
    //commit commit
