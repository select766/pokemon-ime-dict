import os
import glob
import jaconv

SRC_DIR = "data"
DST_DIR = "msime"


def convert_file(src, dst):
    with open(src, encoding="utf-8") as srcf:
        with open(dst, "w", encoding="utf-16", newline="\r\n") as dstf:
            for line in srcf:
                elems = line.rstrip().split("\t")
                tango = elems[0]
                if len(elems) == 1:
                    yomis = [jaconv.kata2hira(tango)]
                else:
                    yomis = elems[1:]
                for yomi in yomis:
                    dstf.write(f"{yomi}\t{tango}\t固有名詞\n")


def main():
    for src in glob.glob(os.path.join(SRC_DIR, "*.tsv")):
        convert_file(src, os.path.join(DST_DIR, os.path.basename(src)[:-4] + ".txt"))


if __name__ == '__main__':
    main()
