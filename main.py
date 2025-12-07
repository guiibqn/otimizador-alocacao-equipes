import numpy as np
import random
import matplotlib.pyplot as plt
from typing import Final

# --- DEFINIÇÃO DOS DADOS DE ENTRADA ---

DESENVOLVEDORES: Final[list] = [
# --- Sêniors (9) ---
    {'id': 0, 'nivel': 'Senior', 'custo': 15000, 'habilidades': ['Python', 'AWS', 'Arquitetura'], 'produtividade': 10},
    {'id': 1, 'nivel': 'Senior', 'custo': 15000, 'habilidades': ['React', 'NodeJS', 'Docker'], 'produtividade': 11},
    {'id': 2, 'nivel': 'Senior', 'custo': 16000, 'habilidades': ['Python', 'Banco de Dados', 'ML'], 'produtividade': 9},
    {'id': 3, 'nivel': 'Senior', 'custo': 14000, 'habilidades': ['React', 'Python', 'Docker'], 'produtividade': 10},
    {'id': 4, 'nivel': 'Senior', 'custo': 17000, 'habilidades': ['Java', 'Spring', 'AWS'], 'produtividade': 12},
    {'id': 5, 'nivel': 'Senior', 'custo': 15500, 'habilidades': ['Angular', 'NodeJS', 'Banco de Dados'], 'produtividade': 10},
    {'id': 6, 'nivel': 'Senior', 'custo': 16500, 'habilidades': ['C#', '.NET', 'Azure'], 'produtividade': 11},
    {'id': 7, 'nivel': 'Senior', 'custo': 15800, 'habilidades': ['Python', 'TensorFlow', 'ML'], 'produtividade': 10},
    {'id': 8, 'nivel': 'Senior', 'custo': 15200, 'habilidades': ['React', 'GraphQL', 'Docker'], 'produtividade': 9},
    {'id': 9, 'nivel': 'Senior', 'custo': 16000, 'habilidades': ['Python', 'ML', 'Arquitetura'], 'produtividade': 11},
    {'id': 10, 'nivel': 'Senior', 'custo': 15500, 'habilidades': ['.NET', 'Azure', 'C#'], 'produtividade': 10},
    {'id': 11, 'nivel': 'Senior', 'custo': 17000, 'habilidades': ['Arquitetura', 'AWS', 'Java'], 'produtividade': 12},
    {'id': 12, 'nivel': 'Senior', 'custo': 15000, 'habilidades': ['Docker', 'NodeJS', 'AWS'], 'produtividade': 10},

    # --- Plenos (12) ---
    {'id': 13, 'nivel': 'Pleno', 'custo': 9000, 'habilidades': ['Python', 'Git'], 'produtividade': 7},
    {'id': 14, 'nivel': 'Pleno', 'custo': 9000, 'habilidades': ['React', 'CSS'], 'produtividade': 6},
    {'id': 15, 'nivel': 'Pleno', 'custo': 10000, 'habilidades': ['NodeJS', 'Banco de Dados'], 'produtividade': 8},
    {'id': 16, 'nivel': 'Pleno', 'custo': 8500, 'habilidades': ['Docker', 'Git'], 'produtividade': 6},
    {'id': 17, 'nivel': 'Pleno', 'custo': 9500, 'habilidades': ['Java', 'Git'], 'produtividade': 7},
    {'id': 18, 'nivel': 'Pleno', 'custo': 9200, 'habilidades': ['Python', 'Flask'], 'produtividade': 6},
    {'id': 19, 'nivel': 'Pleno', 'custo': 8800, 'habilidades': ['Angular', 'CSS'], 'produtividade': 5},
    {'id': 20, 'nivel': 'Pleno', 'custo': 9300, 'habilidades': ['React', 'Git'], 'produtividade': 7},
    {'id': 21, 'nivel': 'Pleno', 'custo': 9800, 'habilidades': ['C#', '.NET'], 'produtividade': 8},
    {'id': 22, 'nivel': 'Pleno', 'custo': 9400, 'habilidades': ['AWS', 'Docker'], 'produtividade': 7},
    {'id': 23, 'nivel': 'Pleno', 'custo': 9100, 'habilidades': ['Python', 'Banco de Dados'], 'produtividade': 6},
    {'id': 24, 'nivel': 'Pleno', 'custo': 8700, 'habilidades': ['NodeJS', 'GraphQL'], 'produtividade': 7},
    {'id': 25, 'nivel': 'Pleno', 'custo': 9600, 'habilidades': ['Python', 'TensorFlow'], 'produtividade': 8}, 
    {'id': 26, 'nivel': 'Pleno', 'custo': 9700, 'habilidades': ['Python', 'ML', 'Git'], 'produtividade': 7}, 
    {'id': 27, 'nivel': 'Pleno', 'custo': 9500, 'habilidades': ['AWS', 'Python'], 'produtividade': 8},
    {'id': 28, 'nivel': 'Pleno', 'custo': 9200, 'habilidades': ['React', 'CSS', 'Git'], 'produtividade': 6},
    {'id': 29, 'nivel': 'Pleno', 'custo': 9800, 'habilidades': ['Java', 'Spring', 'Banco de Dados'], 'produtividade': 7},
    {'id': 30, 'nivel': 'Pleno', 'custo': 10000, 'habilidades': ['AWS', 'Docker', 'NodeJS'], 'produtividade': 8},
    {'id': 31, 'nivel': 'Pleno', 'custo': 9000, 'habilidades': ['Angular', 'CSS'], 'produtividade': 6},
    {'id': 32, 'nivel': 'Pleno', 'custo': 9300, 'habilidades': ['React', 'NodeJS'], 'produtividade': 7},
    {'id': 33, 'nivel': 'Pleno', 'custo': 9100, 'habilidades': ['Python', 'ML'], 'produtividade': 7},
    {'id': 34, 'nivel': 'Pleno', 'custo': 8800, 'habilidades': ['GraphQL', 'React'], 'produtividade': 6},
    {'id': 35, 'nivel': 'Pleno', 'custo': 9500, 'habilidades': ['TensorFlow', 'Python'], 'produtividade': 8},
    
    # --- Júniors (9) ---
    {'id': 36, 'nivel': 'Junior', 'custo': 5000, 'habilidades': ['Python', 'HTML'], 'produtividade': 3},
    {'id': 37, 'nivel': 'Junior', 'custo': 5000, 'habilidades': ['React', 'CSS'], 'produtividade': 4},
    {'id': 38, 'nivel': 'Junior', 'custo': 5500, 'habilidades': ['Git', 'HTML'], 'produtividade': 2},
    {'id': 39, 'nivel': 'Junior', 'custo': 5200, 'habilidades': ['Banco de Dados'], 'produtividade': 3},
    {'id': 40, 'nivel': 'Junior', 'custo': 5100, 'habilidades': ['Java', 'HTML'], 'produtividade': 3},
    {'id': 41, 'nivel': 'Junior', 'custo': 5300, 'habilidades': ['Python'], 'produtividade': 4},
    {'id': 42, 'nivel': 'Junior', 'custo': 5400, 'habilidades': ['C#', 'Git'], 'produtividade': 3},
    {'id': 43, 'nivel': 'Junior', 'custo': 5250, 'habilidades': ['CSS', 'HTML'], 'produtividade': 2},
    {'id': 44, 'nivel': 'Junior', 'custo': 5350, 'habilidades': ['Python', 'Git'], 'produtividade': 3},
    {'id': 45, 'nivel': 'Junior', 'custo': 5500, 'habilidades': ['HTML', 'CSS', 'Git'], 'produtividade': 3},
    {'id': 46, 'nivel': 'Junior', 'custo': 5200, 'habilidades': ['Python', 'Git'], 'produtividade': 4},
    {'id': 47, 'nivel': 'Junior', 'custo': 5300, 'habilidades': ['Java', 'Git'], 'produtividade': 4},
    {'id': 48, 'nivel': 'Junior', 'custo': 5000, 'habilidades': ['C#', 'Git'], 'produtividade': 3},
    {'id': 49, 'nivel': 'Junior', 'custo': 5400, 'habilidades': ['Banco de Dados', 'HTML'], 'produtividade': 3},
    
]

PROJETOS: Final[dict] = {
    0: {'nome': 'Phoenix',   'receita': 150000, 'prazo': 40, 'esforco': 500,  'habilidades_req': ['Python', 'AWS']},
    1: {'nome': 'Hydra',     'receita': 250000, 'prazo': 70, 'esforco': 800,  'habilidades_req': ['React', 'NodeJS', 'Docker']},
    2: {'nome': 'Cerberus',  'receita': 450000, 'prazo': 120,'esforco': 1500, 'habilidades_req': ['Java', 'Spring', 'Banco de Dados']},
    3: {'nome': 'Orion',     'receita': 220000, 'prazo': 60, 'esforco': 750,  'habilidades_req': ['Python', 'ML']},
    4: {'nome': 'Pegasus',   'receita': 300000, 'prazo': 90, 'esforco': 1000, 'habilidades_req': ['Angular', 'NodeJS', 'Git']},
    5: {'nome': 'Kraken',    'receita': 500000, 'prazo': 150,'esforco': 1800, 'habilidades_req': ['C#', '.NET', 'Azure']},
    6: {'nome': 'Titan',     'receita': 200000, 'prazo': 50, 'esforco': 650,  'habilidades_req': ['Python', 'TensorFlow']},
    7: {'nome': 'Vulcan',    'receita': 320000, 'prazo': 100,'esforco': 1100, 'habilidades_req': ['React', 'GraphQL', 'Docker']},
    8: {'nome': 'Atlas',     'receita': 180000, 'prazo': 50, 'esforco': 550,  'habilidades_req': ['Python', 'Flask', 'Git']},
    9: {'nome': 'Chimera',   'receita': 350000, 'prazo': 80, 'esforco': 900,  'habilidades_req': ['Java', 'AWS', 'Docker']},
    10: {'nome': 'Gorgon',   'receita': 280000, 'prazo': 75, 'esforco': 700,  'habilidades_req': ['C#', 'Banco de Dados']},
    11: {'nome': 'Apollo',   'receita': 400000, 'prazo': 110,'esforco': 1300, 'habilidades_req': ['ML', 'TensorFlow', 'Arquitetura']},
    12: {'nome': 'Icarus',   'receita': 260000, 'prazo': 70, 'esforco': 600,  'habilidades_req': ['React', 'GraphQL']},
    13: {'nome': 'Prometheus','receita': 550000, 'prazo': 130,'esforco': 1600, 'habilidades_req': ['Python', 'AWS', 'Banco de Dados']},
    14: {'nome': 'Echo',     'receita': 120000, 'prazo': 30, 'esforco': 300,  'habilidades_req': ['Angular', 'CSS']},
    15: {'nome': 'Cronos',   'receita': 700000, 'prazo': 200,'esforco': 2500, 'habilidades_req': ['Java', '.NET', 'Arquitetura']},
    16: {'nome': 'Hephaestus','receita': 90000, 'prazo': 45, 'esforco': 350,  'habilidades_req': ['Python', 'Flask', 'Git']},
    17: {'nome': 'Nyx',      'receita': 210000, 'prazo': 60, 'esforco': 400,  'habilidades_req': ['Docker', 'AWS', 'Azure']},
    18: {'nome': 'Midas',    'receita': 380000, 'prazo': 90, 'esforco': 950,  'habilidades_req': ['NodeJS', 'Banco de Dados', 'GraphQL']},
    19: {'nome': 'Athena',   'receita': 600000, 'prazo': 150,'esforco': 1700, 'habilidades_req': ['ML', 'TensorFlow', 'Python']},
}

# --- HIPERPARÂMETROS DO ALGORITMO GENÉTICO ---

NUM_DEVS: Final[int] = len(DESENVOLVEDORES)
NUM_PROJETOS: Final[int] = len(PROJETOS)

# O cromossomo representa a alocação:
# O índice [i] é o Dev de ID [i].
# O valor é o ID do projeto (-1 se não alocado).
TAM_CROMO: Final[int] = NUM_DEVS
TAM_POP: Final[int] = 500
TAXA_CROSSOVER: Final[float] = 0.8
TAXA_MUTACAO: Final[float] = 0.05
NUM_GERACOES: Final[int] = 1000
ELITISMO: Final[int] = 5

# --- ESTRUTURAS DE DADOS GLOBAIS ---

pop = np.zeros((TAM_POP, TAM_CROMO), dtype=int)
nova_pop = np.zeros((TAM_POP, TAM_CROMO), dtype=int)
pais = np.zeros((2, TAM_CROMO), dtype=int)
filhos = np.zeros((2, TAM_CROMO), dtype=int)
nota_pop = np.zeros((TAM_POP, 3)) # Colunas: [indice_original, nota_fitness, prob_roleta]

# --- FUNÇÕES DO ALGORITMO GENÉTICO ---

def init_pop():
    """Inicializa a população com indivíduos aleatórios."""
    global pop
    for i in range(TAM_POP):
        cromossomo = []
        for dev_id in range(NUM_DEVS):
            if random.random() < 0.7: # 70% de chance de alocar
                projeto = random.randint(0, NUM_PROJETOS - 1)
                cromossomo.append(projeto)
            else:
                cromossomo.append(-1)  # -1 = Dev não alocado
        pop[i] = cromossomo


def avalia_pop():
    """Função de Aptidão (Fitness). Calcula a nota de cada indivíduo."""
    global nota_pop
    for i in range(TAM_POP):
        individuo = pop[i]
        
        # 1. Decodifica o cromossomo (alocação)
        equipes_por_projeto = {p_id: [] for p_id in PROJETOS}
        devs_alocados = []
        for dev_id, projeto_id in enumerate(individuo):
            if projeto_id != -1:
                equipes_por_projeto[projeto_id].append(DESENVOLVEDORES[dev_id])
                devs_alocados.append(DESENVOLVEDORES[dev_id])

        # 2. Calcula os componentes da nota (Lucro e Penalidades)
        
        # CRITÉRIO: Minimizar Custo
        custo_total = sum(dev['custo'] for dev in devs_alocados)

        receita_total = 0
        penalidade_habilidades = 0
        penalidade_prazo = 0
        penalidade_projeto_vazio = 0
        bonus_eficiencia = 0

        for p_id, equipe in equipes_por_projeto.items():
            projeto_atual = PROJETOS[p_id]
            
            if not equipe:
                # CRITÉRIO: Não deixar projeto vazio (Penalidade)
                penalidade_projeto_vazio += projeto_atual['receita'] * 0.5
                continue

            receita_total += projeto_atual['receita']

            # CRITÉRIO: Ter as habilidades necessárias (Penalidade)
            habilidades_requeridas = set(projeto_atual['habilidades_req'])
            habilidades_da_equipe = set().union(*(set(dev['habilidades']) for dev in equipe))
            skills_faltantes = habilidades_requeridas - habilidades_da_equipe
            if skills_faltantes:
                penalidade_habilidades += len(skills_faltantes) * (projeto_atual['receita'] * 0.25)

            
            soma_produtividade_equipe = sum(dev['produtividade'] for dev in equipe)
            if soma_produtividade_equipe > 0:
                tempo_estimado = projeto_atual['esforco'] / soma_produtividade_equipe
                prazo_oficial = projeto_atual['prazo']
                
                if tempo_estimado > prazo_oficial:
                    # CRITÉRIO: Entregar no prazo (Penalidade)
                    dias_de_atraso = tempo_estimado - prazo_oficial
                    penalidade_prazo += (dias_de_atraso / prazo_oficial) * projeto_atual['receita'] * 0.4
                else:
                    # CRITÉRIO: Maximizar Bônus por Adiantamento
                    dias_de_adiantamento = prazo_oficial - tempo_estimado
                    bonus_eficiencia += (dias_de_adiantamento / prazo_oficial) * projeto_atual['receita'] * 0.1
        
        # 3. Calcula a Nota Final (Fitness)
        # OBJETIVO PRINCIPAL: Maximizar a nota (Lucro)
        nota = (receita_total + bonus_eficiencia) - custo_total - penalidade_habilidades - penalidade_prazo - penalidade_projeto_vazio
        
        nota_pop[i, 0] = i
        nota_pop[i, 1] = nota
        nota_pop[i, 2] = -1

    # Ordena a população pela nota (do maior para o menor)
    nota_pop = nota_pop[nota_pop[:, 1].argsort()[::-1]]
    
    # --- Cálculo da Roleta (Seleção) ---
    # Ajusta as notas para o cálculo de probabilidade (trata notas negativas)
    min_nota = nota_pop[-1, 1]
    if min_nota < 0:
        ajuste = abs(min_nota) + 1
        notas_ajustadas = nota_pop[:, 1] + ajuste
        soma_nota_ajustada = np.sum(notas_ajustadas)
        acum = 0
        for i in range(TAM_POP):
            prob = notas_ajustadas[i] / soma_nota_ajustada
            acum += prob
            nota_pop[i, 2] = acum
    else:
        soma_nota = np.sum(nota_pop[:, 1])
        if soma_nota == 0:
            # Caso raro: todas as notas são 0
            prob_uniforme = 1.0 / TAM_POP
            acum = 0
            for i in range(TAM_POP):
                acum += prob_uniforme
                nota_pop[i, 2] = acum
        else:
            acum = 0
            for i in range(TAM_POP):
                prob = nota_pop[i, 1] / soma_nota
                acum += prob
                nota_pop[i, 2] = acum


def seleciona_pais():
    """Seleciona dois pais usando o método da Roleta."""
    global pais
    r_pai1, r_pai2 = random.random(), random.random()
    idx_pai1, idx_pai2 = -1, -1

    for i in range(TAM_POP):
        if idx_pai1 == -1 and nota_pop[i, 2] >= r_pai1:
            idx_pai1 = int(nota_pop[i, 0])
        if idx_pai2 == -1 and nota_pop[i, 2] >= r_pai2:
            idx_pai2 = int(nota_pop[i, 0])
        if idx_pai1 != -1 and idx_pai2 != -1:
            break
            
    pais[0] = pop[idx_pai1]
    pais[1] = pop[idx_pai2]


def cruza_pais():
    """Aplica crossover de 1 ponto nos pais para gerar filhos."""
    global filhos
    if random.random() < TAXA_CROSSOVER:
        corte = random.randint(1, TAM_CROMO - 1)
        filhos[0, :corte], filhos[0, corte:] = pais[0, :corte], pais[1, corte:]
        filhos[1, :corte], filhos[1, corte:] = pais[1, :corte], pais[0, corte:]
    else:
        filhos[0], filhos[1] = pais[0], pais[1]


def muta_filhos():
    """Aplica mutação nos filhos gerados."""
    global filhos
    for i in range(2):
        for j in range(TAM_CROMO):
            if random.random() < TAXA_MUTACAO:
                # 30% de chance de mutar para "não alocado"
                if random.random() < 0.3:  
                    filhos[i, j] = -1
                else: # 70% de chance de mutar para um projeto aleatório
                    filhos[i, j] = random.randint(0, NUM_PROJETOS - 1)


def elitismo(qtde):
    """Copia os 'qtde' melhores indivíduos da população atual para a nova."""
    global nova_pop
    for i in range(qtde):
        idx_melhor = int(nota_pop[i, 0])
        nova_pop[i] = pop[idx_melhor]


def imprime_melhor_solucao():
    """Decodifica e imprime a melhor solução encontrada."""
    melhor_individuo = pop[int(nota_pop[0, 0])]
    melhor_nota = nota_pop[0, 1]

    print("\n" + "="*30)
    print(">> MELHOR ALOCACAO ENCONTRADA <<")
    print(f"    Nota de Aptidao Final: {melhor_nota:,.2f}")
    print("="*30)
    
    equipes_por_projeto, _ = decodificar_individuo(melhor_individuo)
    
    custo_geral = 0
    for p_id, equipe in equipes_por_projeto.items():
        projeto = PROJETOS[p_id]
        custo_equipe = sum(d['custo'] for d in equipe)
        custo_geral += custo_equipe
        
        print(f"\n--- Projeto: {projeto['nome']} ---")
        if not equipe:
            print("    (Nenhuma equipe alocada)")
            continue

        soma_prod = sum(d['produtividade'] for d in equipe)
        tempo_est = projeto['esforco'] / soma_prod if soma_prod > 0 else float('inf')
        status = "NO PRAZO" if tempo_est <= projeto['prazo'] else "ATRASADO"

        print(f"    - Status: {status}")
        print(f"    - Custo da Equipe: R$ {custo_equipe:,.2f}")
        print(f"    - Produtividade Total da Equipe: {soma_prod}")
        print(f"    - Tempo Estimado: {tempo_est:.1f} dias (Prazo Oficial: {projeto['prazo']} dias)")
        print("    - Equipe Alocada:")
        
        equipe_ordenada = sorted(equipe, key=lambda d: ['Senior', 'Pleno', 'Junior'].index(d['nivel']))
        for dev in equipe_ordenada:
            print(f"      > Dev {dev['id']} ({dev['nivel']}) - Prod: {dev['produtividade']} - Skills: {dev['habilidades']}")
    
    print("\n" + "="*30)
    print(f"Custo Total de Salarios da Alocacao: R$ {custo_geral:,.2f}")
    print("="*30)


def decodificar_individuo(individuo):
    """Função auxiliar para traduzir um cromossomo em equipes."""
    equipes_por_projeto = {p_id: [] for p_id in PROJETOS}
    devs_alocados = []
    for dev_id, projeto_id in enumerate(individuo):
        if projeto_id != -1:
            equipes_por_projeto[projeto_id].append(DESENVOLVEDORES[dev_id])
            devs_alocados.append(DESENVOLVEDORES[dev_id])
    return equipes_por_projeto, devs_alocados

# --- EXECUÇÃO PRINCIPAL DO ALGORITMO ---

if __name__ == '__main__':
    
    # Listas para armazenar o histórico para o gráfico
    geracao_hist = []
    melhor_aptidao_hist = []
    pior_aptidao_hist = []
    media_aptidao_hist = []

    print("--- INICIANDO OTIMIZADOR DE ALOCACAO DE EQUIPES ---")
    
    init_pop()

    for i in range(NUM_GERACOES):
        avalia_pop()
        
        # Armazena dados para o gráfico
        geracao_hist.append(i)
        melhor_aptidao_hist.append(nota_pop[0, 1])  # A melhor nota (índice 0)
        pior_aptidao_hist.append(nota_pop[-1, 1])   # A pior nota (último índice)
        media_aptidao_hist.append(np.mean(nota_pop[:, 1])) 

        if (i + 1) % 50 == 0:
            print(f"Geracao {i+1}/{NUM_GERACOES} | Melhor Nota: {nota_pop[0, 1]:,.2f} | Media: {np.mean(nota_pop[:, 1]):,.2f}")

        # Elitismo: Os N melhores indivíduos passam direto
        elitismo(ELITISMO)
        
        # Preenche o resto da população com filhos (crossover + mutação)
        j = ELITISMO
        while j < TAM_POP:
            seleciona_pais()
            cruza_pais()
            muta_filhos()
            nova_pop[j] = filhos[0]
            if j + 1 < TAM_POP:
                nova_pop[j + 1] = filhos[1]
            j += 2

        pop = nova_pop.copy()

    
    imprime_melhor_solucao()

    
    # --- GERAÇÃO DO GRÁFICO ---
    plt.figure(figsize=(14, 8))

    plt.plot(geracao_hist, melhor_aptidao_hist, linewidth=2, color='green', label='Melhor Aptidão')
    plt.plot(geracao_hist, media_aptidao_hist, linewidth=2, color='blue', label='Aptidão Média', alpha=0.7)
    plt.plot(geracao_hist, pior_aptidao_hist, linewidth=1, color='red', label='Pior Aptidão', alpha=0.6)

    plt.title("Evolução da Aptidão da População por Geração", fontsize=16, pad=20)
    plt.xlabel("Geração", fontsize=12)
    plt.ylabel("Nota de Aptidão (Fitness)", fontsize=12)
    plt.legend(fontsize=10)
    plt.grid(True, alpha=0.3)

    # Ajuste automático do eixo Y para melhor visualização
    margin = 0.1
    y_range = max(melhor_aptidao_hist) - min(pior_aptidao_hist)
    if y_range > 0:
        plt.ylim(min(pior_aptidao_hist) - margin * y_range, 
                 max(melhor_aptidao_hist) + margin * y_range)

    plt.tight_layout()
    plt.show()