import webbrowser
import time
new = 0
count =0
break_count = 3
print ("The program began on time"+time.ctime())
#url = "https://pythonconquerstheuniverse.wordpress.com/2010/10/16/how-to-open-a-web-browser-from-python/"
url = "https://youtu.be/ac7xsFCzvxw"
while (count < break_count):
	time.sleep(5)
	webbrowser.open(url,new)
	count = count + 1