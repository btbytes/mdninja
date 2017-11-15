=======
mdninja
=======

**mdninja + markdown + jinja2 = beautiful HTML documents**

`mdninja` is a document processor that converts markdown documents into HTML document by applying Jinja2 templating.

Installation
------------

::

  pip install mdninja

Usage
-----

Simple use:

::

  mdninja doc.md -o doc.html


If you want to use a different template:

::

  mdninja doc.md -o doc.html --template=stylish.html


The default template is:

::

	<!DOCTYPE html>
	<html>
		<head>
			<title>{% for title in meta.title %}{{title}} {% endfor %}</title>
		</head>
		<body>
			<h1>{% for title in meta.title %}{{title}} {% endfor %}</h1>
			{{ body }}
			<hr/>
		</body>
	</html>

Metadata (like `title` above) is added to the document by adding metadata headers like this at the top of the file

::

  Title: A simple document


Alternatively, you can specify the meatadata using a YAML style header too:

::

	---
	title: A simple document
	---
