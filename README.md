# 🧬 Otimizador de Alocação de Equipes com Algoritmo Genético

Este projeto implementa um **Algoritmo Genético (AG)** aplicado à solução de um problema complexo de gestão corporativa: a alocação ótima de recursos humanos (desenvolvedores) em projetos de software.

O sistema simula o processo de evolução natural (seleção, cruzamento e mutação) para encontrar a melhor combinação possível de equipes, resolvendo um problema clássico de **otimização combinatória** onde a força bruta seria matematicamente inviável.

> Desenvolvido como parte prática da disciplina de Inteligência Artificial / Otimização.

## 📦 Tecnologias Utilizadas

- **Python 3.8+**
- **NumPy:** Manipulação vetorial de alta performance para a população de cromossomos e cálculo matricial da aptidão.
- **Matplotlib:** Geração de gráficos de convergência, permitindo visualizar a evolução da aptidão (Fitness) ao longo das gerações.

## 💼 O Problema de Negócio Modelado

Diferente de exemplos teóricos simples, este algoritmo traduz variáveis reais de um ambiente corporativo de TI em funções matemáticas para calcular a aptidão (Fitness) de cada solução:

- **Níveis de Senioridade:** Diferenciação de produtividade e custo da folha salarial entre perfis Júnior, Pleno e Sênior.
- **Match de Habilidades:** Penaliza severamente a alocação de equipes que não possuem a *stack* tecnológica mínima exigida pelo projeto (ex: Python, React, AWS).
- **Prazos e Multas:** Projeta o tempo de entrega baseado no esforço estimado versus a força de trabalho alocada, aplicando penalidades financeiras em caso de atraso.
- **Viabilidade Financeira (ROI):** Busca o ponto de equilíbrio perfeito entre o custo operacional da equipe e a receita projetada do projeto.

## 👩🏽‍💻 O Processo de Desenvolvimento

O primeiro e maior desafio foi a modelagem do "DNA" (Cromossomo). Precisei criar uma estrutura de dados eficiente com o NumPy onde cada gene representasse a alocação de um desenvolvedor específico a um projeto.

A segunda etapa foi construir a função mais crítica do sistema: a **Função de Aptidão (Fitness Function)**. Tive que traduzir regras de negócio humanas (ex: "um projeto precisa de pelo menos um sênior" ou "estourar o orçamento é pior do que atrasar 2 dias") em equações matemáticas com pesos diferentes.

Com o ambiente modelado, implementei os operadores genéticos. Criei um sistema de **Seleção** (dando mais chance de reprodução para as melhores equipes), **Crossover** (combinando parte da equipe A com a equipe B para gerar uma nova solução) e **Mutação** (trocando aleatoriamente um dev de projeto para evitar que o algoritmo ficasse preso em um ótimo local).

Por fim, integrei o Matplotlib para rastrear a curva de aprendizado, garantindo que o algoritmo realmente convergisse para a solução ótima ao longo das gerações.

## 📚 O Que Eu Aprendi

Este projeto me ensinou a ponte entre a Engenharia de Software e a Gestão de Negócios.

🧠 **Otimização Combinatória:**
- Entendi na prática a explosão combinatória. Tentar testar todas as combinações de devs e projetos usando força bruta (loops) levaria anos de processamento, provando a necessidade real das meta-heurísticas (AG) para resolver problemas em tempo hábil.

⚙️ **Ajuste de Hiperparâmetros (Tuning):**
- Aprendi a calibrar taxas de mutação, tamanho da população e critérios de parada. Percebi que uma mutação muito alta transforma a evolução em uma busca aleatória caótica, enquanto uma muito baixa estagna o aprendizado.

📊 **Tradução de Regras de Negócio:**
- Aprimorei minha habilidade de sentar com a "visão do cliente/gestor" e transformar restrições subjetivas de orçamento e prazo em código lógico e penalidades matemáticas.

## 🚀 Como Executar

1. Clone o repositório:
```bash
git clone [https://github.com/guiibqn/otimizador-alocacao-equipes.git](https://github.com/guiibqn/otimizador-alocacao-equipes.git)
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Execute a simulação:
```bash
python main.py
```

## Autor
Guilherme Augusto Boquimpani
