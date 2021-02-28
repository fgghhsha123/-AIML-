import aiml_bot

bot = aiml_bot.Bot(learn='E:\\机器学习\\自然语言处理实战\\code\\chap12\\基于 AIML 的模式匹配聊天机器人\\greeting_step1.aiml')
# AIML 规范巧妙地忽略了标点符号和大小写
# 但是 AIML 1.0 规范只规范化模式的词结尾的标点符号，而不是词之间和词内部；
# 词之间的空白符，而不是词内部
print("Hello Rosa,:", bot.respond("Hello Rosa,"))
print("hello troll!!!:", bot.respond("hello troll!!!"))
print("hello ! troll!!!:", bot.respond("hello ! troll!!!"))
print("hello !!!troll!!!:", bot.respond("hello !!!troll!!!"))
print("hello **troll:", bot.respond("hello **troll"))
# 它无法处理同义词、拼写错误、带连字符的词或复合词
print("Helo Rosa:", bot.respond("Helo Rosa"))
print("Hello Ro-sa:", bot.respond("Hello Ro-sa"))

# 加载一个附加的 AIML，机器人就可以识别出“Hello”的几种不同的说法和错误拼写形式
bot.learn('E:\\机器学习\\自然语言处理实战\\code\\chap12\\基于 AIML 的模式匹配聊天机器人\\greeting_step2.aiml')
print("Hey Rosa:", bot.respond("Hey Rosa"))
print("Hi Rosa:", bot.respond("Hi Rosa"))
print("Helo Rosa:", bot.respond("Helo Rosa"))
print("HY troll!:", bot.respond("HY troll!"))
print("WHAT IS UP troll!:", bot.respond("WHAT IS UP troll!"))
print("hello **troll** !!!:", bot.respond("hello **troll** !!!"))
print("hello !! troll!!!:", bot.respond("hello !!!troll!!!"))

# 使用<random>标签来帮助机器人在回复问候时显得更有创意一点儿
# 每次匹配模式时，它都会从列表中随机选择一个回复，无法在 aiml_bot 中设置随机种子
bot.learn('E:\\机器学习\\自然语言处理实战\\code\\chap12\\基于 AIML 的模式匹配聊天机器人\\greeting_step3.aiml')
print("Hey Rosa:", bot.respond("Hey Rosa"))
print("Hey Rosa:", bot.respond("Hey Rosa"))
print("Hey Rosa:", bot.respond("Hey Rosa"))