import cgitb
# Above is an import statement. It is used to bring in additional functionality
# that is not core part of Python.
cgitb.enable()
form = cgi.FieldStorage()
print('Content-type: text/html')
print('')

print("""<!DOCTYPE html>
    <html>
        <head>
        <link rel="stylesheet" type="text/css" href="/css/main.css">
        </head>
        <body>""")

print('<img class=centered src=/img/lateral.png>')
print('<form action=/ method=post>')
print('</form>')

print("""</body>
     </html>""")