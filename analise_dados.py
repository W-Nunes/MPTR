import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def analisar_dados_turbina(caminho_arquivo):
    """
    Lê os dados de um arquivo CSV, gera gráficos de linha e de dispersão
    e imprime estatísticas básicas.
    """
    try:
        # Carrega os dados do arquivo CSV
        df = pd.read_csv(caminho_arquivo)

        # --- Verificação dos Dados ---
        print("--- Primeiras 5 linhas dos dados ---")
        print(df.head())
        print("\n--- Estatísticas Descritivas ---")
        print(df.describe())

        # --- Visualização dos Dados ---
        print("\nGerando gráficos...")
        sns.set_theme(style="whitegrid")

        # 1. GRÁFICO DE LINHA (Histórico dos Sensores)
        plt.figure(figsize=(14, 7))
        plt.plot(df['Timestamp'], df['Vibracao'], label='Vibração', color='blue', marker='o', linestyle='-')
        plt.plot(df['Timestamp'], df['Ruido'], label='Ruído', color='red', marker='x', linestyle='--')
        plt.title('Monitoramento dos Sensores da Turbina ao Longo do Tempo', fontsize=16)
        plt.xlabel('Timestamp (ms)', fontsize=12)
        plt.ylabel('Leitura Analógica (0-4095)', fontsize=12)
        plt.legend()
        plt.tight_layout()
        plt.savefig('grafico_linha.png')
        print("Gráfico de linha salvo como 'grafico_linha.png'")
        plt.show()

        # 2. GRÁFICO DE DISPERSÃO (Correlação Vibração vs. Ruído)
        plt.figure(figsize=(12, 8))
        # O parâmetro 'hue' colore os pontos com base na coluna 'Status'
        sns.scatterplot(
            data=df, 
            x='Vibracao', 
            y='Ruido', 
            hue='Status', 
            palette='viridis', # Esquema de cores
            s=100, # Tamanho dos pontos
            alpha=0.8 # Transparência
        )
        plt.title('Correlação entre Vibração e Ruído por Status', fontsize=16)
        plt.xlabel('Leitura de Vibração', fontsize=12)
        plt.ylabel('Leitura de Ruído', fontsize=12)
        plt.legend(title='Status da Turbina')
        plt.tight_layout()
        plt.savefig('grafico_dispersao.png')
        print("Gráfico de dispersão salvo como 'grafico_dispersao.png'")
        plt.show()

    except FileNotFoundError:
        print(f"Erro: O arquivo '{caminho_arquivo}' não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

# --- Execução Principal ---
if __name__ == "__main__":
    nome_do_arquivo = 'dados_coletados.csv'
    analisar_dados_turbina(nome_do_arquivo)
