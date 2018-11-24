#!C:/Python37/python.exe

import cgi
import algorithm

form = cgi.FieldStorage()
review = form.getvalue('review')
prediction = algorithm.test(review)

print("Content-type:text/html\r\n\r\n")
print("""
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
<h1>Your review was</h1>
<p>{}</p>
<p>Your review is: <b>{}</b></p>
</body>
</html>
""").format(review, prediction)
