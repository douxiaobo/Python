import difflib

str1= "Python Programming is easy"
str2= "Python Programming is excellent"

matcher=difflib.SequenceMatcher(None, str1, str2)   ## SequenceMatcher 类用于比较两个序列的相似性
print(matcher.ratio())


text1=str1.split()
text2=str2.split()
d=difflib.Differ()
diff=list(d.compare(text1, text2))
for line in diff:
    print(line)

for line in diff:
    if line[0]==' ': continue
    elif line[0]=='-':
        print('删除：', repr(line[1:]))
    elif line[0]=='+':
        print('新增：', repr(line[1:]))


diff=difflib.ndiff(str1.splitlines(), str2.splitlines())
for line in diff:
    print(line)


words=['Python', 'Programming', 'is', 'easy']
matches=difflib.get_close_matches('Python', words)
print(matches)


## difflibHtmlDiff      没有机会写代码