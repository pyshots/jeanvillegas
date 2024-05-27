# Proyecto Coderhouse
- Comisión: 54135
- Alumno: Jean Piero Villegas López
- Video 1: https://drive.google.com/file/d/1O9McLcz41YvCrOJxCWaqxPIJ70LIrP7I/view?usp=sharing
- Video 1.1: https://drive.google.com/file/d/1dEwpZJ9dZtJYtjbbvvvHOQQatB-w8Zfl/view?usp=sharing

## Acerca del proyecto
FISI 11 es una web donde los estudiantes de la facultad de Ingenieria de Sistemas e Informática de la Universidad Nacional Mayor de San Marcos (Lima, Perú) encuentran ejercicios útiles para sus pc's y exámenes

![fisi22web](https://github.com/pyshots/jeanvillegas/assets/156743660/c47d3b07-e329-4103-a331-59b44a59f3ef)


## Uso
1. Descargue el proyecto de Github
2. Abra el proyecto en Visual Studio Code y active su entorno virtual
3. En su terminal, ubíquese en project, ejecute python manage.py runserver para iniciar la web
4. En la web, le pedirá hacer login, puede registrarse para ello, y también hacer logout si desea
5. Lo dirigirá al home, puede clickear en Ciclos y Ciclo 3
6. Verá el ciclo con las opciones de subir y listar sus ejercicios y soluciones
7. Cada botón lo llevará a un formulario que creará y listará los ejercicios y soluciones
9. Dentro de listar, podrá buscar y ver en detalle los ejercicios y soluciones, así como cambiar y borrar estos.
10. Puede explorar el apartado About en el Navbar para leer brevemente sobre el autor

## Contiene
- project: contiene las apps Clase, core y config
- README.md: las indicaciones de uso
- requirements.txt: librerias a instalar

## Aplicaciones
- Clase (modelos EjercicioCategoria y Solucion, CRUD)
- config
- core (templates base, index, login y about )

## Modelos
1. EjercicioCategoria
2. Solucion
3. Otros

## Mejoras futuras
- Alimentar la BD
- Adecuar el front end de los html

## Problemas conocidos
La imagen de fondo de la web es única, requiere que cambie para cada url
