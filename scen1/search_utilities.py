import click
import os
import re
from logger import Logger
from database import Database
extension = "\.(txt|py|xml|json)$"

db = Database()
logger = Logger(db)

def grep_via_x(file, pattern, re_or_grep):
    valid_path = re.search(extension, file)
    if not valid_path:
        print("invalid file, only txt, py, xml, json extensions supported")
        logger.log_a_logxd('ERROR', f'grep_via_{re_or_grep}({file, pattern}) - invalid file, only txt, py, xml, json extensions supported')
    elif not os.path.isfile(file):
        print("file not found")
        logger.log_a_logxd('ERROR', f'grep_via_{re_or_grep}({file, pattern}) - file not found')
    else:
        if re_or_grep == 're':
            with open(file) as f:
                for line in f:
                    if re.search(pattern, line):
                        print(line, end="")
        elif re_or_grep == 'grep':
            cmd = "cat " + file + " | grep -E \"" + pattern + "\""
            os.system(cmd)