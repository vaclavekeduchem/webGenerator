from yattag import Doc
import requests


def createHTMLFile(name, html):
    f = open(f"{name}.html", "w", encoding="UTF-8")
    f.write(html)
    f.close()


if __name__ == "__main__":
    doc, tag, text = Doc().tagtext()
    r = requests.get("https://dummyjson.com/products")
    doc.asis('<!DOCTYPE html>')
    with tag('html'):
        with tag('head'):
            with tag('title'):
                text('Produky')
        with tag('body'):
            for product in r.json()['products']:
                with tag('h1'):
                    text(product["title"])
                with tag('p'):
                    text(product["description"])
                with tag('div'):
                    for image in product["images"]:
                        doc.stag('img', src=image, height="128", width="128")
                with tag('p'):
                    with tag('strong'):
                        text(f'{product["price"]} €')
    createHTMLFile("generated", doc.getvalue())
