# extract_specific_lines

## 1 Introduction

`extract_specific_lines` is a tool to extract specific lines which maps the query ids (of the query file) from the subject file.

## 2 Installation

    pip install extract_specific_lines

There will be a command `extract_specific_lines` created under the same directory as your `pip` command.

## 3 Usage

    usage: extract_specific_lines.py [-h] [-q <str> [<str> ...]] [-f <query file>]
                                     [-s [<subject file>]] [-s1 <pattern>]
                                     [-s2 <pattern>] [-d1 [<int>]] [-d2 [<int>]]
                                     [-o [<outfile>]] [-v] [-V] [--version]

    to extract specific lines from the subject file which maps the query ids.
    written by Guanliang MENG

    optional arguments:
      -h, --help            show this help message and exit
      -q <str> [<str> ...]  query list
      -f <query file>       query list file
      -s [<subject file>]   subject file [stdin]
      -s1 <pattern>         query file sep_pattern [\s+]
      -s2 <pattern>         subject file sep_pattern [\s+]
      -d1 [<int>]           which field in the query_file is to used? [0]
      -d2 [<int>]           which field in the subject_file is to used? [0]
      -o [<outfile>]        outfile [stdout]
      -v                    invert the output [False]
      -V                    verbose output
      --version             show program's version number and exit
      
## Author
Guanliang MENG

## Citation
Currently I have no plan to publish `extract_specific_lines`.







