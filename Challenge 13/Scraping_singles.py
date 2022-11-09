import urllib.request
import html

def read_website(url):
    mybytes = url.read() #reads an html file as bytes
    mystr = mybytes.decode("utf8") # decodes the bytes to a string. utf8 is unicode
    mystr = html.unescape(mystr) #for special characters
    return mystr

def get_singles(mystr):
    position = mystr.find('<div class="title">') #looking for song in html
    count = 1
    while position != -1 and count <= 10: #this is because -1 is returned in case html is not found
        start = mystr.find(">", position+len('<div class="title">')) + 1 # to find the first > after the title tag
        stop = mystr.find("<", start) # to find the first < after the start tag
        print(f"{count}){mystr[start:stop]}")
        position = mystr.find('<div class="title">', stop)
        count = count + 1

if __name__ == "__main__":
    fp = urllib.request.urlopen("https://www.officialcharts.com/charts/singles-chart/")
    web_str = read_website(fp)
    get_singles(web_str)
