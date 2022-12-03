import os
import sys
import json
from typing import List
import requests
import re


def get_session():
    """loads a adventofcode.com session cookie from env.json"""
    env = json.load(open("env.json"))
    cookie = requests.cookies.create_cookie(name="session", value=env["session"])
    sess = requests.session()
    sess.cookies.set_cookie(cookie)
    return sess


def Download(filepattern, urlpattern, day):
    filepath = filepattern.format(day)
    url = urlpattern.format(day)

    if not os.path.exists(filepath):
        print("Downloading from adventofcode.com")
        print(url)
        res = get_session().get(url)
        if res.status_code != 200:
            print("*** error downloading ***")
            return None
        puzzle = res.text.strip()
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(puzzle)
        return puzzle
    else:
        print(url)

    with open(filepath, encoding="utf-8") as f:
        return f.read()


def GetDay():
    return int(sys.argv[0].split("_")[-1].split(".")[0])


def ReadPuzzle() -> List[str]:
    return Download(
        "./data/puzzle_{:02}.txt", "https://adventofcode.com/2022/day/{}/input", GetDay()
    ).split("\n")


def ReadExamplePuzzle():
    instructions = Download(
        "./data/instructions_{:02}.html", "https://adventofcode.com/2022/day/{}", GetDay()
    )
    datamatch = re.search("For example.*?:[\s\S]+?\<code\>([\s\S]+?)\n?\<\/code\>", instructions, re.MULTILINE)
    answermatch = re.search("\<code\>\<em\>(.*?)\<\/em\>\<\/code\>", instructions)

    answer = None
    try:
        answer = int(answermatch.group(1))
    except:
        pass
    return datamatch.group(1).split("\n"), answer


def Test(part, answer, expected):
    if answer is None or answer != expected:
        print(f"Part {part} test: {answer}, expected {expected}", file=sys.stderr)
        return False
    else:
        print(f"Part {part} test: {answer} is expected")
        return True


def Answer(part, answer):
    print("-" * 80)
    print(f"Part {part} answer: {answer}")
    print("-" * 80)
