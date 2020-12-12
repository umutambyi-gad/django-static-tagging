import re

regex_for_href_with_double_quotes = re.compile(r'\b(href=")(\w.+?)\"\B')
regex_for_src_with_double_quotes = re.compile(r'\b(src=")^http(\w.+?)\"\B')

regex_for_href_with_single_quotes = re.compile(r"\b(href=')(\w.+?)\'\B")
regex_for_src_with_single_quotes = re.compile(r"\b(src=')(\w.+?)\'\B")
