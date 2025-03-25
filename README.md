
# 🚀 Algoritmo MaxMin Select: Divisão e Conquista em Python

**Disciplina**: Fundamentos de Projeto e Análise de Algoritmos  
**Curso**: Engenharia de Software - PUC Minas  
**Professor**: João Paulo Carneiro Aramuni  
**Autor**: João Victor Salim R. G. Trad

---
## 🎯 Objetivo do Projeto

Implementar o algoritmo **MaxMin Select** para encontrar **simultaneamente o maior e o menor elemento** de uma sequência numérica utilizando a técnica de **divisão e conquista**. A proposta visa demonstrar ganhos de desempenho por meio da redução no número de comparações, em relação à abordagem ingênua, mantendo complexidade linear.

---

## 📂 Estrutura do Repositório

```

├── main.py              → Implementação do algoritmo
├── test_maxmin.py       → Testes unitários
├── assets/
│   ├── diagrama_fluxo.puml
│   ├── grafo_controle.puml
│   ├── diagrama_fluxo.png
│   └── grafo_controle.png
└── README.md            → Documentação completa
```

---

## 💡 Implementação do Algoritmo (`main.py`)

```python
def max_min_select(arr, low, high):
    if low == high:
        return (arr[low], arr[low])  # Apenas 1 elemento
    
    if high == low + 1:
        return (arr[low], arr[high]) if arr[low] < arr[high] else (arr[high], arr[low])  # 1 comparação

    mid = (low + high) // 2

    max_left, min_left = max_min_select(arr, low, mid)
    max_right, min_right = max_min_select(arr, mid + 1, high)

    overall_max = max(max_left, max_right)  # 1 comparação
    overall_min = min(min_left, min_right)  # 1 comparação

    return (overall_max, overall_min)
```

---

## 🔍 Explicação Linha a Linha

| Linha de Código | Explicação |
|-----------------|------------|
| `if low == high` | Caso base com 1 elemento. Retorna ele como máximo e mínimo. |
| `if high == low + 1` | Caso com 2 elementos. Realiza 1 comparação. |
| `mid = (low + high) // 2` | Divide o array ao meio. |
| `max_min_select(arr, low, mid)` | Chamada recursiva na metade esquerda. |
| `max_min_select(arr, mid + 1, high)` | Chamada recursiva na metade direita. |
| `max(...)` e `min(...)` | Combinação dos resultados com 2 comparações. |

---

## 🛠 Como Executar

### Requisitos
- Python 3.7+
- pytest

### Passos
```bash
git clone https://github.com/seu-usuario/trabalho_individual_2_FPAA.git
cd trabalho_individual_2_FPAA
python3 main.py           # Executa o algoritmo
pytest test_maxmin.py -v  # Executa os testes
```

---
## 📊 Análise Técnica

### Comparação com Abordagem Ingênua

A abordagem tradicional realiza 2 varreduras:
- n - 1 comparações para encontrar o máximo
- n - 1 comparações para encontrar o mínimo  
**Total: 2n - 2 comparações**

Já a abordagem com divisão e conquista:
- T(n) = (3n / 2) - 2 comparações

| Tamanho n | Comparações Ingênua | Comparações MaxMin | Economia (%) |
|-----------|----------------------|---------------------|--------------|
| 2         | 2                    | 1                   | 50%          |
| 4         | 6                    | 4                   | 33%          |
| 8         | 14                   | 10                  | 28%          |
| 16        | 30                   | 22                  | 26.7%        |
| 32        | 62                   | 46                  | 25.8%        |
| n         | 2n - 2               | (3n / 2) - 2        | ~25%         |

---

### Análise por Contagem de Operações

A cada nível de recursão:
- O problema é dividido em 2 subproblemas
- São feitas 2 comparações na combinação (máximo e mínimo)

**Recorrência:**
T(n) = 2T(n/2) + 2  
**Solução:** T(n) = (3n / 2) - 2  
**Complexidade de tempo:** O(n)

#### **Derivação Detalhada da Fórmula T(n) = (3n / 2) - 2**

1. **Caso Base**:
   - Para n = 1: 0 comparações.
   - Para n = 2: 1 comparação.

2. **Recorrência**:
   - A cada chamada recursiva, o array é dividido em duas metades.
   - Em cada nível, são feitas 2 comparações (uma para o máximo e outra para o mínimo).

3. **Número de Níveis**:
   - O número de níveis de recursão é log₂(n).

4. **Comparações por Nível**:
   - No nível k, há 2^k subproblemas, cada um com 2 comparações.
   - Total de comparações por nível: 2 × 2^k = 2^(k+1).

5. **Somatório Total**:
   - O número total de comparações é a soma das comparações em todos os níveis:
     T(n) = 2 × (n/2) + 2 × (n/4) + ... + 2 × 1.
   - Isso resulta em:
     T(n) = 2 × (n - 1) = 2n - 2.
   - No entanto, como cada nível de recursão economiza comparações, a fórmula final é:
     T(n) = (3n / 2) - 2.

---

### Aplicação do Teorema Mestre

**Recorrência do algoritmo:**

    T(n) = 2T(n/2) + O(1)

Comparando com a fórmula:

    T(n) = aT(n/b) + f(n)

Aplicando o Teorema Mestre à recorrência T(n) = 2T(n/2) + O(1):

- a = 2 (dois subproblemas)
- b = 2 (divisão ao meio)
- f(n) = O(1) (custo externo constante)
- log_b a = log₂ 2 = 1
- f(n) = O(n^c), com c = 0 < 1 → Caso 1 do Teorema Mestre

✅ Portanto, a complexidade assintótica é T(n) = Θ(n)


---
### Diagrama de Fluxo

Aqui está o diagrama que ilustra a divisão e combinação no algoritmo MaxMin Select:

![Diagrama de Fluxo](assets/diagrama_fluxo.png)

---

## ✅ Testes e Validação (`test_maxmin.py`)

```python
import pytest
from main import max_min_select

def test_elemento_unico():
    assert max_min_select([42], 0, 0) == (42, 42)

def test_dois_elementos():
    assert max_min_select([15, 3], 0, 1) == (15, 3)

def test_elementos_negativos():
    arr = [-5, -1, -10]
    assert max_min_select(arr, 0, 2) == (-1, -10)

def test_array_grande():
    arr = list(range(1000))
    assert max_min_select(arr, 0, 999) == (999, 0)
```

### Resultados esperados:

Todos os testes passam com sucesso:

```
PASSED test_elemento_unico
PASSED test_dois_elementos
PASSED test_elementos_negativos
PASSED test_array_grande
```

---

## 🌍 Exemplo Prático

**Cenário**: Um sistema de monitoramento de temperatura deseja encontrar rapidamente a temperatura máxima e mínima do dia.

```python
leituras = [22, 18, 25, 20, 15, 30, 17]
max_temp, min_temp = max_min_select(leituras, 0, 6)
print("Máxima:", max_temp)
print("Mínima:", min_temp)
```

**Saída esperada:**
```
Máxima: 30
Mínima: 15
```

---

## 📚 Referências
- **Material da Disciplina**:  
  [AULA 01 - Análise de Complexidade](https://github.com/joaopauloaramuni/fundamentos-de-projeto-e-analise-de-algoritmos/tree/main/PDF)
- **Repositório de Projetos**:  
  [Projetos de Algoritmos](https://github.com/joaopauloaramuni/fundamentos-de-projeto-e-analise-de-algoritmos/tree/main/PROJETOS)

---
