#Importacion de modulos y librerias
from __future__ import generators
import random
from abc import ABCMeta, abstractmethod
import os
from server import EchoServerProtocol

#Aqui lo que se hace es crear una clase que se encarga de crear factorias de una factoria.
class SambaFactory:
    objeto= {}
    def addFactory(type, factory):
        SambaFactory.objeto.put[type] = factory
    addFactory = staticmethod(addFactory)

    def createSamba(type):
        if not SambaFactory.objeto.has_key(type):
            SambaFactory.objeto[type] = \
            eval(type + '.Factory()')
        return SambaFactory.objeto[type].create()
    createSamba = staticmethod(createSamba)
    
class mensaje(object): pass

#Aqui defino los metodos para la factoria.
class user(mensaje):
    def ejecutar(self):
        os.system('useradd -g users -d /home/username -s /bin/bash -p $(echo '+self.object["usuario"]+' | openssl passwd -1 -stdin) '+self.object['password']+'')
        os.system('python2.7 /home/usuario/autobahn-python-master/examples/twisted/websocket/echo_tls/usuario.py '+self.object['usuario']+' '+self.object['password']+'')
    class Factory:
        def create(self): return user()
        
class folder(mensaje):
    def ejecutar(self):
        os.system('echo ['+self.object['name']+'] >> /usr/local/samba/lib/smb.conf')
        location='   path='+self.object['location']
        os.system('echo "'+location+'" >> /usr/local/samba/lib/smb.conf')
    class Factory:
        def create(self): return folder()  

class restart(mensaje):

    def ejecutar(self):
        os.system('/usr/local/samba/sbin/smbd restart')
    class Factory:
        def create(self): return restart() 
        
class start(mensaje):
    def ejecutar(self):
        os.system('/usr/local/samba/sbin/smbd start')
    class Factory:
        def create(self): return start()
        
class stop(mensaje):
    def ejecutar(self):
        os.system('/usr/local/samba/sbin/smbd stop')
    class Factory:
        def create(self): return stop()
