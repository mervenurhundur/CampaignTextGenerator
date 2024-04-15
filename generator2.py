import streamlit as st
from openai import OpenAI

# OpenAI API client
openai_client = OpenAI()

# Streamlit uygulaması oluştur
st.title("Kampanya Metni Üretici")

# Kampanya konusu girişi al
campaign_topic = st.text_input("Kampanya Konusu")

if campaign_topic:
    # OpenAI modeline kampanya konusunu gönder
    response = openai_client.chat.completions.create(
        model="gpt-4-turbo-preview",  # veya "gpt-3.5-turbo" gibi bir model seç
        messages=[
            {"role": "system", "content": "Bu bir kampanya metni üretici."},
            {"role": "user", "content": campaign_topic}
        ]
    )

    # OpenAI modelinden gelen kampanya metnini göster
    campaign_text = response.choices[0].message.content
    st.write("Üretilen Kampanya Metni:")
    st.write(campaign_text)
