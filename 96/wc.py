def wc(file_):
    """Takes an absolute file path/name, calculates the number of
       lines/words/chars, and returns a string of these numbers + file, e.g.:
       3 12 60 /tmp/somefile
       (both tabs and spaces are allowed as separator)"""
    with open(file_,"r") as count_file:
        cfile = count_file.read()
        linecount = len(cfile.splitlines())
        wordcount = len(cfile.split())
        charcount = len(cfile)
        return f"{linecount} {wordcount} {charcount} {file_}"


if __name__ == '__main__':
    # make it work from cli like original unix wc
    import sys
    print(wc(sys.argv[1]))
