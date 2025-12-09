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


## Saída do Sistema
Você tem razão! O estilo "híbrido" (Acadêmico + Negócios) que usamos no anterior ficou muito bom porque eleva o nível da conversa. Mostra que você tem base teórica (Ciência da Computação) aplicada a problemas reais.

Para a vaga de Analista, isso é ótimo porque o termo "Otimização Combinatória" ou "Heurística" soa muito sofisticado.

Vamos adaptar exatamente naquele modelo para o projeto das Formigas. Ficou bem mais imponente.

Aqui está o README definitivo para a Colônia de Formigas, seguindo a estrutura que você gostou:
Copie e cole no arquivo README.md:
Markdown

# Otimização Logística com Colônia de Formigas 🐜

Este projeto consiste na implementação de uma meta-heurística de **Otimização por Colônia de Formigas (ACO)** aplicada à solução de um problema complexo de logística: o roteamento inteligente de transportes sensível a custos variáveis.

O sistema simula o comportamento biológico de cooperação de formigas (através de trilhas de feromônio) para encontrar a rota mais eficiente em um grafo, resolvendo variações do clássico **Problema do Caixeiro Viajante (TSP)**.

> Desenvolvido como parte prática da disciplina de **Inteligência Artificial / Otimização**.

## 🎯 O Problema de Negócio Modelado

Ao contrário de algoritmos simples de "menor caminho" (como Dijkstra puro), esta implementação modela um cenário logístico real onde a decisão deve ponderar múltiplos fatores conflitantes:

- **Custo de Pedágio (`W_PEDAGIO`):** O sistema avalia se vale a pena pegar uma rota mais curta, porém mais cara devido a tarifas.
- **Tempo de Viagem (`W_TEMPO`):** Considera o impacto da duração da rota na produtividade, diferenciando rotas expressas de rotas lentas.
- **Distância Física (`W_DISTANCIA`):** O consumo de combustível e desgaste da frota baseados na quilometragem.
- **Convergência Inteligente:** O algoritmo aprende com as iterações (feromônio), descartando rotas que são tecnicamente viáveis, mas economicamente inviáveis.

## 🛠️ Tecnologias Utilizadas

- **Linguagem:** Python 3.10+
- **NumPy:** Utilizado para manipulação de matrizes tridimensionais (Origem x Destino x Tipo de Rota) e cálculos probabilísticos vetorizados.
- **Matplotlib:** Para plotagem visual do grafo, demonstrando as rotas exploradas pela colônia (verde) versus a solução ótima consolidada (azul).

## 🚀 Como Executar

1. Instale as dependências:
   ```bash
   pip install -r requirements.txt

    Execute a simulação:
    Bash

    python main.py

📊 Saída do Sistema

O sistema exibe o progresso das gerações no terminal, mostrando a redução progressiva do custo logístico à medida que a colônia converge. Ao final, é gerado um mapa visual destacando o "Caminho Ótimo" encontrado pela inteligência coletiva dos agentes.

## Autor
Guilherme Augusto Boquimpani
