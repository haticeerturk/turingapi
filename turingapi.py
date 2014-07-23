import urllib2 , re

m = raw_input("Turkce kelime girin : ")

url = "http://glosbe.com/gapi/translate?from=tr&dest=en&format=json&phrase=" + m + "&callback=my_custom_function_name&pretty=true"

response = urllib2.urlopen(url)

oku = response.read()

h = re.findall('"phrase" : {\n      "text" : "(.*?)"', oku)

dosya = open("turing.txt","a")

satir =  m + "\t" + ":" + h[0] + "," + h[1] + "," + h[3] + "\n"

dosya.write(satir)

dosya.close
