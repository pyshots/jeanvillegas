# Proyecto Coderhouse
Comisión: 54135
Alumno: Jean Piero Villegas López

## Acerca del proyecto
FISI 11 es una web donde los estudiantes de la facultad de Ingenieria de Sistemas e Informática de la Universidad Nacional Mayor de San Marcos (Lima, Perú), encuentran ejercicios útiles para sus pc's y exámenes

## Uso
1. Descargue el proyecto de Github
2. Abra el proyecto en Visual Studio Code
3. En su terminal, ubíquese en project, ejecute python manage.py runserver para iniciar la web
4. En la web, el icono de la parte superior izquierda, lo lleva al inicio
5. Vaya a Ciclos, haga click en "Ciclo 3" o en el icono del circulo amarillo
6. Verá el ciclo con sus Cursos, sus Temas y sus Ejercicios/Soluciones 
7. Además tiene 3 botones que le permitirán subir sus ejercicios/soluciones y añadir temas nuevos
8. Cada botón lo llevará a un formulario que creará nuevos ejercicios/soluciones y temas
9. En los formularios, llene los campos y guarde
10. Lo redirigirán a la url de los ciclos

## Contiene
- project: contiene las apps
- README.md: las indicaciones de uso
- requirements.txt: librerias a instalar

## Aplicaciones
- Clase (contiene todos los modelos)
- config
- core (templates base)

## Modelos
1. Ciclo
2. Profesor
3. Curso
4. Tema
5. EjercicioCategoria
6. Solucion

## Mejoras futuras
Implementar los ciclos faltantes
Implementar buscadores
Implementar campos de imagen

## Problemas conocidos
La imagen de fondo de la web es única, requiere que cambie para cada url