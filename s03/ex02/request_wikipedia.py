import sys
import requests
import dewiki

def create_file(input: str, content: str):
    filename = input.replace(" ", "_") + ".wiki"
    f = open(filename, "w")
    f.write(content)
    f.close()

def wiki_search(input: str):
    session = requests.Session()
    url = "https://en.wikipedia.org/w/api.php"
    params = {
        "action": "opensearch",
        "namespace": "0",
        "search": input,
        "limit": "5",
        "format": "json"
    }

    res = session.get(url=url, params=params)
    data = res.json()
    if len(data[1]) == 0:
        return
    return data[1][0]

def wiki_page_content(title: str):
    session = requests.Session()
    url = "https://en.wikipedia.org/w/api.php"
    params = {
        "page": title,
        "action": "parse",
        "prop": "wikitext",
        "formatversion": "2",
        "format": "json"
    }
    res = session.get(url=url, params=params)
    data = res.json()
    wikitext = data["parse"]["wikitext"]
    return dewiki.from_string(wikitext)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Input only single argument")
        sys.exit(1)
    input = sys.argv[1]
    try:
        result = wiki_search(input)
        if result:
            content = wiki_page_content(result)
            create_file(input, content)
        else:
            create_file(input, "")
    except Exception as e:
        print('Error:', e)
