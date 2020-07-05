#!/user/bin/python
# Author: Philip Braker

title = "James Smith Site"
page_title =  "This is the home page of James Smith"
page_content = "This is the story of my life ... blah blah blah ... the end"

templ = open("template.html","r")
base = templ.read()

newpg = open("index.html","w+")
newpg.write(base.format(title=title,page_title=page_title,page_content=page_content))

templ.close()
newpg.close()

