
def updateIndexHtml(message):
    fileappend = open("index.html", "a+")
    fileappend.write("<p>added " + message + "</p>")
    fileappend.close() 

message = input("message update: " )
updateIndexHtml(message)
