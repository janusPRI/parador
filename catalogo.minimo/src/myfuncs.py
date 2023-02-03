import csv
def ReadCSV(fname):
	with open(fname, newline='',encoding='utf-8-sig') as csvfile:
		data = csv.DictReader(filter(lambda row: row[0]!='#', csvfile))
		# data = csv.DictReader(csvfile)
		listdata=list(data)
		# for row in data:
		# 	print(row)
#        print(', '.join(row))
#    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
	return listdata


# creo article.size a partir de articulo.excerpt.
# si tiene las palabras contenido o peso, lo borro o lo remplazo por lo que haya entre parentesis
#
import html
import re 
def set_article(article):	
	# article['description']=article['excerpt']
	msj='Todavía no contamos con una descripción detallada del artículo'
	if 'description' not in article:
		article['description']=msj;
	else:
		if article['description']=='':
			article['description']=msj;
			
	article["excerpt"]=html.unescape(article["excerpt"])
	longString=article['excerpt']
	removal_list=['Contenido','Peso']



	# if removal_list in longString:
	if next((True for word in removal_list if word in longString),False):		
		if '(' and ')' in longString:
			# https://stackoverflow.com/questions/38999344/extract-string-within-parentheses-python
			text_inside_paranthesis = re.findall('\(([^)]+)',longString)[0]
			removal_list.append('('+text_inside_paranthesis+')')
			#text_inside_paranthesis = re.findall('\(.*?\)',longString)[0]
			#removal_list.append(text_inside_paranthesis)
			article['excerpt']=text_inside_paranthesis;
		else:
			article['excerpt']=""
		# edit_string_as_list = longString.split()
		# print(removal_list)
		# final_list = [word for word in edit_string_as_list if word not in removal_list]
		# article["size"] = ' '.join(final_list)
		# print(final_list)
		for string in removal_list:
			# print(string)
			longString=longString.replace(string,'')
		longString=longString.replace('kilogramos','kg')
		longString=longString.replace('kilogramo','kg')
		longString=longString.replace('gramos','gr')
		# edit_string_as_list = longString.split('. ')
		edit_string_as_list = re.split('\. |\n',longString)
		longString=edit_string_as_list[0];
		# print(longString)

		if "size" not in article:
			article["size"] = longString.replace(':',"")
		if(len(edit_string_as_list)>1):
			edit_string_as_list.pop(0);
			for string in edit_string_as_list:
				if string =='':
					edit_string_as_list.remove(string)
			# if article['title']=='Grasa Bovina':
			# 	print(edit_string_as_list)	
			article['excerpt']=". ".join(edit_string_as_list);
	else:
		if 'Teléfono' in article:
			article["size"]	= article['Teléfono']
		else:
			if 'size' in article:
				if article['size'].isdigit():
					article['size']=str(article['size'])+' semillas'
			else:
				article["size"]=""
	#guardo el titulo en el id que es único
	article['id']=article['title'];

	#al título le saco los paréntesis que tenga
	if '(' and ')' in article["title"]:
		# text_inside_paranthesis = re.findall('\(.*?\)',article["title"])[0]
		text_inside_paranthesis = re.findall('\(([^)]+)',article["title"])[0]
		article["title"]=(article["title"].replace('('+text_inside_paranthesis+')','')).rstrip()
		if(text_inside_paranthesis.lower() not in article['excerpt'].lower()):
			article["excerpt"]=text_inside_paranthesis+ ' ' + article["excerpt"]

	Enpadronar(article)

	return article

def Enpadronar(article):
	exception_list=['cola de caballo','diente de león', 'rosa mosqueta','tierra negra','cocina natural amar']
	if article['parent'].lower()in exception_list or article['title'].lower() in exception_list:
		article['Nombre']=article['title'].upper()
		article['Apellido']=''
		return
	if 'Nombre' in article:
		if 'Apellido'  in article:
			return
		else:
			article['Apellido']=''
			return
	if 'Apellido' in article:
		article['Nombre']=''
		return
	if article['title']=='':
		return

	article['Nombre']=''
	lista=article['title'].split()

	def set_name(article,lista):
	# la primer palabra siempre esta dentro del nombre
		article['Nombre']+=' '+lista[0].upper()
		if len(lista)==1:
			article['Apellido']=''
			return 1
		lista.pop(0);
		return 0

	if set_name(article,lista):
		return

	preposiciones=['de','con','en']
	if lista[0] in preposiciones:
# si la 2da palabra es 'de', 'con', ... entonces empieza el apellido
		article['Apellido']=' '.join(lista)
		return
	if len(lista)>1 and lista[1] in preposiciones:
		if set_name(article,lista):
			return
	while len(lista)>0 and lista[0].isupper():
# si la 2da palabra está en mayúscula entonces también pertenece al nombre
		article['Nombre'] += ' ' + lista[0]
		lista.pop(0);

	article['Apellido']=' '.join(lista)
	return

# import sys
# def join(f1,f2,fout):
def join(f2,f1=''):
	# if len(sys.argv) > 2:
	if f1:
		with open(f1) as fp:
			ff1 = fp.read()
	else :
		ff1= ''
	with open(f2) as fp:
		ff2 = fp.read()

	# with open (fout, 'w') as fp:
	with open (f2, 'w') as fp:
		fp.write(ff1+"\n"+ff2)

	return ff2
