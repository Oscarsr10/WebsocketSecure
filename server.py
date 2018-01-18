#!/usr/bin/env python
# Copyright (c) Twisted Matrix Laboratories.
# See LICENSE for details.

#Importacion de modulos y librerias

import sys

from twisted.internet import ssl, protocol, task, defer
from twisted.python import log
from twisted.python.modules import getModule
from twisted.internet.protocol import Protocol, Factory
from clases import *
from twisted.internet import reactor
from twisted.web.server import Site
from twisted.web.static import File
import json
import txaio
import os
from clases import *
from autobahn.twisted.websocket import WebSocketServerFactory, \
    WebSocketServerProtocol, \
    listenWS

#Creacion de la clase para que cuando se ejecute una funcion devuelva un mensaje
class EchoServerProtocol(WebSocketServerProtocol):

    def onMessage(self, payload, isBinary):
        self.sendMessage(payload, isBinary)
	print(payload)
	object = json.loads(payload.decode('utf8'))
	print(object)
	object=factory.Factory.CreateSamba()
	object.ejecutar()

'''
Aqui al recoger los .pem que son los certificados del CA y del servidor los carga y hace la conexion con el
websocket y utiliza el puerto 8080.
'''
def main(reactor):
    txaio.start_logging(level='debug')
    log.startLogging(sys.stdout)
    certData = getModule(__name__).filePath.sibling('rootCA.pem').getContent()
    authData = getModule(__name__).filePath.sibling('server.pem').getContent()

    authority = ssl.Certificate.loadPEM(certData)
    certificate = ssl.PrivateCertificate.loadPEM(authData)

    factory = protocol.Factory.forProtocol(EchoServerProtocol)

    factory = WebSocketServerFactory(u"wss://127.0.0.1:9000")
    
    factory.protocol = EchoServerProtocol
    listenWS(factory, certificate.options())
    
    webdir = File(".")
    webdir.contentTypes['.crt'] = 'application/x-x509-ca-cert'
    web = Site(webdir)
    reactor.listenSSL(8080, web, certificate.options(authority))
    return defer.Deferred()

#Aqui se dice que se ejecute el main
if __name__ == '__main__':
    task.react(main)
