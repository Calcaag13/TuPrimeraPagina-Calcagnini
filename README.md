## Funcionalidades

- Herencia de plantillas HTML.
- Tres modelos en `models.py`: Autor, Categoria, Post.
- Formularios para agregar datos a cada uno de los modelos.
- Búsqueda en la base de datos.

## Cómo Probar el Proyecto

1. Clonar el repositorio.
2. Ejecutar `pip install -r requirements.txt` para instalar las dependencias.
3. Configurar la base de datos ejecutando `python manage.py migrate`.
4. Crear un superusuario con `python manage.py createsuperuser`.
5. Ejecutar el servidor con `python manage.py runserver`.
6. Navegar a `http://localhost:8000/` para ver la página principal.
7. Usar los enlaces `Añadir Autor`, `Añadir Categoria`, `Añadir Post` para agregar datos.
8. Usar la barra de búsqueda en la página principal para buscar posts.

## Estructura del Proyecto

- `models.py`: Definición de las clases del modelo.
- `formularios.py`: Definición de los formularios.
- `views.py`: Vistas para manejar las solicitudes HTTP.
- `urls.py`: Enrutamiento de URLs.
- `templates/`: Plantillas HTML para la interfaz de usuario.

