#Modulos y Paquetes

#from sys import path
#path.append('..∖∖packages∖∖extrapack.zip')

#Aqui se importa el modulo, debe señalar todas las carpetas:

#import extra.good.best.sigma as sig
#import extra.good.alpha as alp
#from extra.iota import funI
#from extra.good.beta import funB
#print(sig.funS())
#print(alp.funA())
#print(funI())
#print(funB())


#Repositorios

#Un repositorio (o repo para abreviar) diseñado para recopilar y
#compartir código Python gratuito lleva por nombre Python Package Index (PyPI)
#aunque también es probable que te encuentres con el nombre de The Cheese Shop
#(La Tienda de Queso).Su sitio web está disponible en https://pypi.org/.

#Para hacer uso de The Cheese Shop, se ha creado una herramienta especializada
#y su nombre es pip (pip instala paquetes mientras que pip significa ... ok,
#no importa). Como es posible que pip no se implemente como parte de la
#instalación estándar de Python, es posible que debas instalarlo manualmente.
#Pip es una herramienta de consola.


#Para verificar la versión de pip, se deben emitir los siguientes comandos:
#pip --version
#o
#pip3 --version
#Comprueba tu mismo cuál de estos funciona en el entorno de tu sistema operativo.
#La lista de las actividades principales de pip tiene el siguiente aspecto:
#pip help operación_o_comando – muestra una breve descripción de pip.
#pip list – muestra una lista de los paquetes instalados actualmente.
#pip show nombre_del_paquete – muestra información que incluyen las dependencias del paquete.
#pip search cadena – busca en los directorios de PyPI para encontrar paquetes cuyos nombres contengan cadena.
#pip install nombre – instala el paquete nombre en todo el sistema (espera problemas cuando no tengas privilegios de administrador).
#pip install --user nombre – instala nombre solo para ti; ningún otro usuario de la plataforma podrá utilizarlo.
#pip install -U nombre – actualiza un paquete previamente instalado.
#pip uninstall nombre – desinstala un paquete previamente instalado.