### 

La carpeta data/ contiene stocks extraidas de Yahoo Finance.

Data desde 2020-06-12 al 2021-06-12.

Supuesto: Si la fecha no existe, buscará la fecha de inicio siguiente más cercana, y en caso de la fecha de término, la anterior más cercana con precio existente.

## Iniciar

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

```
python3 main.py
```