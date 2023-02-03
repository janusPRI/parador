
import sys

from pathlib import Path
home = str(Path.home())
mysrc=home+'/projects/code/catalogo.minimo/src'
sys.path.append(mysrc)



import myfuncs as my


def main():
	import render
	render.main()

	# render.local_conf(mysrc+'/config/conf_jorge.py')


	# conf_original=my.join(home+'/projects/catalogo.simple/src/config/conf_jorge.py','config/conf.py')
	
	# render.main()

	# with open ('config/conf.py', 'w') as fp:
	# 	fp.write(conf_original)


if __name__ == "__main__":
	main()

