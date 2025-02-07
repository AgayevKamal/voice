import streamlit as st
import pyttsx3

# Pyttsx3 motorunu başlat
engine = pyttsx3.init()

# Streamlit interfeysi
st.title("Mətni Səsli Formada Oxuma Tətbiqi")

# İstifadəçi mətn daxil edir
text_input = st.text_area("Oxunacaq mətni daxil edin:")

# Oxuma sürətini və səsi tənzimləmək
rate = st.slider("Oxuma sürəti (Standart: 200)", min_value=100, max_value=300, value=200)
volume = st.slider("Səs səviyyəsi (0.0 ilə 1.0 arası)", min_value=0.0, max_value=1.0, value=0.9)

# Tənzimləmələri tətbiq et
engine.setProperty('rate', rate)
engine.setProperty('volume', volume)

# Səsli cavab düyməsi
if st.button("Oxu"):
    if text_input:
        engine.say(text_input)
        engine.runAndWait()
    else:
        st.warning("Zəhmət olmasa mətn daxil edin!")