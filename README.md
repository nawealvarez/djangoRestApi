# django_apiRest

Importar json con: 
~~~~
	./manage.py loaddata titulares
~~~~

####Probando endpoints:
	
Obtener todos los titulares:
~~~~
	curl -H 'Accept: application/json; indent=4' -u admin:admin -X GET http://localhost:8000/titulares/
~~~~

Obtener todos las personas fisicas:
~~~~
	curl -H 'Accept: application/json; indent=4' -u admin:admin -X GET http://localhost:8000/fisicas/
~~~~

Obtener la persona fisica con id = 1:
~~~~
	curl -H 'Accept: application/json; indent=4' -u admin:admin -X GET http://localhost:8000/fisicas/1/
~~~~

Agregar una persona fisica:
~~~~
    curl -H 'Accept: application/json; indent=4' -u admin:admin -X POST -d "cuit=20931&&name=Jose&&lastname=Perez&dni=20" http://localhost:8000/fisicas/
~~~~

Editar el nombre de la persona fisica recientemente añadida:
~~~~
    curl -H 'Accept: application/json; indent=4' -u admin:admin -X PATCH http://localhost:8000/fisicas/5/ -d "name=Jose Luis"
~~~~

Eliminar la persona fisica recien añadida:
~~~~
    curl -H 'Accept: application/json; indent=4' -u admin:admin -X DELETE http://localhost:8000/fisicas/5/
~~~~

Obtener todos las personas juridicas:
~~~~
	curl -H 'Accept: application/json; indent=4' -u admin:admin -X GET http://localhost:8000/juridicas/
~~~~

Obtener la persona juridica con id = 2:
~~~~
	curl -H 'Accept: application/json; indent=4' -u admin:admin -X GET http://localhost:8000/juridicas/2/
~~~~

Agregar una persona juridica:
~~~~
    curl -H 'Accept: application/json; indent=4' -u admin:admin -X POST -d "cuit=20931&&razonSoc=Nike Store&&year=2017" http://localhost:8000/juridicas/
~~~~

Editar el nombre de la persona juridica recientemente añadida:
~~~~
    curl -H 'Accept: application/json; indent=4' -u admin:admin -XPATCH http://localhost:8000/juridicas/6/ -d "razonSoc=Nike"
~~~~

Eliminar la persona juridica recien añadida:
~~~~
    curl -H 'Accept: application/json; indent=4' -u admin:admin -X DELETE http://localhost:8000/juridicas/6/
~~~~


