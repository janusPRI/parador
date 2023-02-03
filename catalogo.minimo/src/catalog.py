import conf as xx

from myfuncs import *

def set_catalog():
	catalog=[]
	for file in xx.input_files:
		catalog.extend(ReadCSV(file))

	# print(catalog)
	catalog.sort(key=lambda k: k[xx.parents['col_title']])

	# for row in catalog:
	# 	print(row)
	from itertools import groupby
	from operator import itemgetter
	import re 
	parents=[]
	titles=[]
	ordered_catalog=[]


	for categories,groups in groupby(catalog, key=itemgetter(xx.parents['col_title'])):
		# groups contiene todos los artículos de una dada categoría
		# Frescos>Hortalizas es distinto que Frescos>Hortalizas>Vinagre

		categories_list = re.split('[>|]{1}', categories) 

		# print("Categorias:")
		# print(categories)
		# print(categories_list)
		# Me quedo con el padre y descarto las subcategorias
		parent=categories_list[0].strip().lower()
		if parent=='':
			continue
		print(parent)
		parent=clean_parents([parent])[0]
		
		# Si existen categorías hijos y nietos las guardo
		child='';grandchild=''
		if len(categories_list)>1:
			if categories_list[0] != categories_list[1]:
				child=categories_list[1];
				if len(categories_list)>2:
					grandchild=categories_list[2];

		print(parent)

		print(xx.parents['undesired'])

		if xx.parents['only']:
			if parent not in xx.parents['only']:
				xx.parents['undesired']=parent
		
		if parent not in xx.parents['undesired']:
			parents.append(parent)
			parent_catalog=[]
			for article in groups:
				# print(article)
				article.update({'parent':parent})
				article.update({'child':child})
				article.update({'grandchild':grandchild})
				article = set_article(article)
				def valid_article(article,conf):
					if 'only' in conf.articles:
						if conf.articles['only']:
							if article['title'].lower() not in conf.articles['only']:
								article['status']='draft'
					if 'status' in article:
						# return article['status']=='publish' and ('outofstock' not in article['visibility']) and article['title'] not in conf.undesired_articles
						return article['status']=='publish'  and article['title'] not in conf.undesired_articles
					else:
						return True

				if valid_article(article,xx):
					titles.append(article['id'])
					parent_catalog.append(article);
					
			parent_catalog.sort(key=lambda k: k['title'])

			parent_catalog.sort(key=lambda k: k['order'])

			ordered_catalog.extend(parent_catalog);

	# for item in ordered_catalog:
	# 	print(item)

	# create_search_file(titles)
	parents_dict=create_parents_dict(clean_parents(parents))

	# for parent in parents_dict:
	# falta poner aca que article tenga un atributo 'bg-color', heredado de su padre

	# return [ordered_catalog,parents_dict|xx.parents]
	return [ordered_catalog,dict(list(parents_dict.items())+list(xx.parents.items()))]

#titles = [myarticle['title'] for myarticle in catalog]
#este incluye todos los títulos, incluso los que no estan


def create_parents_dict(unique_parents):

	parents_dictionary={
		"names":[],
		"bgcolors":[],
	}
	bgcolors=[
	# "rgba(255,0,0,1)","rgba(0,255,0,1)","rgba(0,0,255,1)","rgba(255,153,102,1)"
	#Fondos fuertes que se ven bien con letras blancas o negras
	#"Tomato","orange","dodgerBlue","MediumSeaGreen","rgba(248,228,113,1)","SlateBlue"
	#Fondos claros que se ven con letras negras
	"LightSalmon","DarkSeaGreen","LightSteelBlue","PaleGoldenRod","Tan","DarkKhaki","Thistle","Tomato","orange","dodgerBlue","MediumSeaGreen","rgba(248,228,113,1)","SlateBlue"]
	#NavajoWhite parecido al bisque
	#"Plum"

	if 'long_names' not in xx.parents:
		xx.parents['long_names']={}
	i=0;

	# print(xx.parents['long_names'])
	
	for parent_name in unique_parents:
		if parent_name.lower() not in xx.parents['long_names']:
			xx.parents['long_names'][parent_name]=parent_name;

		# parents_dictionary['long_names'][.append(parent_name);]
		parents_dictionary['names'].append(parent_name);
		parents_dictionary['bgcolors'].append(bgcolors[i]);
		i+=1;
	return parents_dictionary


def clean_parents(parents):
	unique_parents=list(set(parents))

	removal_list=['productos','alimentos']
	for removal_word in removal_list:
		unique_parents=[word.replace(removal_word,'') for word in unique_parents]
	clean_parents=[parent.lstrip().lower() for parent in unique_parents]

	clean_parents.sort()
	# print(clean_parents)
	for parent in clean_parents:
		if parent=='':
			clean_parents.pop(clean_parents.index(''))
			# print(type(clean_parents))

	#Pongo primero en la lista los que estan en parents['first']
	i=0

	if 'first' in xx.parents:
		for parent in xx.parents['first']:
			if parent.lower() in clean_parents:
				clean_parents.insert(i,clean_parents.pop(clean_parents.index(parent.lower())))
				i+=1
	if 'last' in xx.parents:
		for parent in xx.parents['last']:
			if parent.lower() in clean_parents:
				clean_parents.append(clean_parents.pop(clean_parents.index(parent.lower())))


	# print(clean_parents)

	return clean_parents
