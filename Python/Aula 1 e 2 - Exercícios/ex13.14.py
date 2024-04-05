def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)

print("Fatorial: " + str (fatorial(int(input("Insira um número: ")))))