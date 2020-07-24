"""
For information about how the program works, see the program notes file: 
https://github.com/KatherineMichel/til-100-days-of-code-version/blob/master/program_notes.py
"""

import os
from datetime import datetime

from twython import Twython

twitter = Twython(
    os.environ.get("APP_KEY"),
    os.environ.get("APP_SECRET"),
    os.environ.get("OAUTH_TOKEN"),
    os.environ.get("OAUTH_TOKEN_SECRET"),
)

HEADER = """\
# TIL- 100 Days of Code Version

Placeholder
"""

FOOTER = """\

## ToDo

* Add `parse_til()` notes to program_notes.py
* Fill in header and footer
* Add total TILs
* Humanize "Tils" plural
* Create GitHub template

## License

This project is adapted from a [Today I Learned](https://github.com/khanhicetea/today-i-learned/) project by [@khanhicetea](https://github.com/khanhicetea), distributed under the [Creative Commons Attribution License](http://creativecommons.org/licenses/by/3.0/). 

See my [TIL- 100 Days of Code Version](https://github.com/KatherineMichel/portfolio/blob/master/regular-blog-posts/til-100-days-of-code-version.md) blog post for information about the [changes I made](https://github.com/KatherineMichel/portfolio/blob/master/regular-blog-posts/til-100-days-of-code-version.md#changes-i-made).
"""


def main():

    root = "."

    excludes = ["archive", "drafts"]

    categories = [
        dir
        for dir in os.listdir(root)
        if os.path.isdir(dir) and dir not in excludes and not dir.startswith(".")
    ]
    categories.sort()

    content = ""

    recent_content = ""
    cat_content = ""

    recent_tils = []

    count = 0

    content += HEADER

    cat_content += "| **By Category** | :books: |\n| -------- | -------- |\n"

    for cat in categories:
        cat_tils = []
        for file in os.listdir(os.path.join(root, cat)):
            raw = read_files(os.path.join(root, cat, file))
            parts = raw.split("/---/")
            for part in parts:
                til = parse_til(part.strip(), cat)
                til["file_name"] = file
                cat_tils.append(til)
                recent_tils.append(til)

        cat_tils.sort(key=lambda a: a["date"])
        cat_content += f"| **{cat.capitalize()}** [ {len(cat_tils)} Tils ] | |\n"
        for til in cat_tils:
            count += 1
            cat_content += f"| {count}. [{til['title']}]({til['category']}/{til['file_name']}) | {til['date'].strftime('%Y-%m-%d')} |\n"
    cat_content += "\n"

    recent_tils.sort(reverse=True, key=lambda a: a["date"])
    recent_content += "| **5 Most Recent TILs** | :tada: |\n| -------- | -------- |\n"
    for til in recent_tils[0:5]:
        recent_content += f"| [{til['title']}]({til['category']}/{til['file_name']}) [{til['category']}] | {til['date'].strftime('%Y-%m-%d')} |\n"
    recent_content += "\n"

    content += recent_content
    content += cat_content

    content += FOOTER

    with open("README.md", "w") as fd:
        fd.write(content)

    status = recent_tils[0]["status"]

    tweet = status
    print(tweet)
    # twitter.update_status(status=tweet)


def read_files(file_path):
    with open(file_path, "r") as fd:
        return fd.read()


def parse_til(content, category):
    pos1 = content.find("- Date : ")
    pos2 = content.find("- Tags : ", pos1)
    pos3 = content.find("- Status : ", pos2)
    pos4 = content.find("\n", pos3)
    pos5 = content.find("##", pos4)
    pos6 = content.find("\n", pos5)
    post = {
        "category": category,
        "date": datetime.strptime(content[pos1 + 9 : pos2].strip(), "%Y-%m-%d"),
        "tags": [t[1:] for t in content[pos2 + 9 : pos3].strip().split(" ")],
        "status": content[pos3 + 11 : pos4].strip(),
        "title": content[pos5 + 3 : pos6].strip(),
    }

    return post


if __name__ == "__main__":
    main()
