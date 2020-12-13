import re
from compiler import regex_for_href_with_double_quotes as d_hr
from compiler import regex_for_src_with_double_quotes as d_sr
from compiler import regex_for_href_with_single_quotes as s_hr
from compiler import regex_for_src_with_single_quotes as s_sr

htmlFile = 'index.html'
double_quoted_matches = []
single_quoted_matches = []


with open(htmlFile, 'r') as file:
	contents = file.read()
	for i in re.finditer(d_hr, contents): 
		if not i.group(2).startswith('http') and not i.group(2).endswith('html'):
			double_quoted_matches.append(i.group(2))

	for i in re.finditer(d_sr, contents): 
		if not i.group(2).startswith('http') and not i.group(2).endswith('html'):
			double_quoted_matches.append(i.group(2))

	for i in re.finditer(s_hr, contents): 
		if not i.group(2).startswith('http') and not i.group(2).endswith('html'):
			single_quoted_matches.append(i.group(2))

	for i in re.finditer(s_sr, contents): 
		if not i.group(2).startswith('http') and not i.group(2).endswith('html'):
			single_quoted_matches.append(i.group(2))


	for i in range(len(double_quoted_matches)):
		contents = re.sub(double_quoted_matches[i], r"{% static '" + double_quoted_matches[i] + r"' %}", contents)

	for i in range(len(single_quoted_matches)):
		contents = re.sub(single_quoted_matches[i], r"{% static '" + single_quoted_matches[i] + r"' %}", contents)

with open(htmlFile, 'w') as file:
	file.write(contents)
