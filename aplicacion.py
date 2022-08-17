from joblib import load
import numpy as np

def ingresarIMC():
  IMC = None
  while IMC == None or IMC <= 0:
    try:
      IMC = float(input(f'Ingrese el IMC: '))
      if IMC <= 0:
        print('Error, ingrese un IMC positivo!')
    except Exception:
      print('Error, ingrese un IMC correcto!')

  return IMC

def ingresarTabaquismo():
  respuesta = None
  while respuesta != 'si' and respuesta != 'no':
    respuesta = input('¿Ha fumado al menos 100 cigarrillos en toda su vida? si/no: ').lower()

  if respuesta == 'si':
    return 1
  return 0

def ingresarAlcoholismo():
  respuesta = None
  while respuesta != 'si' and respuesta != 'no':
    respuesta = input('¿Ha tomado más de 14 tragos de alcohol(hombres) o más de 7(mujeres) en una semana? si/no: ').lower()

  if respuesta == 'si':
    return 1
  return 0

def ingresarDerrame():
  respuesta = None
  while respuesta != 'si' and respuesta != 'no':
    respuesta = input('¿Ha tenido un derrame cerebral? si/no: ').lower()

  if respuesta == 'si':
    return 1
  return 0

def ingresarSaludFisica():
  respuesta = -1
  while respuesta < 0 or respuesta > 30:
    try:
      print('¿Durante los últimos 30 días su salud física no fue buena?')
      respuesta = int(input('Responda en un rango de 0 a 30: '))
    except:
      respuesta = -1
  return respuesta

def ingresarSaludMental():
  respuesta = -1
  while respuesta < 0 or respuesta > 30:
    try:
      print('¿Durante los últimos 30 días su salud mental no fue buena?')
      respuesta = int(input('Responda en un rango de 0 a 30: '))
    except:
      respuesta = -1

  return respuesta

def ingresarDificultadParaCaminar():
  respuesta = None
  while respuesta != 'si' and respuesta != 'no':
    respuesta = input('¿Tiene dificutad para caminar o subir escaleras? si/no: ').lower()

  if respuesta == 'si':
    return 1
  return 0

def ingresarSexo():
  opcion = -1
  while opcion != 1 and opcion != 0:
    try:
      opcion = int(input('[1] Masculino\n[0] Femenino\nOpcion: '))
    except:
      opcion = -1

  return opcion

def ingresarCategoriaEdad():
  categorias = ['18-24','25-29','30-34','35-39','40-44','45-49','50-54','55-59','60-64','65-69','70-74','75-79','80 o mayor']
  opcion = -1
  while opcion < 0 or opcion >= len(categorias):
    try:
      print('Escoja el rango de edad')
      for i in range(len(categorias)):
        print(f'[{i}] {categorias[i]}')
      opcion = int(input('Opcion: '))
    except:
      opcion = -1

  return opcion

def ingresarRaza():
  razas = ['Blanco','Negro','Asiático','Indio americano / nativo de Alaska','Otro','Hispano']
  opcion = -1
  while opcion < 0 or opcion >= len(razas):
    try:
      print('Escoja la raza')
      for i in range(len(razas)):
        print(f'[{i}] {razas[i]}')
      opcion = int(input('Opcion: '))
    except:
      opcion = -1

  return opcion

def ingresarDiabetico():
  respuesta = None
  while respuesta != 'si' and respuesta != 'no':
    respuesta = input('¿Es diabético? si/no: ').lower()

  if respuesta == 'si':
    return 1
  return 0

def ingresarActividadFisica():
  respuesta = None
  while respuesta != 'si' and respuesta != 'no':
    respuesta = input('¿Realiza actividad física? si/no: ').lower()

  if respuesta == 'si':
    return 1
  return 0

def ingresarSaludGeneral():
  salud = ['Mala','Justa','Buena','Muy Buena','Excelente']
  opcion = -1
  while opcion < 0 or opcion >= len(salud):
    try:
      print('Salud general')
      for i in range(len(salud)):
        print(f'[{i}] {salud[i]}')
      opcion = int(input('Opcion: '))
    except:
      opcion = -1

  return opcion

def ingresarHorasSuenio():
  respuesta = 0
  while respuesta < 3 or respuesta > 20:
    try:
      respuesta = int(input('Ingrese las horas de sueño: '))
    except:
      respuesta = 0
  
  return respuesta

def ingresarAsma():
  respuesta = None
  while respuesta != 'si' and respuesta != 'no':
    respuesta = input('¿Tiene asma? si/no: ').lower()

  if respuesta == 'si':
    return 1
  return 0

def ingresarEnfermedadRinion():
  respuesta = None
  while respuesta != 'si' and respuesta != 'no':
    respuesta = input('¿Sufre de alguna enfermedad en el riñon? si/no: ').lower()

  if respuesta == 'si':
    return 1
  return 0

def ingresarCancer():
  respuesta = None
  while respuesta != 'si' and respuesta != 'no':
    respuesta = input('¿Tiene cancer? si/no: ').lower()

  if respuesta == 'si':
    return 1
  return 0

modelo = load('modelo.joblib')
respuesta = 'si'

while respuesta != 'no':
  variables = np.zeros((1,17))

  variables[0,0] =  ingresarIMC()
  variables[0,1] = ingresarTabaquismo()
  variables[0,2] = ingresarAlcoholismo()
  variables[0,3] = ingresarDerrame()
  variables[0,4] = ingresarSaludFisica()
  variables[0,5] = ingresarSaludMental()
  variables[0,6] = ingresarDificultadParaCaminar()
  variables[0,7] = ingresarSexo()
  variables[0,8] = ingresarCategoriaEdad()
  variables[0,9] = ingresarRaza()
  variables[0,10] = ingresarDiabetico()
  variables[0,11] = ingresarActividadFisica()
  variables[0,12] = ingresarSaludGeneral()
  variables[0,13] = ingresarHorasSuenio()
  variables[0,14] = ingresarAsma()
  variables[0,15] = ingresarEnfermedadRinion()
  variables[0,16] = ingresarCancer()
  
  probabilidad = modelo.predict_proba(variables)
  porcentaje = round(probabilidad[0][1]*100, 2)
  print(f'\nLa probabilidad que tanga una enfermedad cardíaca es del {porcentaje}%')

  respuesta = input('Desea volver a llenar el formulario? si/no: ').lower()

