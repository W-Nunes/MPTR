#include <Arduino.h>

// --- Configuração dos Pinos ---
// Pinos confirmados de acordo com o seu último 'diagram.json'.
const int VIBRATION_PIN = 27; // Potenciômetro 1 (Vibração) conectado ao pino 27
const int SOUND_PIN = 26;     // Potenciômetro 2 (Ruído) conectado ao pino 18

// --- Limiares para Lógica de Decisão ---
// Valores experimentais. Ajuste-os durante a simulação!
const int VIBRATION_THRESHOLD_HIGH = 3000; // Limiar alto de vibração
const int SOUND_THRESHOLD_HIGH = 3000;     // Limiar alto de ruído
const int VIBRATION_THRESHOLD_LOW = 500;   // Limiar baixo de vibração
const int SOUND_THRESHOLD_LOW = 500;       // Limiar baixo de ruído

void setup() {
  // Inicializa a comunicação serial com o computador a 115200 bauds
  Serial.begin(115200);
  
  // Imprime o cabeçalho para o formato CSV.
  Serial.println("Timestamp,Vibracao,Ruido,Status");
}

void loop() {
  // --- Leitura dos Sensores ---
  int vibrationValue = analogRead(VIBRATION_PIN);
  int soundValue = analogRead(SOUND_PIN);

  // Variável para armazenar o status da turbina
  String status = "NORMAL";

  // --- Lógica de Análise e "Predição" ---
  // Verifica se ambos os sensores estão com leitura muito alta (risco de gelo/sobrecarga)
  if (vibrationValue > VIBRATION_THRESHOLD_HIGH && soundValue > SOUND_THRESHOLD_HIGH) {
    status = "ALERTA_SOBRECARGA";
  } 
  // Verifica se ambos os sensores estão com leitura muito baixa (risco de falha súbita)
  else if (vibrationValue < VIBRATION_THRESHOLD_LOW && soundValue < VIBRATION_THRESHOLD_LOW) {
    status = "ALERTA_FALHA_SUBITA";
  }

  // --- Saída dos Dados via Monitor Serial ---
  Serial.print(millis());
  Serial.print(",");
  Serial.print(vibrationValue);
  Serial.print(",");
  Serial.print(soundValue);
  Serial.print(",");
  Serial.println(status);

  // Aguarda 2 segundos antes da próxima leitura
  delay(2000);
}
