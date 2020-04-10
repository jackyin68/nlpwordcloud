import re

with open('../corpus/nlpjob.txt', 'w') as dst_file:
    with open('../data/nlpjob.txt', 'r') as src_file:
        for line in src_file.readlines():
            print("读取的数据为: %s" % line)
            # line = re.sub(r'职位描述', '', line)
            # line = line.strip()
            if line and (not re.search(r'[职位描述|任职要求|加分|工作内容]', line)):
                dst_file.writelines(line)

    src_file.close()
dst_file.close()
