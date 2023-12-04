import argparse
import os
import re
from datetime import datetime

import requests
import html2text
from dotenv import load_dotenv

load_dotenv()

year = datetime.now().year
session_token = os.getenv("AOC_SESSION_TOKEN")

parser = argparse.ArgumentParser("A script to set up the file structure for a new Advent of Code puzzle.")
parser.add_argument("-d","--day", action="store", type=str, required=True, help="The day of the puzzle.")
parser.add_argument("-y","--year", action="store", type=str, required=False, help="The year of the puzzle. If not specified, will use current  year.")
parser.add_argument("-i","--instructions", action="store_true", required=False, help="Add the puzzle instructions as a comment in the day_xx.py file.")
parser.add_argument("-o","--open", action="store_true", required=False, help="Open the day_xx.py file in your default text editor.")
parser.add_argument("-s","--second", action="store_true", required=False, help="Get the second puzzle instructions and appends it to the file.")

args = parser.parse_args()


def get_puzzle_instructions(day, part=1):
    headers = {"Cookie": "session={}".format(session_token)}
    url = "https://adventofcode.com/{}/day/{}".format(year, day)
    r = requests.get(url, headers=headers)
    
    if part == 1:
        pattern = r"<article class=\"day-desc\">((.|\n)*)<\/article>"
    else:
        pattern = r"<h2 id=\"part2\">((.|\n)*)<\/article>"

    stripped_text = re.search(pattern, r.text)

    if stripped_text:
        return html2text.html2text(stripped_text.group(1))


def get_puzzle_input(day):
    headers = {"Cookie": "session={}".format(session_token)}
    url = "https://adventofcode.com/{}/day/{}/input".format(year, day)
    r = requests.get(url, headers=headers)
    return r.text


if __name__ == "__main__":
    if args.year:
        year = args.year

    if not args.second:
        print("Creating directory and files for day " + args.day)
        if not os.path.isdir(year):
            os.system("mkdir {}".format(year))
        if not os.path.isdir("{}/day_{}".format(year, args.day)):
            os.system("mkdir {}/day_{}".format(year, args.day))
        if not os.path.isfile("{}/day_{}/input.txt".format(year, args.day)):
            os.system("touch {}/day_{}/input.txt".format(year, args.day))
        if not os.path.isfile("{}/day_{}/day_{}.py".format(year, args.day, args.day)):
            os.system("touch {}/day_{}/day_{}.py".format(year, args.day, args.day))
        

        if args.instructions:
            print("Getting puzzle instructions...")
            try:
                if os.stat("{}/day_{}/day_{}.py".format(year, args.day, args.day)).st_size == 0:
                    puzzle_instructions = get_puzzle_instructions(args.day)
                    with open("{}/day_{}/day_{}.py".format(year, args.day, args.day), "a") as f:
                        f.write("\"\"\"\n# Advent of Code {} - Day {}\n## Part 1\n\n{}\"\"\"\n\n".format(year, args.day, puzzle_instructions))
                    print("Puzzle instructions added to day_{}.py".format(args.day))
                else:
                    print("day_{}.py already has content. Skipping instructions.".format(args.day))
            except Exception as e:
                print("Error downloading puzzle instructions. Please check your session token and try again. {}".format(str(e)))
                exit()

        print("Getting puzzle input...")
        try:
            if os.stat("{}/day_{}/input.txt".format(year, args.day)).st_size == 0:
                puzzle_input = get_puzzle_input(args.day)
                with open("{}/day_{}/input.txt".format(year, args.day), "w") as f:
                    f.write(puzzle_input)
                print("Puzzle input added to input.txt")
            else:
                print("input.txt already has content. Skipping input.")
        except Exception as e:
            print("Error downloading puzzle input. Please check your session token and try again. {}".format(str(e)))
            exit()

        print("Done!")

        if args.open:
            os.system("open {}/day_{}/day_{}.py".format(year, args.day, args.day))
    else:
        print("Getting second puzzle instructions...")
        try:
            puzzle_instructions = get_puzzle_instructions(args.day,2)
            with open("{}/day_{}/day_{}.py".format(year, args.day, args.day), "a") as f:
                f.write("\"\"\"\n## Advent of Code {} - Day {}\n\n{}\"\"\"\n\n".format(year, args.day, puzzle_instructions))
            print("Puzzle instructions added to day_{}.py".format(args.day))
        except Exception as e:
            print("Error downloading puzzle instructions. Please check your session token and try again. {}".format(str(e)))
            exit()

        print("Done!")

        if args.open:
            os.system("open {}/day_{}/day_{}.py".format(year, args.day, args.day))
