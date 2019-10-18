import os
from chardet import detect
import argparse
import multiprocessing as mp


def get_encoding_type(file):

    # get file encoding type
    with open(file, 'rb') as f:
        rawdata = f.read()
    return detect(rawdata)['encoding']


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--srcfile', default='',
                        type=str, required=True, help='元文件')
    parser.add_argument('--trgfile', default='',
                        type=str, required=True, help='目标文件')

    args = parser.parse_args()
    print('args:\n' + args.__repr__())
    srcfile = args.srcfile
    trgfile = args.trgfile
    from_codec = get_encoding_type(srcfile)

    # add try: except block for reliability
    try:
        with open(srcfile, 'r', encoding=from_codec) as f, open(trgfile, 'w', encoding='utf-8') as e:
            text = f.read()  # for small files, for big use chunks
            e.write(text)

        # os.remove(srcfile)  # remove old encoding file
        # os.rename(trgfile, srcfile)  # rename new encoding
    except UnicodeDecodeError:
        print('Decode Error')
    except UnicodeEncodeError:
        print('Encode Error')


if __name__ == '__main__':
    p = mp.Process(target=main)
    p.start()
    p.join()
