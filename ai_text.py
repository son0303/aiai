import streamlit as st
import os
from openai import OpenAI
os.environ["OPENAI_API_KEY"] = "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"
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)

# 앱 제목
st.title("오늘의 술을 추천해드릴게요😊😃 !")

#기분 입력하기
mood = st.text_input("오늘의 기분이 어떠신가요?")

#출력
if st.button("술 추천받기"):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": mood,
            },
            {
                "role": "system",
                "content": "입력 된 기분에 어울리는 술의 종류랑 그 종류에 맞는 술의 종류를 각각 추천해주고 그 술을 설명해주고 추천 이유도 알려줘",
            }
        ],
        model="gpt-4o",
    )
    
    response = client.images.generate(
        model="dall-e-3",
        prompt="바텐더 일러스트를 그려줘",
        size="1024x1024",
        quality="standard",
        n=1,
    )
    result = chat_completion.choices[0].message.content
    
    image_url = response.data[0].url
    
    st.write(result)
    st.image(image_url)
