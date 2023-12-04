# Advent of Code Setup Script

This Python script is designed to automate the setup of new puzzles for the Advent of Code challenge.

## Requirements

- Python 3
- `requests` library
- `html2text` library
- `dotenv` library

## Usage

The script accepts the following command line arguments:

- `-d`, `--day`: The day of the puzzle (required).
- `-y`, `--year`: The year of the puzzle. If not specified, will use the current year.
- `-i`, `--instructions`: Add the puzzle instructions as a comment in the day_xx.py file.
- `-o`, `--open`: Open the day_xx.py file in your default text editor.
- `-s`, `--second`: Get the second puzzle instructions and appends it to the file.

Example usage:

```bash
python setup.py -d 1 -y 2023 -i -o
```

This will create the necessary directories and files for day 1 of the 2023 Advent of Code challenge, fetch the puzzle instructions and input, and open the Python file in your default text editor.

Files are created in directory where `setup.py` is located and use the following pattern: `<year>/<day_xx>/<day_xx.py>`
`<year>/<day_xx>/input.txt`


Environment Variables
The script requires an Advent of Code session token to fetch puzzle instructions and input. This should be provided in a .env file in the same directory as the script, with the key AOC_SESSION_TOKEN.

Example .env file:
```
AOC_SESSION_TOKEN=your-session-token-here
```

Please replace "your-session-token-here" with your actual session token. You can get a session token by requesting a day's page in Advent of Code and then investigating the API call via Developer Tools.

## License

This project is licensed under the terms of the MIT license.
MIT License

Copyright (c) 2023 Simon Walter

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
