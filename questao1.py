import cmath

def f(x):
    return x**3 - 0.5 * x**2 + 4 * x - 2

def metodo_muller(f, x0, x1, x2, tol=1e-8, max_iter=100):
    # Cabeçalho para o acompanhamento das iterações
    print("\n" + "="*65)
    print("                ACOMPANHAMENTO DAS ITERAÇÕES")
    print("="*65)
    print(f"{'Iteração':<10} | {'x_k':<25} | {'f(x_k)':<25}")
    print("-" * 65)

    for i in range(max_iter):
        f0, f1, f2 = f(x0), f(x1), f(x2)

        h1 = x1 - x0
        h2 = x2 - x1
        
        if h1 == 0 or h2 == 0 or (h2 + h1) == 0:
            print(f"Divisão por zero encontrada na iteração {i+1}. O método falhou.")
            return None
            
        d1 = (f1 - f0) / h1
        d2 = (f2 - f1) / h2

        a = (d2 - d1) / (h2 + h1)
        b = a * h2 + d2
        c = f2

        raiz_discriminante = cmath.sqrt(b**2 - 4 * a * c)

        denominador1 = b + raiz_discriminante
        denominador2 = b - raiz_discriminante

        if abs(denominador1) > abs(denominador2):
            denominador = denominador1
        else:
            denominador = denominador2

        if abs(denominador) == 0:
            return None

        dx = -2 * c / denominador
        x3 = x2 + dx

        # ✅ Mostra o progresso a cada iteração
        print(f"{i+1:<10} | {x3.real:<25.10f} | {f(x3.real):<25.10f}")

        if abs(dx) < tol:
            print("-" * 65) # Fecha a tabela de acompanhamento
            return x3

        x0, x1, x2 = x1, x2, x3

    print("-" * 65)
    return None


if __name__ == "__main__":
    # ✅ Novos valores mais distantes da raiz
    x0 = -1.0
    x1 = 1.0
    x2 = 2.0

    raiz = metodo_muller(f, x0, x1, x2)

    print("\n" + "="*40)
    print("      RESULTADO FINAL DO MÉTODO")
    print("="*40)

    if raiz is not None:
        raiz_real = raiz.real
        valor_f = f(raiz_real)
        
        print(f"✅ Convergência alcançada com sucesso!")
        print(f"   - Raiz Positiva Encontrada (x): {raiz_real:.8f}")
        print(f"   - Valor de f(x) na raiz:        {valor_f:.12f}")
        
    else:
        print("❌ O método não convergiu com os parâmetros fornecidos.")
    
    print("="*40)
    
    
