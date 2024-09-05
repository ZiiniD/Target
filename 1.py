x = int(input("num: "))


def fibonacci(x):
    fibonacci_list = [0, 1]
    while len(fibonacci_list) < x:
        proximo_numero = fibonacci_list[-1] + fibonacci_list[-2]
        fibonacci_list.append(proximo_numero)
        if proximo_numero < x:
            continue
        elif proximo_numero == x:
            return "O numero existe na sequencia de fibonacci."
        else:
            return f"O numero nao existe na sequencia de fibonacci: {fibonacci_list}"

    return fibonacci_list


print(fibonacci(x))
