# import jieba

# text="我爱上海东方明珠"

# seg_list=jieba.cut(text,cut_all=False)
# seg_list=list(seg_list)
# print(seg_list)

# jieba.lcut(text)就是list(jieba.cut(text))

################################################################################################################


# import jieba
# text="我爱上海东方明珠"
# print("精确模式：",jieba.lcut(text))
# print("全模式：",list(jieba.cut(text,cut_all=True)))

# (jieba) douxiaobo@192 jieba % python3 demo.py
# Building prefix dict from the default dictionary ...
# Loading model from cache /var/folders/w6/m3p5s_493_lfr5qmr1w96x7m0000gn/T/jieba.cache
# Loading model cost 0.260 seconds.
# Prefix dict has been built successfully.
# 精确模式： ['我', '爱', '上海', '东方明珠']
# 全模式： ['我', '爱', '上海', '上海东方', '海东', '东方', '东方明珠', '方明', '明珠']



################################################################################################################


# import jieba
# text="我爱上海东方明珠"
# result=jieba.cut_for_search(text)
# print("搜索引擎模式：","/".join(result))

# (jieba) douxiaobo@192 jieba % python3 demo.py
# Building prefix dict from the default dictionary ...
# Loading model from cache /var/folders/w6/m3p5s_493_lfr5qmr1w96x7m0000gn/T/jieba.cache
# Loading model cost 0.257 seconds.
# Prefix dict has been built successfully.
# 搜索引擎模式： 我/爱/上海/东方/方明/明珠/东方明珠


################################################################################################################

# import jieba
# comments=[
#     "我爱上海东方明珠",
#     "巴黎是法国的首都",
#     "创造劳动最光荣"
# ]
# tokenized_comments=[]
# for comment in comments:
#     words=jieba.cut(comment)
#     tokenized_comments.append(list(words))
# print(tokenized_comments)

# (jieba) douxiaobo@192 jieba % python3 demo.py
# Building prefix dict from the default dictionary ...
# Loading model from cache /var/folders/w6/m3p5s_493_lfr5qmr1w96x7m0000gn/T/jieba.cache
# Loading model cost 0.253 seconds.
# Prefix dict has been built successfully.
# [['我', '爱', '上海', '东方明珠'], ['巴黎', '是', '法国', '的', '首都'], ['创造', '劳动', '最', '光荣']]
# (jieba) douxiaobo@192 jieba % 



################################################################################################################


# import jieba

# jieba.add_word("上海")
# jieba.add_word("东方明珠")

# print(list(jieba.cut("我爱上海东方明珠")))

# (jieba) douxiaobo@192 jieba % python3 demo.py
# Building prefix dict from the default dictionary ...
# Loading model from cache /var/folders/w6/m3p5s_493_lfr5qmr1w96x7m0000gn/T/jieba.cache
# Loading model cost 0.256 seconds.
# Prefix dict has been built successfully.
# ['我', '爱', '上海', '东方明珠']
# (jieba) douxiaobo@192 jieba % 


################################################################################################################


# (jieba) douxiaobo@192 jieba % python3 text.py
# Building prefix dict from the default dictionary ...
# Dumping model to file cache /var/folders/w6/m3p5s_493_lfr5qmr1w96x7m0000gn/T/jieba.cache
# Loading model cost 0.256 seconds.
# Prefix dict has been built successfully.
# ['我', '爱', '上海', '东方明珠']
# (jieba) douxiaobo@192 jieba % 


################################################################################################################

# import jieba.posseg as pseg
# text="我爱上海东方明珠"
# words=pseg.cut(text)
# for word in words:
#     print(word.word,word.flag)

# (jieba) douxiaobo@192 jieba % python3 demo.py
# Building prefix dict from the default dictionary ...
# Loading model from cache /var/folders/w6/m3p5s_493_lfr5qmr1w96x7m0000gn/T/jieba.cache
# Loading model cost 0.249 seconds.
# Prefix dict has been built successfully.
# 我 r
# 爱 v
# 上海 ns
# 东方明珠 nr


################################################################################################################



# import jieba.analyse as analyse
# text="自然语言处理是人工智能的一部分，主要包括词法分析、语义理解和信息抽取等。"
# keywords=analyse.extract_tags(text,topK=5)
# print(keywords)

# (jieba) douxiaobo@192 jieba % python3 demo.py
# Building prefix dict from the default dictionary ...
# Loading model from cache /var/folders/w6/m3p5s_493_lfr5qmr1w96x7m0000gn/T/jieba.cache
# Loading model cost 0.248 seconds.
# Prefix dict has been built successfully.
# ['词法', '自然语言', '语义', '人工智能', '抽取']
# (jieba) douxiaobo@192 jieba % 



################################################################################################################



# douxiaobo@192 jieba % python3 -m venv jieba
# douxiaobo@192 jieba % source jieba/bin/activate
# (jieba) douxiaobo@192 jieba % pip3 install jieba
# Collecting jieba
#   Downloading jieba-0.42.1.tar.gz (19.2 MB)
#      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 19.2/19.2 MB 91.6 kB/s  0:03:27
#   Installing build dependencies ... done
#   Getting requirements to build wheel ... done
#   Preparing metadata (pyproject.toml) ... done
# Building wheels for collected packages: jieba
#   Building wheel for jieba (pyproject.toml) ... done
#   Created wheel for jieba: filename=jieba-0.42.1-py3-none-any.whl size=19314509 sha256=382a96fb32b8eeddb149f359d13ead3d61ccd85ecd0e273c38b24c94f62af45f
#   Stored in directory: /Users/douxiaobo/Library/Caches/pip/wheels/8d/e9/51/2f0a6a9d051293af20e265d3889beae50efe2de72f8511c801
# Successfully built jieba
# Installing collected packages: jieba
# Successfully installed jieba-0.42.1

# [notice] A new release of pip is available: 25.2 -> 26.1.1
# [notice] To update, run: pip install --upgrade pip
# (jieba) douxiaobo@192 jieba % code .          


# (jieba) douxiaobo@192 jieba % mv text.py demo.py



# https://github.com/fxsjy/jieba