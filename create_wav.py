import os
import pandas as pd
from TTS.api import TTS

# Carrega a planilha (ajuste o caminho se necessário)
df = pd.read_csv("data/frases_100_basicas.csv")

# Cria pasta de saída
os.makedirs("audios", exist_ok=True)

# Carrega modelo de francês
tts = TTS(model_name="tts_models/fr/css10/vits", progress_bar=False, gpu=False)

# Gera os arquivos de áudio
for index, row in df.iterrows():
    frase = row["Français"]
    file_name = f"audios/{index+1:02}.wav"
    tts.tts_to_file(text=frase, file_path=file_name)
    df.at[index, "Audio (URL ou caminho)"] = file_name

# Salva a nova planilha com os caminhos dos áudios
df.to_csv("frases_com_audio.csv", index=False)
print("Áudios gerados com sucesso!")
