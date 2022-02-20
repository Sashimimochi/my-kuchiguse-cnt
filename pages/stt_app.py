import streamlit as st
import plotly.graph_objs as go
import speech_recognition as sr

from modules.nlp import wakati, counter


def stt(filename):
    r = sr.Recognizer()
    with sr.AudioFile(filename) as source:
        audio = r.record(source)
    return r.recognize_google(audio, language='ja')


def app():
    st.markdown('## わたしのくちぐせカウンター')

    AUDIO_FILE = st.file_uploader(
        '音声ファイル(.wav)をアップロードしてね！', type='wav')
    st.audio(AUDIO_FILE, format="audio/wav", start_time=0)

    if st.button('文字書き起こし開始') and AUDIO_FILE:
        texts = stt(AUDIO_FILE)
        st.session_state['texts'] = texts
    texts = st.session_state['texts']
    st.markdown('文字書き起こしは重たい処理なので**必要な時だけ**押してね！')

    st.text_area('音声ファイルから書き起こした文章がここに表示されるよ！', texts , height=200, placeholder='音声ファイルから書き起こした文章がここに表示されるよ')

    n = st.number_input('回数が多い順に表示したい件数を入力してね！', value=10)
    pos = st.multiselect(
        '対象の品詞を選んでね！',
        ['名詞', '動詞', '形容詞', '助詞', '助動詞', '感動詞', '連体詞', '副詞', '接続詞', 'フィラー'],
        ['名詞', '動詞', '形容詞'],
        )
    words = wakati(texts, pos)
    df = counter(words)[-n:]

    fig = go.Figure()
    fig.add_trace(go.Bar(x=df.Count, y=df.Word, orientation='h'))
    fig.update_layout(
        title=dict(text=f'くちぐせカウンター 上位{n}件', x=0.5, xanchor='center'),
        width=1700, height=700,xaxis=dict(title='発言回数'),yaxis=dict(title='くちぐせ'))
    st.plotly_chart(fig, use_container_width=True)


def main():
    if ('texts' in st.session_state):
        app()
    else:
        st.session_state['texts'] = ''
        app()
