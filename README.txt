----------------------------------------------------------------
WINDOWS
----------------------------------------------------------------

1- py -m venv .venv

2- .venv\Scripts\activate

3- .\.venv\Scripts\python -m pip install --upgrade pip

4- .\.venv\Scripts\pip install -e .

5- .\.venv\Scripts\python -m playwright install chromium

----------------------------------------------------------------

Comando para correr todos los test
.\.venv/bin/python -m pytest --html=report.html --self-contained-html

Comando para correr un test especifico (ejm login_test)
.\.venv/bin/python -m pytest tests/login_test.py --html=report.html --self-contained-html


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

Comando para correr todos los test
pytest --html=report.html --self-contained-html

Comando para correr un test especifico (ejm login_test)
pytest tests/login_test.py --html=report.html --self-contained-html