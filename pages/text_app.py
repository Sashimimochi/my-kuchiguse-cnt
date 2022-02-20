# -*- coding: utf-8 -*-

import streamlit as st
import plotly.graph_objs as go

from modules.nlp import wakati, counter


def main():

    st.markdown('## わたしのくちぐせカウンター')

    texts = st.text_area('くちぐせを数えたいテキストを入力してね！Ctrl＋Enterで分析開始だよ！',
                        '''私はその人を常に先生と呼んでいた。
だからここでもただ先生と書くだけで本名は打ち明けない。
これは世間を憚はばかる遠慮というよりも、その方が私にとって自然だからである。
私はその人の記憶を呼び起すごとに、すぐ「先生」といいたくなる。
筆を執とっても心持は同じ事である。よそよそしい頭文字かしらもじなどはとても使う気にならない。
(夏目漱石 こころ - 青空文庫より)''',
                        height=400, placeholder='くちぐせを数えたいテキストを入力してね！')

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
