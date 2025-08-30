from bs4 import BeautifulSoup

html_doc = """"
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1 id="header">
        Hello World!
    </h1>

    <div class="group1">
        <h2>
            Programming
        </h2>

        <ul>
            <li>HTML</li>
            <li>CSS</li>
            <li>JavaScript</li>
        </ul>
    </div>
    <div class="group2">
        <h2>
            Design
        </h2>

        <ul>
            <li>Photoshop</li>
            <li>Illustrator</li>
        </ul>
    </h2>
    </div>
    <div class="group3">
        <h2>
            Lifestyle
        </h2>

        <ul>
            <li>Photography</li>
            <li>Cinema</li>
        </ul>
    </div>
    <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>
    <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>
    <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>
</body>
</html>
"""

soup = BeautifulSoup(html_doc, "html.parser")

result = soup.prettify()
result = soup.title
result = soup.head
result = soup.body

result = soup.title.name
result = soup.title.string
result = soup.h1
result = soup.h2
result = soup.h2.name
result = soup.h2.string

result = soup.find_all("h2")
result = soup.find_all("h2")[0]
result = soup.find_all("h2")[1]

result = soup.div
result = soup.find_all("div")
result = soup.find_all("div")[0]
result = soup.find_all("div")[1]
result = soup.find_all("div")[1].ul.find_all("li")

result = soup.div.findChildren(recursive = False)
result = soup.div.findNextSibling().findNextSibling().findPreviousSibling()

for i in soup.find_all("a"):
    # result = i.get("href")
    result = i.get("id")
    print(result)
    
# print(result)

