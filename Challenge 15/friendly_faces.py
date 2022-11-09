import csv
csv_file = Path("Premier 16-17.csv")
def read_csv(csv_file):
    ## read the specified csv file just like Challenge 10
    
def read_html(html_file):
    ## read a html file as a regular file
            
def process(csv, html):
    ## replace link1...link5 in html with corresponding values fronm csv
    ## Similarly do for initials1...intitials5 and name1...name5

def write_html(path, html):
    ## write the new contents into an html file


if __name__ == "__main__":
    csv = read_csv("south.csv")
    html = read_html("south.html")
    html = process(csv, html)
    write_html("south_final.html", html)
