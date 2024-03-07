# Proyek Analisis Data 
Proyek analisis data polusi ini dilaksanakan guna memenuhi tugas proyek akhir Dicoding Bangkit 2024

# setup Environment
```bash
conda create --name main-ds python=3.9
conda activate main-ds
pip install numpy pandas scipy matplotlib seaborn Colab sreamlit npm localtunnel urllib
```

# Run streamlit app
## Pemanggilan key URL untuk streamlit
```bash
import urllib
print("Password/Enpoint IP for localtunnel is:",urllib.request.urlopen('https://ipv4.icanhazip.com').read().decode('utf8').strip("\n"))
```

## Run streamlit URL
```bash
streamlit run dasbord.py & npx localtunnel --port 8501
```

