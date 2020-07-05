#!/usr/bin/python
# Simple Chessboard code by Philip Braker

f = open("C:/tmp/demo.html","w+")

f.write("<html>\n\t<head>\n\t\t    <title>\n\t\t\t'James Smith'</title>\n")
f.write("\t<body>\n\t\t<table border=1>\n")

for o in range(65,73):
  f.write("\t\t\t<tr>" )
  for i in range(8):
    if (i+o)%2==0:
      f.write("\t\t\t\t<td style='width:30px;height:30px;'> %s%s </td>\n" % (chr(o), str(i+1)))
    else: 
      f.write("\t\t\t\t<td style='width:30px;height:30px;' bgcolor='pink'> %s%s </td>\n" % (chr(o), str(i+1)))
  f.write("\t\t\t</tr>")
f.write("\t\t</table>\n\t</body>\n</html>")
f.close()
