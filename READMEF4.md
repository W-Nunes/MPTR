
Desafio Hermes Reply - Fase 4: Simulação e Análise de Dados
Projeto: Monitoramento Preditivo de Turbinas de Refrigeração<br>

1. Introdução
Este projeto representa a entrega do desafio em parceria com a Hermes Reply, com foco na construção de um sistema simulado de coleta e análise de dados para monitoramento industrial. Utilizando Wokwi, VSCode e PlatformIO, desenvolvemos um circuito com um ESP32 para simular o monitoramento de uma turbina, coletando dados de vibração e ruído para identificar padrões e anomalias.
O fluxo de trabalho é inteiramente local: os dados são gerados na simulação, capturados via Monitor Serial e analisados com um script Python para gerar visualizações.
2. Sensores Virtuais e Circuito
 * Sensores: Utilizamos dois potenciômetros para simular os sensores de Vibração (ligado ao pino 27) e Ruído (ligado ao pino 26).
 * Justificativa: Potenciômetros oferecem controle manual e intuitivo sobre os valores analógicos, permitindo simular com precisão cenários de operação normal, sobrecarga e falha súbita.
 * Circuito: O esquema abaixo mostra as conexões no Wokwi.
[IMAGEM AQUI: Insira um print de tela do seu circuito montado no Wokwi]
3. Coleta e Registro de Dados
O código main.ino lê os valores dos sensores a cada 2 segundos. Com base em limiares pré-definidos, ele atribui um status (NORMAL, ALERTA_SOBRECARGA, ALERTA_FALHA_SUBITA) à leitura. Os dados são impressos no Monitor Serial em formato CSV, prontos para serem copiados.
   [monitor.png]
4. Análise de Dados e Gráficos
Os dados coletados do Monitor Serial foram salvos em um ficheiro dados_coletados.csv e analisados com um script Python (analise_dados.py) utilizando as bibliotecas Pandas, Matplotlib e Seaborn.
4.1 Gráfico de Linha: Histórico dos Sensores
Este gráfico mostra a evolução das leituras de vibração e ruído ao longo do tempo, sendo ideal para identificar tendências de degradação ou eventos anômalos pontuais.
[IMAGEM AQUI: Insira o ficheiro grafico_linha.png gerado pelo script]
4.2 Gráfico de Dispersão: Correlação Vibração vs. Ruído
Este gráfico é fundamental para entender a relação entre as duas variáveis. Cada ponto representa uma leitura, e a sua cor indica o status da turbina naquele momento.
 * Eixo X: Leitura de Vibração
 * Eixo Y: Leitura de Ruído
 * Cor: Status da Turbina
Com este gráfico, podemos identificar visualmente os "clusters" ou agrupamentos que definem cada estado operacional. Por exemplo, esperamos ver um cluster de pontos "ALERTA_SOBRECARGA" no canto superior direito (alta vibração e alto ruído).
[IMAGEM AQUI: Insira o ficheiro grafico_dispersao.png gerado pelo script]
Esta análise inicial confirma que o sistema de coleta é funcional e que os dados gerados são relevantes e suficientes para treinar um futuro modelo de machine learning para classificar o estado da turbina automaticamente.
