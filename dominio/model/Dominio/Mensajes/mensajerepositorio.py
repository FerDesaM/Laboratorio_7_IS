#-*- coding: utf-8 -*-

from django.db import models

class MensajeRepositorio(models.Model):
    class Meta:
        pass

    def EnviarMensaje(self, Mensaje mensaje):
        pass

    def EliminarMensaje(self, Mensaje mensaje):
        pass

