"# TaskPython" 

> Uma aplicação simples para controle de tarefas

Antes de iniciar o build, você precisa ter npm e python instalados em sua máquina.

## Build Setup

#BackEnd

``` bash
#Criar um ambiente virtual
#Dentro da pasta .\app\BackEnd\
python -m venv virtual
virtual\Scripts\activate.bat

#Configure ambiente virtual
pip install django
pip intall djangorestframework
pip install django-cors-headers

#Agora acesse pasta do sistema e rode o serviço de BackEnd
cd taskAPP
python manage.py migrate
python manage.py runserver
```

#FrontEnd

``` bash

#Dentro da pasta .\app\FrontEnd\task

# installe dependencias
npm install

# rode serviço front end
npm run dev
```

Agora você pode acessar o sistema no link
http://localhost:8080

Qualquer duvida pode entrar em contato no e-mail: paulo.es@live.com