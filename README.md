# Experimentos_com_Python
Diversos experimentos, principalmente com API em Python e Flesk.

 - [DB Browser (SQLite)](https://sqlitebrowser.org/)
 - Instalar Flask → `pip install Flask`
 - Instalar JWT → `pip install PyJWT`
 - Gerar lista de dependências → `pip freeze > requirements.txt`
 - Obter localização das dependências → `python -m site --user-site`
 - Instalar todas as dependências → `pip install -r requirements.txt`

`Procfile`
```
web: gunicorn my_flask_app:app
```
Para "rodar" o aplicativo:
```python
•••
if __name__ == "__main__":
    app.run(debug=True)
```

Vídeos:

 - [Criar e publicar um Site com Flask](https://youtu.be/K2ejI4z8Mbg?si=E5gTWMDEVuHfnHfJ)
 - [Publicar no Railway ou Render](https://youtu.be/E9MMZ52InK8?si=zGTQGXnb31oOZWy2)
 - [Cursinho de GitHub Desktop](https://www.youtube.com/watch?v=EGmzAs1G0z0)
