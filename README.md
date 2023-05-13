# openai

### Example:
```
$Env:OPENAI_API_KEY = 'xxxxx'
python test.py
python test_chinese.py
```

### Result (test.py):
```
===== OpenAI Prompt =====

The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.

Human: Hello, who are you?

AI: I am an AI created by OpenAI. How can I help you today?

Human: Who is the highest scorer of all time in NBA history?

AI: The highest scorer of all time in NBA history is Kareem Abdul-Jabbar, who scored 38,387 points during his career.
```

### Result (test_chinese.py):
```
Human: 寫一篇新詩，內容含有 "微軟"

AI:

微軟給我們帶來力量
讓虛擬世界翩然起舞
爭取平等為每個人樹立典範
創新無所不在凝聚未來

技術和永續於新技術下崛起
創造對人類有益的影


Human: 寫一篇新詩，內容含有 "郭台銘"

AI:

獨樹一帜的郭台銘，
追求夢想不停歇；
他的勇氣與堅毅，
打造出一片新天地；
輝煌的成就令人嘆服，
優雅中展現他的精神。
職場當中挑戰重重，
別無


Human: 寫一篇新詩，內容含有 "烏克麗麗"

AI: 

烏克麗麗是我的歌聲，
心中把它永恆記著。
它的旋律像漣漪，
帶著無淚的幸福歡笑。

每一個節奏都如夢之中，
那樂聲萬千尋寻。
它彷彿在詠唱，
```

### References:

1. https://vocus.cc/article/6393d4aafd89780001952fce
2. https://platform.openai.com/docs/api-reference/chat?lang=python