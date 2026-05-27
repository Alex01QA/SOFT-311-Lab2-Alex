----------------------------------------------------------------
WINDOWS
----------------------------------------------------------------

1- py -m venv .venv

2- .venv\Scripts\activate

3- .\.venv\Scripts\python -m pip install --upgrade pip

4- .\.venv\Scripts\pip install -e .

5- .\.venv\Scripts\python -m playwright install chromium

----------------------------------------------------------------

Comando para correrlo

.\.venv\Scripts\python tests/login_test.py


----------------------------------------------------------------
MAC
----------------------------------------------------------------

Comandos para crear el ambiente Windows

1- python3 -m venv .venv

2- source .venv/bin/activate

3- python -m pip install --upgrade pip

4- pip install -e .

5- python -m playwright install chromium
----------------------------------------------------------------

Comando para correrlo

.\.venv\Scripts\python tests/login_test.py