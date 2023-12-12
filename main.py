import pandas as pd
import streamlit as st
import plotly_express as px


st.title('Приложение, которое хотело бы быть красивее')

df = st.cache_data(pd.read_csv)('dataset.csv')

st.header('Графики распределения')

columns = ['TARGET','AGE','GENDER','CHILD_TOTAL','DEPENDANTS','SOCSTATUS_WORK_FL','SOCSTATUS_PENS_FL','LOAN_NUM_TOTAL','LOAN_NUM_CLOSED','PERSONAL_INCOME']
for col in columns:
    fig = px.histogram(df, x=col, title="Distribution of {}".format(col))
    st.plotly_chart(fig)

st.header('Графики распределения с разбиением по таргету')

for col in columns[1:]:
    fig = px.histogram(df, x=col, color='TARGET', title="Distribution of {} by TARGET".format(col))
    st.plotly_chart(fig)

st.header('Корреляционный heatmap')

corr_matrix = df[columns].corr()
fig = px.imshow(corr_matrix)
st.plotly_chart(fig)

st.header('Графики зависимости')

columns = ['AGE','CHILD_TOTAL','DEPENDANTS','LOAN_NUM_TOTAL','LOAN_NUM_CLOSED','PERSONAL_INCOME']
for col in columns:
    fig = px.scatter(df, x=col, y='TARGET', title="Pairs of TARGET and {}".format(col))
    st.plotly_chart(fig)

st.header('Основные статистики')

status = st.radio('Укажите интересующий столбец: ', ('AGE','CHILD_TOTAL','DEPENDANTS','LOAN_NUM_TOTAL','LOAN_NUM_CLOSED','PERSONAL_INCOME'))
if (status == 'AGE'):
    st.text('Среднее:{}'.format(df['AGE'].mean()))
    st.text('Медиана:{}'.format(df['AGE'].median()))
    st.text('Стандартное отклонение:{}'.format(df['AGE'].std()))
    st.text('Минимум:{}'.format(df['AGE'].min()))
    st.text('Максимум:{}'.format(df['AGE'].max()))
elif (status == 'CHILD_TOTAL'):
    st.text('Среднее:{}'.format(df['CHILD_TOTAL'].mean()))
    st.text('Медиана:{}'.format(df['CHILD_TOTAL'].median()))
    st.text('Стандартное отклонение:{}'.format(df['CHILD_TOTAL'].std()))
    st.text('Минимум:{}'.format(df['CHILD_TOTAL'].min()))
    st.text('Максимум:{}'.format(df['CHILD_TOTAL'].max()))
elif (status == 'DEPENDANTS'):
    st.text('Среднее:{}'.format(df['DEPENDANTS'].mean()))
    st.text('Медиана:{}'.format(df['DEPENDANTS'].median()))
    st.text('Стандартное отклонение:{}'.format(df['DEPENDANTS'].std()))
    st.text('Минимум:{}'.format(df['DEPENDANTS'].min()))
    st.text('Максимум:{}'.format(df['DEPENDANTS'].max()))
elif (status == 'LOAN_NUM_TOTAL'):
    st.text('Среднее:{}'.format(df['LOAN_NUM_TOTAL'].mean()))
    st.text('Медиана:{}'.format(df['LOAN_NUM_TOTAL'].median()))
    st.text('Стандартное отклонение:{}'.format(df['LOAN_NUM_TOTAL'].std()))
    st.text('Минимум:{}'.format(df['LOAN_NUM_TOTAL'].min()))
    st.text('Максимум:{}'.format(df['LOAN_NUM_TOTAL'].max()))
elif (status == 'LOAN_NUM_CLOSED'):
    st.text('Среднее:{}'.format(df['LOAN_NUM_CLOSED'].mean()))
    st.text('Медиана:{}'.format(df['LOAN_NUM_CLOSED'].median()))
    st.text('Стандартное отклонение:{}'.format(df['LOAN_NUM_CLOSED'].std()))
    st.text('Минимум:{}'.format(df['LOAN_NUM_CLOSED'].min()))
    st.text('Максимум:{}'.format(df['LOAN_NUM_CLOSED'].max()))
elif (status == 'PERSONAL_INCOME'):
    st.text('Среднее:{}'.format(df['PERSONAL_INCOME'].mean()))
    st.text('Медиана:{}'.format(df['PERSONAL_INCOME'].median()))
    st.text('Стандартное отклонение:{}'.format(df['PERSONAL_INCOME'].std()))
    st.text('Минимум:{}'.format(df['PERSONAL_INCOME'].min()))
    st.text('Максимум:{}'.format(df['PERSONAL_INCOME'].max()))
