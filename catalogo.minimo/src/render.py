from jinja2 import Template, Environment,FileSystemLoader
from pathlib import Path

import sys
sys.path.append('config')

from catalog import set_catalog

def main():
	import conf as xx
	# Pongo el reload porque para que vuelva a buscar el archivo conf si llamo a main varias veces, e.g. si lo modifico al conf.py con otra configuración en el medio
	import importlib
	importlib.reload(xx)

	import locale 
	locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
	from datetime import datetime
	today = datetime.now()
	css="<hr><p style='font-size: 80%;'><span style='float:left'>Última actualización: </span>"
	css="<hr><p style='font-size: 80%;'>"
	fecha = "<span style='float:left; '>"+today.strftime("%d de %B")+"</span>"
	hora = "<span style='float:right'>"+today.strftime("%H:%M")+"</span>"

	xx.fecha=css+fecha+hora+'</p>'

	[ordered_catalog,parents_dict]=set_catalog()

	# print(parents_dict)

	project_dir=Path(__file__).parent.parent; print(project_dir)
	template_dirs = project_dir / 'templates'

	j2_env = Environment(autoescape=True,
		trim_blocks=True,
		loader=FileSystemLoader(template_dirs)
		)



	j2_template = j2_env.get_template('/index.html')


	html=j2_template.render(
		catalog=ordered_catalog,
		parents=parents_dict,
		child="all",
		xx=xx)

	#project_dir/'output/index.html'
	print(xx.output_file)
	
	with open(xx.output_file, "w", encoding="utf-8-sig") as report:
		report.write(html)

def local_conf(conf_file):
	# from myfuncs import join
	import myfuncs as my
	conf_original=my.join('config/conf.py',conf_file)

	main()

	with open ('config/conf.py', 'w') as fp:
		fp.write(conf_original)	