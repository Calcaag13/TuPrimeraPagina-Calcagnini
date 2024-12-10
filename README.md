## Funcionalidades

- Herencia de plantillas HTML.
- Cuatro modelos en `models.py`: Estudiantes, Cursos, Profesores, Entregables.
- Formularios para agregar datos a cada uno de los modelos.
- Búsqueda en la base de datos.

## Cómo Probar el Proyecto

1. Ingresar a alguno de los 4 menús para ingresar información ("Añadir Estudiante", "Añadir Curso", "Añadir Entregable", "Añadir Profesor")
2. Luego de ingresar los datos volverá a la página principal. Seleccionar la opción de "Buscar en la base de datos".
3. Ingresar alguno de los campos con los que haya completado la adición de alguna de las anteriores clases y presionar "Buscar"

## Estructura del Proyecto

- `models.py`: Definición de las clases del modelo.
- `formularios.py`: Definición de los formularios.
- `views.py`: Vistas para manejar las solicitudes HTTP.
- `urls.py`: Enrutamiento de URLs.
- `templates/`: Plantillas HTML para la interfaz de usuario.

