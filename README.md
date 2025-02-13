# Problema dos Três Corpos

Este projeto implementa uma simulação do **Problema dos Três Corpos**, um problema clássico da mecânica celeste que descreve a interação gravitacional entre três corpos massivos. A solução é obtida numericamente utilizando `solve_ivp` da biblioteca SciPy e visualizada por meio de gráficos e animações em `matplotlib`.

## Conceito Científico

O Problema dos Três Corpos consiste em determinar as trajetórias de três corpos que interagem gravitacionalmente, sem solução analítica geral. Este projeto utiliza integração numérica para resolver as equações diferenciais do movimento.

## Estrutura do Projeto

- `3bodyproblem.py` → Script principal que resolve as equações diferenciais e gera a animação.
- **Gráficos e animações** → O código gera gráficos das trajetórias e um vídeo da simulação.

## 🚀 Como Executar

### 1. Clonar o Repositório
```sh
git clone https://github.com/seu-usuario/3bodyproblem.git
cd 3bodyproblem
```
### 2. Instalar as dependências (se necessário):
```sh
  pip install numpy matplotlib scipy
```

### 3. Executar o script:
```sh
  python 3bodyproblem.py
```

📌 Notas
O método solve_ivp é utilizado para resolver as equações diferenciais de forma eficiente.
A animação é criada usando FuncAnimation para visualizar o movimento orbital.
O vídeo final é salvo em alta qualidade com FFMpegWriter.
