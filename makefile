rmcache:
	find . -type d -name __pycache__ -exec rm -r {} \+

rmeggs:
	find . -type d -name *.egg-info -exec rm -r {} \+