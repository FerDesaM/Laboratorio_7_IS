#-*- coding: utf-8 -*-

from django.db import models

class Publicación(models.Model):
    class Meta:
        pass

    Titulo = None
    fecha = None
    autor = None
    contenido = None
    likes = None
    obtenerAutor = None
    obtenerFecha = None
    obtenerLikes = None
    agregarLike = None

