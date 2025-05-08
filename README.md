# QA-winter25

Описание проекта:
```
.
├── task1.py -  решение задания 1
├── task2 - папка с решением задания 2
│   ├── base_page.py - общая логика всех страниц
│   ├── example_page.py - методы тестируемой страницы
│   └── test_example_page.py - сами тесты 
├── requirements.txt - используемые библиотеки
└── README.md - инструкции по запуску
```

## Инструкция по запуску

1. Склонируйте к себе репозиторий 
```  
git clone https://github.com/lazyglitch/QA-may25.git
```  

2. Убедитесь, что на вашем компьютере установлен Python. В командной строке/терминале выполните команду  
```  
python -v # Windows
``` 
``` 
python3 -v # Linux/macOS  
```     
>Если он не установлен, то установите с официального [сайта Python](https://www.python.org/downloads/). В процессе установки обязательно поставьте галочку в чекбоксе "Add python.exe to PATH". 

3. Через командную строку/терминал перейдите в директорию проекта, выполнив команду  
```  
cd /здесь укажите путь до директории  
```
**При выполнении следующих команд рекомендуется использование активного виртуального окружения (venv)**
Окружение можно создать через терминал, например в [Visual Studio Code](https://code.visualstudio.com/)
```
python3 -m venv .venv # Linux/macOS
``` 
``` 
python -m venv .venv # Windows
```
Активируйте виртуальное окружение следующей командой
``` 
.venv/scripts/activate # Windows
```
```
.venv/bin/activate или source .venv/bin/activate # Linux/macOS
``` 

4. Установите необходимые зависимости из файла `requirements.txt`, выполнив команду    
```  
pip3 install -r requirements.txt  # Linux/macOS
```  
```  
pip install -r requirements.txt  # Windows 
```  

5. Запустите скрипт, выполнив команду    
```  
python  task1.py 
``` 
6. Запустите тест, выполнив команду    
```  
pytest -v 
``` 