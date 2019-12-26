
with open('test_new.txt','w') as new:  # 新建一个文档
    for line in lines:
        if line not in ['0\n','1\n']:
            new.write(line)   