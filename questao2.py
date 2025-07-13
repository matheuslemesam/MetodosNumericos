import copy
import os
import time

def limpar_tela():
    """
    Limpa a tela do terminal, compatível com Windows, macOS e Linux.
    """
    os.system('cls' if os.name == 'nt' else 'clear')

def imprimir_matriz_aumentada(A, B, titulo):
    """
    Função auxiliar para imprimir a matriz aumentada [A|B] de forma formatada.
    """
    print(f"\n--- {titulo} ---")
    n = len(B)
    for i in range(n):
        linha_A = " ".join([f"{val:8.2f}" for val in A[i]])
        print(f"  [ {linha_A} | {B[i]:8.2f} ]")
    print("-" * (n * 9 + 15))

def eliminacao_gauss_puro_python(A, B):
    """
    Resolve um sistema linear Ax = B usando a Eliminação de Gauss,
    mostrando as etapas do processo.
    """
    n = len(B)
    A = copy.deepcopy(A)
    B = copy.deepcopy(B)

    print("="*60)
    print("      INÍCIO DA EXECUÇÃO: MÉTODO DE ELIMINAÇÃO DE GAUSS")
    print("="*60)

    imprimir_matriz_aumentada(A, B, "Matriz Aumentada Inicial [A|B]")

    # Etapa 1: Eliminação progressiva com pivoteamento parcial
    for k in range(n - 1):
        p_idx = max(range(k, n), key=lambda i: abs(A[i][k]))
        if p_idx != k:
            A[k], A[p_idx] = A[p_idx], A[k]
            B[k], B[p_idx] = B[p_idx], B[k]

        if A[k][k] == 0:
            print("Erro: Matriz singular detectada.")
            return None

        for i in range(k + 1, n):
            if A[i][k] != 0:
                fator = A[i][k] / A[k][k]
                for j in range(k, n):
                    A[i][j] -= fator * A[k][j]
                B[i] -= fator * B[k]
        
        imprimir_matriz_aumentada(A, B, f"Após etapa de eliminação da coluna k={k}")

    imprimir_matriz_aumentada(A, B, "Forma Triangular Superior Final")
    print("\nFase de eliminação concluída. Iniciando substituição regressiva...")

    # Etapa 2: Substituição regressiva
    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        soma = sum(A[i][j] * x[j] for j in range(i + 1, n))
        x[i] = (B[i] - soma) / A[i][i]
    
    print("="*60)
    return x

def montar_sistema_circuito():
    """
    Retorna a matriz A e o vetor B correspondentes ao circuito da Figura 1.
    """
    A = [
        [ 7.0, -1.0,  0.0, -4.0],
        [-1.0, 11.0, -10.0,  0.0],
        [ 0.0, -5.0,  7.0, -2.0],
        [-5.0,  0.0, -5.0, 11.0]
    ]
    B = [400.0, 0.0, 0.0, 0.0]
    return A, B


if __name__ == "__main__":
    # --- TELA 1: Explicação Inicial (TEXTO COMPLETO RESTAURADO) ---
    limpar_tela()
    print("="*70)
    print("      Análise de Circuito Elétrico com Métodos Numéricos")
    print("="*70)
    print("\nEste script resolve a Questão 2 da lista de exercícios, que consiste\n"
          "em encontrar as correntes em um circuito de resistores.")
    
    print("\nCOMO FUNCIONA:")
    print("1. MODELAGEM FÍSICA: O circuito é transformado em um sistema de equações\n"
          "   lineares através da Análise Nodal, que aplica a Lei de Kirchhoff\n"
          "   das Correntes em cada nó do circuito para determinar as tensões (V).")
          
    print("\n2. SOLUÇÃO NUMÉRICA: Para resolver o sistema de equações (Ax = B), este\n"
          "   programa implementa o método de Eliminação de Gauss com Pivoteamento\n"
          "   Parcial. Este método resolve o sistema de forma sistemática e robusta,\n"
          "   evitando erros numéricos.")

    print("\n3. IMPLEMENTAÇÃO: O código foi escrito em Python puro, sem bibliotecas\n"
          "   externas como NumPy, para garantir que funcione em qualquer computador\n"
          "   com uma instalação padrão do Python.")
    
    print("\n" + "="*70)
    input("Pressione a tecla ENTER para executar o método e ver as iterações...")
    
    # --- TELA 2: EXECUÇÃO DO MÉTODO COM AS ITERAÇÕES ---
    limpar_tela()
    A, B = montar_sistema_circuito()
    tensoes = eliminacao_gauss_puro_python(A, B)
    
    if tensoes is not None:
        input("\nPressione Enter para ver o resumo final dos resultados...")
    
    # --- TELA 3: RESULTADOS FINAIS ---
    limpar_tela()
    
    print("\n" + "="*50)
    print("      RESULTADO FINAL DA ANÁLISE DE CIRCUITO")
    print("="*50)

    if tensoes is not None:
        V2, V3, V4, V5 = tensoes
        
        print("✅ Sistema resolvido com sucesso!")
        print("\n--- Tensões nos Nós ---")
        for i, Vi in enumerate(tensoes):
            print(f"   - V{i+2} = {Vi:.4f} V")

        print("\n--- Correntes nos Resistores ---")
        V1, V6 = 200.0, 0.0
        correntes = {
            "R=10Ω (2→1)": (V2 - V1) / 10, "R=20Ω (2→3)": (V2 - V3) / 20,
            "R=2Ω  (3→4)": (V3 - V4) / 2,  "R=5Ω  (2→5)": (V2 - V5) / 5,
            "R=5Ω  (4→5)": (V4 - V5) / 5,  "R=25Ω (5→6)": (V5 - V6) / 25,
        }

        for nome, corrente in correntes.items():
            print(f"   - Corrente {nome}: {corrente:.4f} A")

        print("\n(Uma corrente negativa indica sentido oposto ao assumido)")
    else:
        print("❌ Não foi possível resolver o sistema de equações.")
    print("="*50)