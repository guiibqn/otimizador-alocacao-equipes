# Otimização de Equipes com Algoritmo Genético

Este projeto consiste na implementação de um **Algoritmo Genético (AG)** aplicado à solução de um problema complexo de gestão: a alocação ótima de recursos humanos em projetos de software.

O sistema simula o processo de evolução natural para encontrar a melhor combinação possível de equipes, visando maximizar o lucro e a eficiência, resolvendo um problema clássico de **otimização combinatória**.

> Desenvolvido como parte prática da disciplina de **Inteligência Artificial / Otimização**.

## O Problema de Negócio Modelado

Diferente de exemplos teóricos simples, este algoritmo considera variáveis reais de um ambiente corporativo para calcular a aptidão (Fitness) de cada solução:

- **Níveis de Senioridade:** Diferenciação de produtividade e custo entre Júnior, Pleno e Sênior.
- **Match de Habilidades:** Penaliza a alocação de equipes que não possuem a stack tecnológica exigida pelo projeto (ex: Python, React, AWS).
- **Prazos e Multas:** O algoritmo projeta o tempo de entrega baseado no esforço total vs. força de trabalho, aplicando penalidades por atraso.
- **Viabilidade Financeira:** Busca o equilíbrio entre o custo da folha salarial e a receita projetada.

## Tecnologias Utilizadas

- **Linguagem:** Python 3.8+
- **NumPy:** Utilizado para manipulação vetorial de alta performance da população e cromossomos.
- **Matplotlib:** Para geração de gráficos de convergência, permitindo visualizar a evolução da aptidão (Fitness) ao longo das gerações.

## Como Executar

1. Clone o repositório:
   ```bash
   git clone [https://github.com/guiibqn/team-allocation-optimizer.git](https://github.com/guiibqn/otimizador-alocacao-equipes.git)
2. Instale as dependências:
    ```bash
    pip install -r requirements.txt
3. Execute o otimizador:
    ```bash
    python main.py

## Autor
Guilherme Augusto Boquimpani