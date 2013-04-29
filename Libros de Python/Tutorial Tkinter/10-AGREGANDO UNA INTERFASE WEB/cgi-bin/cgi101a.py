#!/usr/bin/python
import cgi
form = cgi.FieldStorage( )                   # parse form data
print "Content-type: text/html\n"         # hdr plus blank line
print "<title>Reply Page</title>"         # html reply page
if not form.has_key('user'):
    print "<h1>Who are you?</h1>"
else:
    print "<h1>Hello <i>%s</i>!</h1>" % cgi.escape(form['user'].value)

