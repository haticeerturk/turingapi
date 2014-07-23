import urllib2 , re

turkce = raw_input("Turkce kelime girin : ")

url = "http://glosbe.com/gapi/translate?from=tr&dest=en&format=json&phrase=" + turkce + "&callback=my_custom_function_name&pretty=true"

cevap = urllib2.urlopen(url)

oku = cevap.read()

ingilizce = re.findall('"phrase" : {\n      "text" : "(.*?)"', oku)

cumleler = re.findall('"text" : "(.*?)",',oku)

dosya = open("turing.txt","a")

satir =  turkce + "\t" + ":" + ingilizce[0] + "," + ingilizce[1] + "\n"

for i in range(len(cumleler)) :

       if len(cumleler[i]) >= 20 :

               cumle = "Ornek cumle : " + cumleler[i] + "\n" + "\n"

               break

print satir

print cumle

dosya.write(satir)

dosya.write(cumle)

print "Kelime dosyaya eklendi."

dosya.close
