# Django Tutorial

Repositório de teste para praticar a criação de projetos de backend  utilizando
**Django**.

## Part 1

Instalar django no projecto utilizando `pip`:

```sh
pip install django
```

Isso irá instalar o commando `django-admin`. Além de várias opções, ele permite criar projetos django com o comando:

```sh
django-admin startproject my_project
```

O projecto criado conta com a seguinte estrutura:

```sh
my_project/
    manage.py
    my_project/
        __init__.py
        settings.py
        urls.py
        wsgi.py
```

Algumas explicações:

- A raiz `my_project` é so o container do projeto, pode ser renomeada.
- o arquivo `manage.py` é um utilitário para interagir com o projeto.
- `my_project/settings.py` salva as configurações do projeto.
- `my_project/urls.py` estrutura os endpoints, como se fosse um "Table of Contents"
- `mysite/wsgi.py` é o entrypoint para utilizar web servers (Apache, nginx) para ser vir a aplicação

### Rodando o projeto

Django já provê um web server integrado apra fins de desenvolviemnto. Para rodar basta acessar a pasta raiz dele e utilizar o comando:

```sh
python manage.py runserver [ip][port]
```

Por padrão ele executa na porta `8000`.

Agora podemos acessar o projeto tranquilamente pelo endereço impresso no terminal.

Com o ambiente do projeto está todo preparado, podemos começar a trabalhar com nossos **apps**.

> #### Projetos vs Apps
> Django introduz conceitos bem definidos sobre **projeto** e **app**. O projeto é o ambiente, o app é a aplicação rodando dentro do ambiente. Assim sendo, podemos ter vários apps num mesmo projeto django.


### Criando um app

Para inicar um app chamado `webserver` rodamos o comando:

```sh
python manage.py startapp webserver
```
Será criado uma pasta `webserver` com a seguinte estrutura:

```sh
webserver/
    __init__.py
    admin.py
    apps.py
    migrations/
        __init__.py
    models.py
    tests.py
    views.py
```

#### View

Criamos uma view muito simples em `webserver/views.py`:

```python
from django.http import HttpResponse

# Create your views here.
def index(req):
    return HttpResponse("<b>Hello World. You're the webserver index</b>")
```

Agora precisamos fazer o map da view para um endpoint em `webserver/urls.py`:

```python
from django.urls import path

from . import views

urlpatters = [
    path('', views.index, name="index"),
]
```

Também é necessário adicionar essa nova url para o `my_project/urls.py` do projeto:

```diff
 from django.contrib import admin
-from django.urls import path
+from django.urls import path, include

 urlpatterns = [
     path('admin/', admin.site.urls),
+    path('webserver/', include('webserver.urls')),
 ]
```

A documentação recomenda sempre usar `include`, exceto no `admin.site.urls`.
