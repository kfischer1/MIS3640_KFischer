def sed(pattern, replace, source, dest):
    """Reads a source file and writes the destination file.
    In each line, replaces pattern with replace.
    pattern: string
    replace: string
    source: string filename
    dest: string filename
    """
    f_in = open(source, 'r')        # reads the source we are changing
    f_out = open(dest, 'w')         # writes the new file with the changes we are making to source

    for line in f_in:
        new_line = line.replace(pattern, replace)
        f_out.write(new_line)               #will be saved as 'new_sed_tester.txt'

    f_in.close()
    f_out.close()

def main():
    pattern = 'Hey Jude'
    replace = 'Hi Jerry'
    source = 'sed_tester.txt'
    dest = 'new_' + source
    sed(pattern, replace, source, dest)


if __name__ == '__main__':
    main()