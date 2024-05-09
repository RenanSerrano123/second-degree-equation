import math
def calcular_delta(a, b, c):
    return b**2 - 4*a*c
def resolver_equacao_segundo_grau(a, b, c):
    delta = calcular_delta(a, b, c)
    if delta < 0:
        print(f"Sem solucao real!\nDelta = {delta:.2f}")
    elif delta == 0:
        x = -b / (2*a)
        if x == 0:
            x=-x
        else:
            x=x
        print(f"x = {x:.2f}")
    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        if x1>x2:
            aux=x1
            x1=x2
            x2=aux
        else:
            x1=x1
            x2=x2
        print(f"x1 = {x1:.2f}\nx2 = {x2:.2f}")
def main():
    a = float(input())
    b = float(input())
    c = float(input())
    resolver_equacao_segundo_grau(a, b, c)
main()