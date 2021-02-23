import re
from compiler import regex_for_href_with_double_quotes as d_href
from compiler import regex_for_src_with_double_quotes as d_src
from compiler import regex_for_href_with_single_quotes as s_href
from compiler import regex_for_src_with_single_quotes as s_src
from compiler import regex_for_url

with open('fileToFormat.txt', 'r', encoding="utf8") as file:
	htmlFiles = file.read().strip().split('\n')

def formating(htmlFile):
	double = [] # double quoted matches ex. href=""
	single = [] # single quoted matches ex. href=''
	contents = "{% load static %}\n"

	with open(htmlFile, 'r', encoding="utf8") as file:
		contents += file.read()

		# finding matches from double quoted 'href'
		for i in re.finditer(d_href, contents): 
			# avoid all matches to be and html files or from the other websites
			if not i.group(2).startswith('http') and not i.group(2).endswith('html'):
				double.append(i.group(2).strip())

		# finding matches from double quoted 'src'
		for i in re.finditer(d_src, contents): 
			# avoid all matches to be and html files or from the other websites
			if not i.group(2).startswith('http') and not i.group(2).endswith('html'):
				double.append(i.group(2).strip())

	    # finding matches from single quoted 'src'
		for i in re.finditer(s_href, contents): 
			# avoid all matches to be and html files or from the other websites
			if not i.group(2).startswith('http') and not i.group(2).endswith('html'):
				single.append(i.group(2).strip())

		# finding matches from single quoted 'href'
		for i in re.finditer(s_src, contents): 
			# avoid all matches to be and html files or from the other websites
			if not i.group(2).startswith('http') and not i.group(2).endswith('html'):
				single.append(i.group(2).strip())


		# finding all style:...url() and format it if it's needed
		for x in re.finditer(regex_for_url, contents):
			pick_url  = re.compile(r'\b(:\s*?url\()(.*)\)\B')
			for y in re.finditer(pick_url, x.group(2)):
				if y.group(2).startswith("'"):
					if not y.group(2)[1:-1].startswith('http'):
						# just to check if staticfile is not in the list to avoid duplicate
						if y.group(2)[1:-1] not in (single, double):
							contents = re.sub(y.group(2), "{% static " + y.group(2) + " %}", contents)
				else:
					if not y.group(2)[1:-1].startswith('http'):
						double.append(y.group(2).strip())


		# replacing the all double quoted matches
		# [*{* double }] to avoid duplicates
		double = [*{*double}]
		for i in range(len(double)):
			contents = re.sub(double[i], r"{% static '" + double[i] + r"' %}", contents)


		# replacing the all single quoted matches
		# [*{* single }] to avoid duplicates
		single = [*{*single}]
		for i in range(len(single)):
			contents = re.sub(single[i], r'{% static "' + single + r'" %}', contents)


	with open(htmlFile, 'w', encoding="utf8") as file:
		file.write(contents)


for htmlFile in htmlFiles:
	formating(htmlFile)