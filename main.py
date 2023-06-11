import streamlit as st
from PIL import Image

heatmap_corr_1 = Image.open("heatmap_corr_1.png")
graph_corr_1 = Image.open("graph_corr_1.png")
heatmap_corr_2 = Image.open("heatmap_corr_2.png")
graph_corr_2 = Image.open("graph_corr_2.png")
heatmap_dtw_1 = Image.open("heatmap_dtw_1.png")
heatmap_dtw_2 = Image.open("heatmap_dtw_2.png")
weights_hist = Image.open("weights_hist.png")
pf_values = Image.open("pf_values.png")

st.set_page_config(page_title = "",layout = "wide")

st.subheader("Проект по питону")
st.title("Кластеризация акций и создание на ее основе портфеля")
st.write("##")
st.write("В совем проекте я кластеризую акции двумя различными способами и строю на основе кластеризации портфели (HRP), которые сравниваю с т.н. 'эффективным' портфелем")

with st.container():
    st.write("---")
    st.write("##")
    l_column, r_column = st.columns(2)
    with l_column:
        st.write("До кластериазции (на основе корреляций), акции были неупорядочены.")
        st.write("Это можно увидеть на приведенных графиках графиках (графф корреляции и тепловая карта).")
        st.write("В принципе доасточно легко заметить, что данные абсолютно неструктурированы.")
        st.write("##")
        st.image(graph_corr_1)  
    with r_column:
        st.image(heatmap_corr_1)
    
with st.container():
    st.write("---")
    st.write("##")
    l_column, r_column = st.columns(2)
    with l_column:
        st.write("После кластеризации можем наблюдать следущую картину:")
        st.write("Как видно, акции теперь составляют отдельные блоки")
        st.image(graph_corr_2)  
    with r_column:
        st.image(heatmap_corr_2)

with st.container():
    st.write("---")
    st.write("##")
    st.write("Аналогично можно кластеризовать на основе dtw:")
    l_column, r_column = st.columns(2)
    with l_column:
        st.image(heatmap_dtw_1)  
    with r_column:
        st.image(heatmap_dtw_2)

with st.container():
    st.write("---")
    st.write("##")
    st.write("На основе данных кластеризаций можно получить веса.")
    st.write("Как можно заметить, портфель гораздо более диверсифицированный по сравнению с tangency портфелем.")
    st.image(weights_hist)

with st.container():
    st.write("---")
    st.write("##")
    st.write("Полученные портфели тестируем на исторических данных (с ежегодной перебалансировкой).")
    st.write("HRP портфели показывают более высокую доходность (за весь период), и значительно меньшую волатильность")
    st.image(pf_values)