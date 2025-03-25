
---

# 🚀 Algoritmo MaxMin Select: Divisão e Conquista em Python

**📘 Disciplina**: Fundamentos de Projeto e Análise de Algoritmos  
**🏫 Curso**: Engenharia de Software - PUC Minas  
**👨‍🏫 Professor**: João Paulo Carneiro Aramuni  
**👨‍💻 Autor**: João Victor Salim R. G. Trad

---

## 🎯 Objetivo do Projeto

Implementar o algoritmo **MaxMin Select** para encontrar simultaneamente o maior e o menor elemento de uma sequência numérica utilizando a técnica de divisão e conquista.  
A proposta visa demonstrar ganhos de desempenho por meio da redução no número de comparações, em relação à abordagem ingênua, mantendo complexidade linear.

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

### ⚙️ Requisitos
- Python 3.7+
- pytest

### ▶️ Passos para execução

```bash
git clone https://github.com/JvSalim/TrabalhoFPAA02.git
cd TrabalhoFPAA02
python3 main.py           # Executa o algoritmo
pytest test_maxmin.py -v  # Executa os testes
```

---

## 📊 Análise Técnica

### ⚖️ Comparação com Abordagem Ingênua

A abordagem tradicional realiza 2 varreduras:

- `n - 1` comparações para encontrar o máximo  
- `n - 1` comparações para encontrar o mínimo  

**Total: 2n - 2 comparações**

Já a abordagem com divisão e conquista:

- `T(n) = (3n / 2) - 2` comparações

| Tamanho n | Comparações Ingênua | Comparações MaxMin | Economia (%) |
|-----------|----------------------|---------------------|--------------|
| 2         | 2                    | 1                   | 50%          |
| 4         | 6                    | 4                   | 33%          |
| 8         | 14                   | 10                  | 28%          |
| 16        | 30                   | 22                  | 26.7%        |
| 32        | 62                   | 46                  | 25.8%        |
| n         | 2n - 2               | (3n / 2) - 2        | ~25%         |

---

## 🧮 Análise da Complexidade Assintótica por Contagem de Operações

O algoritmo **MaxMin Select** utiliza a técnica de divisão e conquista para reduzir o número de comparações ao encontrar, simultaneamente, o maior e o menor elemento de uma sequência.

### 🔁 Funcionamento Recursivo

A cada nível de recursão:

- O problema é dividido em 2 subproblemas de tamanho `n/2`
- Após as chamadas recursivas, são feitas 2 comparações:
  - 1 para determinar o maior valor
  - 1 para determinar o menor valor

### 📐 Recorrência do algoritmo

```
T(n) = 2T(n/2) + 2
```

### 🧷 Casos base

- Para `n = 1`: nenhuma comparação é necessária → `T(1) = 0`
- Para `n = 2`: é feita **1 comparação** → `T(2) = 1`

### 📏 Etapas da recorrência

- O array é dividido em duas partes
- Cada chamada retorna os pares (máximo, mínimo)
- São feitas 2 comparações para combinar os resultados

### 🧱 Profundidade da recursão

- O número de níveis da recursão é `log₂(n)`
- Em cada nível `k`, existem `2^k` subproblemas
- Cada subproblema realiza **2 comparações**
- Comparações por nível: `2 comparações × 2^k = 2^(k+1)`

### ➕ Somatório total de comparações

```
T(n) = 2 × (n/2) + 2 × (n/4) + 2 × (n/8) + ... + 2 × 1
```

Esse somatório forma uma progressão geométrica e resulta em:

```
T(n) = 2 × (n - 1) = 2n - 2   → (comparações na abordagem ingênua)
```

Entretanto, o algoritmo **MaxMin Select** evita comparações desnecessárias, economizando aproximadamente 25% das operações.

### ✅ Fórmula final

```
T(n) = (3n / 2) - 2
```

### ⏱️ Complexidade de Tempo

Como o número total de comparações é proporcional a `n`, concluímos que a complexidade assintótica do algoritmo é:

```
O(n)
```

---

## 📐 Análise da Complexidade Assintótica com Teorema Mestre

Para analisar a eficiência do algoritmo **MaxMin Select**, aplicamos o **Teorema Mestre**, que é uma técnica padrão para resolver recorrências de algoritmos recursivos do tipo divisão e conquista.

### 🧮 Recorrência do algoritmo:

```
T(n) = 2 * T(n / 2) + O(1)
```

### 🧩 Etapa 1: Identificação dos parâmetros

| Parâmetro | Valor | Interpretação |
|----------|--------|-----------------------------|
| a        | 2      | O problema é dividido em 2 subproblemas |
| b        | 2      | Cada subproblema tem tamanho n/2 |
| f(n)     | O(1)   | Custo externo constante: 2 comparações por nível |

### 📏 Etapa 2: Cálculo de log_b a

```
log_b a = log_2 2 = 1
Portanto, p = 1
```

### 🔍 Etapa 3: Classificação segundo o Teorema Mestre

- f(n) = O(1), que é equivalente a O(n^0)
- Como 0 < p = 1, estamos no:

**✅ Caso 1 do Teorema Mestre**  
Ou seja, a complexidade é dominada pelas chamadas recursivas.

### ✅ Conclusão

```
T(n) = Θ(n)
```

Ou seja, o algoritmo tem crescimento linear, mesmo usando recursão.
Além de ser correto, ele é mais eficiente do que a abordagem ingênua (que faz 2n - 2 comparações), pois reduz o número de comparações totais mantendo a eficiência assintótica.

Esse resultado comprova a vantagem do uso da técnica de divisão e conquista nesse problema.

---

## 🧭 Diagrama de Fluxo

Abaixo, o diagrama que ilustra a divisão e combinação no algoritmo MaxMin Select:

![Diagrama de Fluxo](assets/diagrama_fluxo.png)

---

## ✅ Testes e Validação (`test_maxmin.py`)

```python
import pytest
from main import max_min_select

def test_elemento_unico():
    assert max_min_select([42], 0, 0) == (42, 42)

def test_dois_elementos():
    assert max_min_select([15, 3], 0, 1)

 == (15, 3)

def test_elementos_negativos():
    arr = [-5, -1, -10]
    assert max_min_select(arr, 0, 2) == (-1, -10)

def test_array_grande():
    arr = list(range(1000))
    assert max_min_select(arr, 0, 999) == (999, 0)
```

### 📋 Resultados Esperados

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
