import requests
import webbrowser

filename = "new_stn.html"

res = requests.get("https://www.is.fi")

html = res.text
data = html.split("<span>")
new_html = data[0]
for line in data[1:]:
    index = line.find("</span>")
    new_html += "<span>" + line[:index] + " saatana" + line[index:]
    
with open(filename, "w") as f:
    f.write(new_html)
    
webbrowser.get('firefox').open_new_tab(filename)
