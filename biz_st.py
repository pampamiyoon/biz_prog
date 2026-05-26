import streamlit as st #streamlit 라이브러리 임포트
import numpy as np

#타이틀 텍스트 출력
st.title('첫번째 웹 어플 만들기') 
"#첫번째 웹 어플 만들기"
st.write('# 1. 마크다운 텍스트 작성하기')
st.write('안녕')

"""
#비즈니스 모델 분석

[네이버](http://www.naver.com)  
[홍익대학교](https://www.hongik.ac.kr)

이것이 일반 본문 **이것이 굵은 글씨** *이것이 기울임 글씨* ~이것이 취소선~

:red[빨간색 글씨] :green[초록색 글씨] :blue[파란색 글씨]

```
print("코드블록")
```

"""

st.caption('캡션(작고 흐린 글씨로 표현됨)')

with st.echo():
    # 이 블록의 코드와 결과를 출력
    name = 'Chunghun Ha'
    st.write("Helllo,streamlit", name)

st.latex('\int_a^b f(x)dx')
"$$\int_a^b f(x)dx$$"

'# :blue[데이터 테이블]'

'#### :orange[Pandas 데이터 프레임]'
import pandas as pd
df=pd.DataFrame(
    {'id':[1,2,3],
     'name':['Alice','Bob','Charlie'],
     'age':[24,34,45]
     }
)
df # 데이터프레임 출력

st.metric("Temperature","70°F","-1.2°F")

'#### :orange[지표(Metric)]'
col1, col2, col3 = st.columns(3) #3개의 컬럼 생성
col1.metric("Temperature","70°F","1.2°F")
col1.write("이것은 온도 지표입니다.")
col2.metric("Wind","9 mph","-8%")
col3.metric("Humidity","86%","4%")



'#### :orange[이미지:st.image()]'

st.image("./data/python_설명.jpeg", caption="파이썬 로고", width=500)

'#### :orange[오디오:st.audio()]'

st.audio("./data/moodmode.mp3", format="audio/mpeg", loop=True)

'#### :orange[동영상:]'