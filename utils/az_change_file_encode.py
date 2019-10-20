import os
import shutil
from chardet import detect
import argparse
import multiprocessing as mp


def get_encoding_type(file):

    # get file encoding type
    with open(file, 'rb') as f:
        rawdata = f.read()
    return detect(rawdata)['encoding']


def change_encode(srcfile, trgfile, file_count):
    # TODO: mkdir subfolder
    # error_dir = "errorFile"
    # error_dir_path = os.path.join(srcfile, error_dir)
    # if not os.path.exists(error_dir_path):
    #    os.mkdir(error_dir_path)

    from_codec = get_encoding_type(srcfile)
    print("from_coder(basic): " + str(from_codec))
    if from_codec is None or from_codec.upper() == "GB2312" or from_codec.upper() == "GBK":
        from_codec = "GB18030"  # 包含的字符个数：GB2312 < GBK < GB18030
    print("from_coder(changed): " + str(from_codec))
    # add try: except block for reliability
    try:
        with open(srcfile, 'r', encoding=from_codec) as f, open(trgfile, 'w', encoding='utf-8') as e:
            text = f.read()  # for small files, for big use chunks
            e.write(text)

        # os.remove(srcfile)  # remove old encoding file
        # os.rename(trgfile, srcfile)  # rename new encoding

    except UnicodeDecodeError:
        print('###------------------ Decode Error ------------------###')
        # print(e.object.decode("utf-8"))
        shutil.copyfile(srcfile, srcfile + ".UnicodeDecodeError." + str(file_count))

    except UnicodeEncodeError:
        print('###------------------ Encode Error ------------------###')
        # print(e.object.encode("utf-8"))
        shutil.copyfile(srcfile, srcfile + ".UnicodeEncodeError." + str(file_count))
    else:
        print('finish (no error)')

    try:
        print("encode file from[" + srcfile + "] to [" + trgfile + "]")
    except Exception:
        print("### print file name error-2 ###")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--SrcFilePath', default='',
                        type=str, required=True, help='元文件文件夹')
    parser.add_argument('--TrgFilePath', default='',
                        type=str, required=True, help='目标文件文件夹')

    args = parser.parse_args()
    print('args:\n' + args.__repr__())
    SrcFilePath = args.SrcFilePath
    TrgFilePath = args.TrgFilePath

    file_count = 0
    if os.path.isdir(SrcFilePath):
        for file in os.listdir(SrcFilePath):
            if file.endswith(".txt"):
                srcfile = os.path.join(SrcFilePath, file)
                trgfile = os.path.join(TrgFilePath, "train-" + str(file_count) + ".txt")
                logfile = os.path.join(TrgFilePath, "log-train.txt")
                try:
                    with open(logfile, 'a', encoding='utf-8') as lf:
                        lf.write("No=" + str(file_count) + "\n")
                        lf.write(srcfile + "\n")
                        lf.write(trgfile + "\n")
                    print("[srcfile]" + srcfile + " ==> " + "[trgfile]" + trgfile)
                except Exception:
                    print("### print file name error-1 ###")

                change_encode(srcfile, trgfile, file_count)
                file_count += 1



if __name__ == '__main__':
    p = mp.Process(target=main)
    p.start()
    p.join()
    # main()
