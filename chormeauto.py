import webbrowser as wb

def webAuto():
    chorme_path = "C:\Program Files (x86)\Internet Explorer\ExtExport.exe"

    #list of urls that's you want to open
    urls = [
        "programiz.com",
        "google.com",
        "python.org"
    ]

    #loop through urls list and open them in chorme brower
    for url in urls:
        print("Opening this: ", url)
        wb.get(chorme_path).open(url)

    #call web automation function
    webAuto()