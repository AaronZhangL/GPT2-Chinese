import sys
import os
import argparse
import pickle

'''
移除Vocab文件中重复字符
'''


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--from_path', default='data/from.txt',
                        type=str, required=False, help='原始文件路径')
    parser.add_argument('--save_path', default='data/result.txt',
                        type=str, required=False, help='结果文件路径')

    args = parser.parse_args()
    print('args:\n' + args.__repr__())

    from_path = args.from_path
    save_path = args.save_path
    itemlist = list()
    #with open(from_path, 'rb') as fp:
    #    itemlist = pickle.load(fp)

    #with open(from_path) as f:
    #    itemlist = f.readlines()

    #new_list = list(set(itemlist))
    #[x for x in new_list if x]
    #with open(save_path, 'wb') as fp:
    #    pickle.dump(new_list, fp)

    #with open(save_path, mode='w') as f:
    #    f.writelines(new_list)

    lines_seen = set()  # holds lines already seen
    with open(save_path, "w") as fo:
        for line in open(from_path, "r"):
            print("line=>" + line + "<=")
            if line is None or len(line) == 0 or len(line.strip()) == 0:
                print("----skip string-----")
                print(line)
                continue
            else:
                if line not in lines_seen:  # not a duplicate
                    fo.write(line)
                    if line is not None:
                        print("Add to set()")
                        lines_seen.add(line)
    print("print set()")
    print(str(lines_seen))


if __name__ == '__main__':
    main()
