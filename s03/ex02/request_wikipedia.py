import wikipedia
import sys

def create_file(input: str, content: str):
    filename = input.replace(" ", "_") + ".wiki"
    f = open(filename, "w")
    f.write(content)
    f.close()

def wiki_suggest(input):
    search = wikipedia.search(input)
    if len(search) > 0:
        return search[0]
    else:
        return wikipedia.suggest(input)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Input only single argument")
        sys.exit(1)
    input = sys.argv[1]
    try:
        suggest = wiki_suggest(input)
        page = wikipedia.page(suggest)
        create_file(input, page.content)
    except Exception as e:
        print('Error:', e)
