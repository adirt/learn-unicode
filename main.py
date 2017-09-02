import os


def main():
    workdir = os.getcwd()
    str_filenames = os.listdir('data')
    unicode_filenames = os.listdir(u'data')
    str_files = [open(os.path.join(workdir, 'data', str_filename))
                 for str_filename in str_filenames]
    for str_file in str_files:
        content = str_file.read()
        print content
        str_file.close()
    unicode_files = [open(os.path.join(workdir, u'data', unicode_filename))
                     for unicode_filename in unicode_filenames]
    for unicode_file in unicode_files:
        content = unicode_file.read()
        print content
        unicode_file.close()

if __name__ == '__main__':
    main()