# Desafio Hermes Reply - Fase 4: Simulação e Análise de Dados

**Projeto:** Monitoramento Preditivo de Turbinas de Refrigeração<br>

---

### 1. Introdução

Este projeto tem foco na construção de um **sistema simulado de coleta e análise de dados para monitoramento industrial**. Utilizando Wokwi, VSCode e PlatformIO, desenvolvemos um circuito com um ESP32 para simular o monitoramento de uma turbina de refrigeração, coletando dados de vibração e ruído para identificar padrões e anomalias.

O fluxo de trabalho é inteiramente local: os dados são gerados na simulação, capturados via Monitor Serial e analisados com um script Python para gerar visualizações.

---

### 2. O Circuito de Simulação

Para simular o comportamento de uma turbina real, criamos um circuito virtual na plataforma Wokwi. Ele é composto pelo "cérebro" da operação (o ESP32) e por dois sensores virtuais (potenciômetros) que representam as variáveis físicas que queremos monitorar.

* **Componentes:**
    * **ESP32:** O microcontrolador responsável por ler os dados dos sensores, aplicar a lógica de decisão e enviar os resultados para o Monitor Serial.
    * **Potenciômetro 1 (Vibração):** Este componente simula um sensor de vibração, como um acelerômetro.
    * **Potenciômetro 2 (Ruído):** Simula um sensor de som ou microfone, capturando o nível de ruído operacional.

* **Conexões Elétricas:**
    * **Alimentação:** Ambos os potenciômetros são alimentados ligando seus pinos `VCC` ao pino `3V3` (3.3 Volts) do ESP32 e seus pinos `GND` ao pino `GND` (Terra) do ESP32. Isso garante que eles tenham a energia necessária para funcionar.
    * **Sinais:** O pino de sinal de cada sensor, que carrega a leitura analógica, é conectado a um pino **ADC (Analog-to-Digital Converter)** do ESP32.
        * O sinal do Potenciômetro de **Vibração** está ligado ao **GPIO 27**.
        * O sinal do Potenciômetro de **Ruído** está ligado ao **GPIO 26**.

A escolha de pinos ADC é crucial, pois permite ao ESP32 "ler" uma faixa de valores contínuos (de 0 a 4095), e não apenas "ligado" ou "desligado".

(monitor.png)

---

### 3. Lógica de Detecção de Status

O coração do nosso sistema de monitoramento é a lógica programada no ficheiro `main.ino`. Ela analisa os dados dos sensores e classifica o estado da turbina em uma de três categorias. A lógica baseia-se em limiares (`thresholds`) que definem o que é considerado um valor "alto" ou "baixo".

* **Valores de Limiar (Thresholds):**
    * `THRESHOLD_HIGH = 3000`: Qualquer leitura acima deste valor é considerada alta.
    * `THRESHOLD_LOW = 500`: Qualquer leitura abaixo deste valor é considerada baixa.

#### O Estado "NORMAL"

Este é o estado padrão. A turbina é considerada "NORMAL" se os valores de vibração e ruído estiverem dentro da faixa esperada, ou seja, **acima de 500 e abaixo de 3000**. Isso representa o funcionamento ideal do equipamento, sem sinais de estresse ou falha.

#### O Estado "ALERTA_SOBRECARGA"

A condição para este alerta é:
`se (Vibração > 3000 E Ruído > 3000)`

* **Significado no Mundo Real:** Este estado simula um cenário de estresse ou degradação. Uma vibração muito alta pode indicar um desbalanceamento das hélices, possivelmente causado por **acúmulo de gelo**. O ruído alto e simultâneo representa o motor a trabalhar com mais força para compensar o problema. É um sinal claro de que a manutenção é necessária para evitar uma quebra.

#### O Estado "ALERTA_FALHA_SUBITA"

A condição para este alerta é:
`se (Vibração < 500 E Ruído < 500)`

* **Significado no Mundo Real:** Este estado simula uma paralisação completa e inesperada da turbina. A vibração e o ruído caem para perto de zero simultaneamente. Isso pode ser causado por uma **falha elétrica súbita**, um corte de energia ou um bloqueio mecânico total que impede o motor de girar. É o cenário mais crítico, pois a produção é interrompida sem aviso.

---

### 4. Coleta e Registro de Dados

O código `main.ino` lê os valores dos sensores a cada 2 segundos. Após aplicar a lógica descrita acima, ele imprime os dados no Monitor Serial em formato **CSV**, prontos para serem copiados para análise.

---

### 5. Análise de Dados e Gráficos

Os dados coletados foram salvos num ficheiro `dados_coletados.csv` e analisados com um script Python (`analise_dados.py`).

#### 5.1 Gráfico de Linha: Histórico dos Sensores

Este gráfico mostra a evolução das leituras ao longo do tempo, sendo ideal para identificar tendências.

**[grafico_linha.png]**

#### 5.2 Gráfico de Dispersão: Correlação Vibração vs. Ruído

Este gráfico é fundamental para entender a relação entre as duas variáveis. Cada ponto representa uma leitura, e a sua cor indica o status da turbina, permitindo identificar visualmente os "clusters" (agrupamentos) de cada estado operacional.

**[grafico_dispersao.png]**

Esta análise inicial confirma que o sistema de coleta é funcional e que os dados gerados são relevantes e suficientes para treinar um futuro modelo de machine learning para classificar o estado da turbina automaticamente.
