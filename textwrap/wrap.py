import textwrap

text_English = "Every morning, I wake up at seven o'clock.I wash my face and brush my teeth in the bathroom.Then I eat breakfast with my family.My favorite breakfast is toast with eggs and a glass of milk.After breakfast, I put on my school bag and walk to school.The morning air is fresh and cool.I always feel happy when a new day begins."
text_Chinese = "每天早上，我七点钟起床。我在浴室里洗脸、刷牙。然后和家人一起吃早饭。我最喜欢的早餐是吐司配鸡蛋，还有一杯牛奶。吃完早饭，我背上书包走路去学校。早晨的空气清新又凉爽。每当新的一天开始，我总是感到很开心。"

lines_Chinese=textwrap.wrap(text_Chinese,width=10)      ## 按汉字数字统计
for line in lines_Chinese:
    print(line)

lines_English=textwrap.wrap(text_English,width=20)      ## 按字母数字统计
for line in lines_English:
    print(line)

filled_Chinese=textwrap.fill(text_Chinese,width=10)      ## 按汉字数字统计
print(filled_Chinese)

filtered_English=textwrap.fill(text_English,width=20)      ## 按字母数字统计
print(filtered_English)

shortened_English=textwrap.shorten(text_English,width=50)      ## 当文本超过指定宽度时，该函数会先折叠连续空白符，再通过placeholder参数（默认[...]）标记截断位置。
print(shortened_English)

shortened_Chinese=textwrap.shorten(text_Chinese,width=50)      ## 当文本超过指定宽度时，该函数会先折叠连续空白符，再通过placeholder参数（默认[...]）标记截断位置。
print(shortened_Chinese)

indented="""
    This is an indented paragraph.
    It has multiple lines.
    It also contains leading whitespace.
    It will be left-aligned.
"""

print(indented)

dedented=textwrap.dedent(indented)    ## 移除文本中每一行的相同前缀空白符   移除缩进
print(dedented)

prefixed=textwrap.indent(dedented,prefix=">>> ")    ## 在每行文本前面添加指定前缀   添加缩进
print(prefixed)

wrapper=textwrap.TextWrapper(width=20,initial_indent=">>> ",subsequent_indent="...",expand_tabs=True,replace_whitespace=True)
print(wrapper.wrap(text_English))
for line in wrapper.wrap(text_English):
    print(line)

# 示例：保留换行符
text_with_newlines = "这是第一行。\n\n这是第二行。"
wrapped_text = textwrap.fill(text_with_newlines, width=20, replace_whitespace=False)
print(wrapped_text)

# 示例：自定义断行逻辑
long_word_text = "这是一个非常长的单词，它不能被拆分。"
wrapped_text = textwrap.fill(long_word_text, width=10, break_long_words=True)
print(wrapped_text)

# 示例：自定义缩进和前缀
text = "这是一个包含多个段落的文本。每个段落都应该有自己的缩进。"
wrapped_text = textwrap.fill(text, width=30, initial_indent="    ", subsequent_indent="    ")
print(wrapped_text)