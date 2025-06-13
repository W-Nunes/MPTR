Monitoramento Preditivo de Turbinas de Refrigeração
Projeto de solução digital para o desafio da Hermes Reply, focado na prevenção de falhas em linhas de produção industrial através de IoT e Machine Learning.
📖 Sobre o Projeto
Este projeto descreve uma solução digital para o monitoramento e manutenção preditiva de turbinas de congelamento em câmaras frias. O sistema utiliza sensores de IoT (simulados via Wokwi e ESP32) para coletar dados de áudio e vibração em tempo real.




Os dados são armazenados e processados em um ambiente de nuvem, onde um modelo de Machine Learning (Scikit-learn) analisa os padrões para:
Detectar anomalias imediatas (paralisação súbita).
Prever a necessidade de manutenção futura (desgaste por acúmulo de gelo).




As informações e alertas são apresentados de forma clara e acionável em um dashboard interativo construído com Streamlit, permitindo que as equipes de manutenção atuem de forma proativa, reduzindo custos e perdas.
🎯 O Problema
A falha inesperada de turbinas em sistemas de refrigeração industrial é um problema crítico que acarreta perdas financeiras significativas. As falhas geralmente ocorrem de duas formas:



Degradação Gradual: O acúmulo de gelo nas hélices causa um desbalanceamento, alterando a frequência sonora e aumentando a vibração ao longo do tempo, até a eventual quebra.
Falha Súbita: Componentes elétricos ou mecânicos podem falhar subitamente, interrompendo a operação sem aviso prévio.




A manutenção corretiva (após a falha) é cara e ineficiente. A solução proposta visa substituir essa abordagem por uma estratégia de manutenção preditiva e baseada em condições.
🏛️ Arquitetura da Solução
A solução é dividida em quatro camadas lógicas, criando um pipeline de dados completo desde o sensor até o usuário final.
Camada 1: Coleta de Dados (IoT)
Sensores: Microfone (frequência sonora) e Acelerômetro/Potenciômetro (vibração).
Hardware: Microcontrolador ESP32 com conectividade Wi-Fi.
Simulação: Ambiente Wokwi + VS Code para prototipagem.
Comunicação: Dados em formato JSON enviados para a nuvem via protocolo MQTT.
Camada 2: Armazenamento de Dados (Cloud)
Ingestão: Broker MQTT em AWS IoT Core.
Armazenamento: Banco de dados de série temporal como AWS Timestream (recomendado) ou um banco relacional como AWS RDS.
Camada 3: Processamento e Análise (IA/ML)
Ambiente: AWS EC2 para hospedar scripts e o dashboard, e AWS Lambda para processamento em tempo real.
Modelo de IA:
Um modelo de classificação (Random Forest ou Regressão Logística) treinado com Scikit-learn em dados históricos para prever a necessidade de manutenção.
Lógicas de detecção de anomalia para identificar falhas súbitas.
Camada 4: Visualização e Alertas (Dashboard)
Dashboard: Aplicação interativa desenvolvida em Streamlit, hospedada no EC2.
Alertas: Envio de notificações automáticas (e-mail, SMS) via AWS SNS para a equipe de manutenção.
🚀 Roadmap / Fases do Projeto
Simulação e Geração de Dados:
[ ] Desenvolver o circuito no Wokwi com ESP32, microfone e potenciômetro.
[ ] Criar o script Python para gerar o dataset histórico (.csv) para treinamento do modelo.
Desenvolvimento do Modelo de IA:
[ ] Explorar os dados, treinar e avaliar modelos de classificação com Scikit-learn.
[ ] Salvar o melhor modelo treinado (modelo.pkl).
Configuração da Infraestrutura na Nuvem:
[ ] Configurar os serviços na AWS: IoT Core, Timestream/RDS, EC2 e SNS.
Integração e Dashboard:
[ ] Programar o firmware do ESP32 para enviar os dados para a AWS.
[ ] Desenvolver o dashboard em Streamlit para visualização e predição.
Testes End-to-End:
[ ] Validar o fluxo completo, desde a simulação do sensor até o alerta no dashboard.
🛠️ Tecnologias Utilizadas
Linguagens: Python, C++ (Arduino/ESP32)
Simulador: Wokwi + VS Code (PlatformIO)
Machine Learning: Scikit-learn, Pandas, NumPy
Computação em Nuvem: AWS (IoT Core, EC2, Lambda, Timestream, RDS, SNS)
Dashboard: Streamlit
