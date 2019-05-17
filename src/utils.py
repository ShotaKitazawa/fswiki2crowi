#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import codecs

import urllib.parse

code_flag = False
table_flag = False


def euc2utf8(filename_euc):
    return urllib.parse.unquote(filename_euc, "euc-jp")


def euc2utf8_file(filepath_euc):
    fin = codecs.open(filepath_euc, "r", "euc-jp", errors="ignore")
    array = []
    for row in fin:
        array.append(row)
    fin.close()
    return array


def fs2md(line):
    global code_flag, table_flag
    markdown = ""

    if not (code_flag):
        if (table_flag):
            if not (line.startswith(",")):
                table_flag = False

        if (line.startswith("{{pre")):
            markdown = "```\n"
            code_flag = True
        elif (line.startswith("!!!")):
            markdown = "#" + line[3:]
        elif (line.startswith("!!")):
            markdown = "##" + line[2:]
        elif (line.startswith("!")):
            markdown = "###" + line[1:]
        elif (line.startswith("***")):
            markdown = "        -" + line[3:]
        elif (line.startswith("**")):
            markdown = "    -" + line[2:]
        elif (line.startswith("*")):
            markdown = "-" + line[1:]
        elif (line.startswith("\"\"")):
            markdown = "> " + line[3:]
        elif (line.startswith(",")):
            if not (table_flag):
                table_flag = True
                markdown = line.replace(",", "|").replace("\n", "") + "|\n|"
                for i in range(line.count(",")):
                    markdown += "-|"
                markdown += "\n"
            else:
                markdown = line.replace(",", "|").replace("\n", "") + "|\n"
        else:
            markdown = line

        markdown.replace("'''", "**")
        markdown = re.sub(r'<<\(.*\)>>', '`\1`', markdown)

    elif (line.startswith("}}")):
        markdown = "```\n"
        code_flag = False
    else:
        markdown = line
    return markdown


if __name__ == '__main__':
    pass
