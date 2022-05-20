from django.shortcuts import render
from django.http import HttpResponse
from appKeepCoding.models import Curso, Entregable

def curso(self):

      #curso = Curso(nombre = "Desarrollo web", camada = "19881")
      #curso.save()
      #documentoDeTexto = f"--->Curso:{curso.nombre}, Camada:{curso.camada}"
      return HttpResponse("Insert realizado")

from datetime import date

def entrega(self, nombreT):
      hoy = date.today()
      entrega = Entregable(nombre = nombreT, fechaDeEntrega = hoy, entregado = 1)
      entrega.save()  
      #entrega.eliminar(7)
      return HttpResponse(entrega)
      
def eliminar(self, idT):
      try:
            entrega = Entregable.objects.get(id=idT)
            entrega.delete()
            return HttpResponse(f'La tarea {entrega.nombre} eliminada correctamente')
      except: pass
      finally:return  HttpResponse(f'No se ha encontrado la tarea')
      

