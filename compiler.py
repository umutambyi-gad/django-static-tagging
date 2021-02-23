import re


# compile for href with double quotes ex. href=""
regex_for_href_with_double_quotes = re.compile(r'\b(href=")(\.{0,}\/{0,}\s{0,}\w.+?)\"\B')

# compile for src with double quotes ex. src=""
regex_for_src_with_double_quotes = re.compile(r'\b(src=")(\.{0,}\/{0,}\s{0,}\w.+?)\"\B')

# compile for href with single quotes ex. href=''
regex_for_href_with_single_quotes = re.compile(r"\b(href=')(\.{0,}\/{0,}\s{0,}\w.+?)\'\B")

# compile for src with single quotes ex. src=''
regex_for_src_with_single_quotes = re.compile(r"\b(src=')(\.{0,}\/{0,}\s{0,}\w.+?)\'\B")

# compile for url which embedded in html style tag ex. style="url()"
regex_for_url = re.compile(r'\b(style=")(\.{0,}\/{0,}\s{0,}\w.+?)\"\B')