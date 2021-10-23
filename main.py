import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time 

# プログレスバーの作成（ダウンロードバーみたいなやつ）

st.write('start')

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'表示まで {100-(i+1)} 秒')
    bar.progress(i + 1)
    time.sleep(1)

st.write('Yeah!!')

'''
# エクスパンダーの作成
expander = st.expander('問合せ')
expander.write('問合せ内容１')
expander.write('問合せ内容２')

# 2カラム表示　(説明ではst.beta_columnsだけどなくなったらしい)
left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')

if button:
    right_column.write('ここは右カラムです。')

# サイドバー
sidebara = st.sidebar.text_input('A')
sidebarb = st.sidebar.slider('B', 0 ,100, 50)

st.write('サイドバーで文字入力してください',sidebara)
st.write('サイドバーで指定してください',sidebarb)

# スライダーを作成
com = st.slider('あなたの今の調子は？', 0 ,100, 50)

st.write('コンディションは', com, 'です。')

# テキスト入力
text = st.text_input('あなたの趣味を教えてください。')

st.write('あなたの趣味は', text, 'です。')

# セレクトボックスを作成
option = st.selectbox(
    'あなたが好きな数字を教えてください。',
    list(range(1,11))
)

st.write('あなたの好きな数字は', option, 'です。')

# チェックボックスで画像の表示有無を判断
if st.checkbox('Show Image'):
    # 画像の表示
    # use_column_width：trueの時、Webの表示可能幅に合わせて表示される
    img = Image.open('a.png')
    st.image(img, caption='A img', use_column_width=True)

# 文字を表示したいとき
st.title('Streamlit 超入門')

# 文字や表を表示したいとき（引数は受け付けない）
st.write('DataFrame')

df = pd.DataFrame(
    np.random.rand(20, 3),
    columns=['a', 'b', 'c']
)

dfmp = pd.DataFrame(
    np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
    columns=['lat', 'lon']
)

# 地図上にマッピングする
st.map(dfmp)

# 折れ線グラフで表示（塗りつぶしなし）
st.line_chart(df)

# 折れ線グラフで表示（塗りつぶしあり）
st.area_chart(df)

# 棒グラフで表示
st.bar_chart(df)

# 表表示において、引数を指定したいとき（ソート機能も付与される）
st.dataframe(df.style.highlight_max(axis=0), width=1000, height=1000)

# 表表示したいとき（ソート機能等の動的処理なし）
st.table(df.style.highlight_max(axis=0))

# マークダウン記法（見出し等を表示する）
"""
# 章
## 節
### 項
"""

# マークダウン記法(pythonのコードを表示させる)
"""

```python
import streamlit as st
import numpy as np
import pandas as pd
```
"""

'''