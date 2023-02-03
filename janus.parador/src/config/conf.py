AUTHOR= 'JanusDEV'
BRANDNAME= 'Parador JANUS'
SITEURL= '.' #'https://januspri.github.io/parador'
SITESUBTITLE= "confort y simpleza" #"Proyecto Rural Integrador" # #Catálogo de productos"
SITENAME=  "Parador JANUS"

COPYRIGHT_NOTICE= '© 2023 JanusDEV' #+ AUTHOR

if 'WHATSAPPNUM' not in locals():
  WHATSAPPNUM= '542995711049'

if 'EMAIL' not in locals(): 
  EMAIL='jorgearagon@janus.bio'

print(EMAIL.split('@'))
def showEMAIL(email):
  return email.replace('@',' @ ')

if 'COSTODEENVIO' not in locals(): 
  COSTODEENVIO=0

ImagenMostrador= 'https://www.almacenjanus.bio/wp-content/uploads/2021/03/PARADOR-2019-FACE-DIA_DIA.jpg'


undesired_articles=['VISITA GUIADA y merienda','VISITA GUIADA y menú degustación']

#from jorge_conf import *

SHORTCEL=WHATSAPPNUM[2:5]+' '+WHATSAPPNUM[5:]

LINKS = (
  ('Ubicación: RN 151 ~ km 24,5 ~ Clte Cordero ~ Río Negro ~ ARG','https://g.page/JanusBio?share'),
  ('Janus Proyecto Rural Integrador', 'http://janus.bio/'),
  ('Almacén Janus', 'https://almacenjanus.bio'),
  ('WhatsApp: '+SHORTCEL,'https://wa.me/'+WHATSAPPNUM),
  ('e-mail: '+showEMAIL(EMAIL),'mailto: '+EMAIL)
  )

input_files=['../data/productos.csv']
if 'output_file' not in locals():
  output_file='../output/index.html'

#template_subdir:
subdir='alojamiento'
#Categorias
if 'parents' not in locals():
  parents={}
if 'only' not in parents:
  parents['only']=[]


parents['name']='Categorias'
parents['col_title']='categories'

parents['undesired']=['comidas']

parents['first']=['']
parents['last']=['comodidades']

parents['long_names']={}
#'visitas':'Visitas por el día','comodidades':'comodidades compartidas'}
parents['mensajes']={
'pernoctes':"""
<p style='font-weight:900;'>
PRECIOS POR NOCHE POR PERSONA
</p>
<p>
Habitaciones sin baño privado (vea nuestras comodidades). 
</p>
""",
'diurno':"Solo con reserva previa",
'visitas':
"""<p>
Coordine su visita con antelación: <a href='https://wa.me/'"""+WHATSAPPNUM+">"+SHORTCEL+"</a></p>"
}
# Nuestras habitaciones no tienen baño privado (vea nuestras comodidades). 
#y para la 1er noche.</p><p>Las siguientes noches -10% para toda la estadía.

#PEDIDOS
pedido=True

articles={}
articles['prefix']='un'
articles['word']='servicio' #alojamiento'
articles['pedido']='Reserva'

#MENSAJES
mensaje={}

mensaje['inicial']="""
<p>
Inspirados en la tradición viajera característica de las extensas rutas argentinas, 
queremos hacer un homenaje a la figura del clásico parador de ruta, 
ese oasis sin tiempo ni espacio en el que podemos encontrar reposo, sosiego, alimento y energía para continuar en el camino.
</p>
"""

mensaje['pedido']=""" 
<label for="fecha-inicio">Fecha:</label>

<input type="date" id="fecha-inicio" name="trip-start"
       value="2023-02-01"
       min="2023-02-01" max="2024-03-01" form="myform">

"""

mensaje['retiro']=""