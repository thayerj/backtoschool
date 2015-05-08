import cgitb
# Above is an import statement. It is used to bring in additional functionality
# that is not core part of Python.
cgitb.enable()
form = cgi.FieldStorage()
print("Content-type: text/html")
print("")

print("""<!DOCTYPE html>
    <html>
        <head>

        </head>
        <body>""")


print('<form action="/" method="post">')

print('</form>')

print("""</body>
     </html>""")