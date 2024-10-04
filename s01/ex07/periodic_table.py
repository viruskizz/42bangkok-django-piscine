import sys

css_template = """
body {
    height: 100vh;
    display: flex;
    flex-direction: column;
    align-items: center;
}
h1 {
    text-align: center;
}
table {
    align-self: center;
    border-collapse: collapse;
}
table tr td {
    text-align: center;
    border: 1px solid black;
    padding: 4px;
    font-size: 0.6rem;
    min-width: 60px;
    min-height: 60px;
}
table tr td ul {
    list-style-type: none;
    padding: 0;
    margin: 0;
}
table tr td h4 {
    margin: 0;
    font-weight: lighter;
}
table tr td.empty {
    border: 0 !important;
    background-color: transparent;
}
table tr td li.number {
    font-weight: bolder;
}
table tr td li.small {
    font-size: 1.4em;
    margin: 4px;
    font-weight: 900;
}

tr:first-child td:first-child {
    background-color: #67e8f9;
}
td:nth-child(1) {
    background-color: #f87171;
}
td:nth-child(2) {
    background-color: #fbbf24;
}
td:nth-child(3),
td:nth-child(4),
td:nth-child(5),
td:nth-child(6),
td:nth-child(7),
td:nth-child(8),
td:nth-child(9),
td:nth-child(10),
td:nth-child(11),
td:nth-child(12) {
    background-color: #fef08a;
}
tr:not(:nth-child(1)) td:nth-child(13),
tr:not(:nth-child(1)) td:nth-child(14),
tr:not(:nth-child(1)) td:nth-child(15),
tr:not(:nth-child(1)) td:nth-child(16) {
    background-color: #bef264;
}
tr:nth-child(2) td:nth-child(13),
tr:nth-child(3) td:nth-child(14),
tr:nth-child(4) td:nth-child(14),
tr:nth-child(4) td:nth-child(15),
tr:nth-child(5) td:nth-child(15),
tr:nth-child(5) td:nth-child(16),
tr:nth-child(6) td:nth-child(16) {
    background-color: #86efac;
}
tr:nth-child(2) td:nth-child(14),
tr:nth-child(3) td:nth-child(15),
tr:nth-child(3) td:nth-child(16),
tr:nth-child(4) td:nth-child(16) {
    background-color: #93c5fd;
}
tr:nth-child(2) td:nth-child(15),
tr:nth-child(2) td:nth-child(16),
td:nth-child(17) {
    background-color: #c4b5fd;
}
td:last-child {
    background-color: #c084fc;
}
"""

def create_template(content):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Peiodic Table</title>
    <link rel="stylesheet" href="periodic_table.css">
</head>
<body>
    <h1>Periodic Table</h1>
    {content}
</body>
</html>
"""

def convert(line):
    pd = {}
    name_values = line.strip().split("=")
    name = name_values[0]
    value = {}
    for el in name_values[1].split(","):
        key = el.split(":")[0].strip()
        val = el.split(":")[1].strip()
        value[key] = val
    pd[name] = value
    return pd

def find_element_name(periodic, x, y):
    for name, data in periodic.items():
        level = len(data['electron'].split(' '))
        if int(data['position']) == x and y == level - 1:
            return name

def create_element_box(name, data):
    return f"""
        <td>
           <h4>{name}</h4>
           <ul>
            <li class="number">No {data['number']}</li>
            <li class="small">{data['small']}</li>
            <li>{data['molar']}</li>
            <!-- <li>{data['electron']} electron</li> -->
           </ul>
        </td>\n
        """

def create_table_element(periodic):
    str = ''
    for y in range(7):
        str += '\t\t<tr>\n'
        for x in range(18):
            name = find_element_name(periodic, x, y)
            if name:
                str += create_element_box(name, periodic[name])
            else:
                str += """<td class="empty"></td>\n"""
        str += "\t\t</tr>\n"
    str = f"<table>\n{str}</table>"
    return str

def get_lines(filename):
    f = open(filename)
    lines = f.readlines()
    f.close()
    return lines

def create_file(filename, content):
    f = open(filename, "w")
    f.write(content)
    f.close()

def sort_periodic(item):
    return int(item[1]['number'])

if __name__ == '__main__':
    lines = get_lines("periodic_table.txt")
    periodic = dict()
    for line in lines:
        if line.strip() == "":
            continue
        d = convert(line.strip())
        periodic.update(d)
    periodic = { key: value for key, value in sorted(periodic.items(), key=sort_periodic)}
    # print(periodic)
    content = create_table_element(periodic)
    create_file("periodic_table.html", create_template(content))
    create_file("periodic_table.css", css_template)

