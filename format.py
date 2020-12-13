import re
from compiler import regex_for_href_with_double_quotes as d_href
from compiler import regex_for_src_with_double_quotes as d_src
from compiler import regex_for_href_with_single_quotes as s_href
from compiler import regex_for_src_with_single_quotes as s_src


htmlFile = 'index.html'
double = [] # double quoted matches ex. href=""
single = [] # single quoted matches ex. href=''


with open(htmlFile, 'r') as file:
	contents = file.read()

	# finding matches from double quoted 'href'
	for i in re.finditer(d_href, contents): 
		# avoid all matches to be and html files or from the other websites
		if not i.group(2).startswith('http') and not i.group(2).endswith('html'):
			double.append(i.group(2))

	# finding matches from double quoted 'src'
	for i in re.finditer(d_src, contents): 
		# avoid all matches to be and html files or from the other websites
		if not i.group(2).startswith('http') and not i.group(2).endswith('html'):
			double.append(i.group(2))

    # finding matches from single quoted 'src'
	for i in re.finditer(s_href, contents): 
		# avoid all matches to be and html files or from the other websites
		if not i.group(2).startswith('http') and not i.group(2).endswith('html'):
			single.append(i.group(2))

	# finding matches from single quoted 'href'
	for i in re.finditer(s_src, contents): 
		# avoid all matches to be and html files or from the other websites
		if not i.group(2).startswith('http') and not i.group(2).endswith('html'):
			single.append(i.group(2))


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


with open(htmlFile, 'w') as file:
	file.write(contents)
