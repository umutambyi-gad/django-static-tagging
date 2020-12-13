import re


# compile for href with double quotes ex. href=""
regex_for_href_with_double_quotes = re.compile(r'\b(href=")(\w.+?)\"\B')

# compile for src with double quotes ex. src=""
regex_for_src_with_double_quotes = re.compile(r'\b(src=")(\w.+?)\"\B')

# compile for href with single quotes ex. href=''
regex_for_href_with_single_quotes = re.compile(r"\b(href=')(\w.+?)\'\B")

# compile for src with single quotes ex. src=''
regex_for_src_with_single_quotes = re.compile(r"\b(src=')(\w.+?)\'\B")
