rem coverage by branches
coverage run --source=. --branch -m --skip-covered unittest discover
rem coverage by lines
rem coverage run --source=. --skip-covered -m unittest discover
coverage html
start "" .\htmlcov\index.html