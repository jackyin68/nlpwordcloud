import jieba
import wordcloud
import imageio
# import jieba.analyse
# import matplotlib.pyplot as plt
# from wordcloud import ImageColorGenerator

f = open('../corpus/nlpjob.txt', encoding='utf-8')
nlp_job = f.read()
nlp_job_list = jieba.lcut(nlp_job)
nlp_job_list_words = " ".join(nlp_job_list)

# tfidf
# result = jieba.analyse.textrank(nlp_job, topK=3000, withWeight=True)
# keywords = dict()
# for word in result:
#     keywords[word[0]] = word[1]

stopwords = ['基于', '自然语言处理', '自然语言', '处理', '深度', '熟悉',
             '精通', '技术', '经验', '优先', '学习', '负责', '相关', '开发', '项目', '专业',
             'NLP', '机器', '应用', '具备', '以上', '语言', '实现', '熟练', '以上', '学历', '熟练',
             '能力', '硕士', '以上学历', '研发', '参与', '具有', '使用',
             '知识', '或者', '了解', '熟练掌握', '基础', '常用', '了解', '基础', '一定', '至少',
             '能够', '良好', '一种', '扎实', '较强', '优秀', '一种', '利用', '进行', '良好', '公司', '考虑', '计算机',
             '编程语言', '掌握', '一门', '方面', '包括', '理解', '限于', '丰富', '以下',
             '计算机相关', '以及', '提供', '探索', '同时', '结合', '当前', '各种', '常见', '提供', '本科']

bg = imageio.imread('./imgs/bg.jpg')
w = wordcloud.WordCloud(width=1000,
                        height=700,
                        background_color='white',
                        font_path='./fonts/msyhl.ttc',
                        mask=bg,
                        scale=20,
                        stopwords=stopwords,
                        collocations=False,
                        max_font_size=120,
                        # contour_width=1,
                        # contour_color='yellow',
                        )

w.generate(nlp_job_list_words)
# tfidf
# w.generate_from_frequencies(keywords)
# img_color = ImageColorGenerator(bg)
# w_color = w.recolor(color_func=img_color)
w.to_file('nlpjobwcloud.png')
