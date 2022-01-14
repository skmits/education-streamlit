import pandas as pd
import yfinance as yf
import altair as alt
import streamlit as st


# サイドバー
st.sidebar.write("""
# GAFA株価
こちらは株価可視化ツールです。以下のオプションから表示日数を指定できます。
""")

st.sidebar.write("""
# 表示日数選択
""")

days = st.sidebar.slider('日数', 1, 50, 20)

try:
    st.sidebar.write("""
    ## 株価の範囲指定
    """)

    ymin, ymax = st.sidebar.slider(
        '範囲を指定してください。', 0.0, 3500.0, (0.0, 3500.0)
        )

    # メイン画面
    st.title('米国株価可視化アプリ')

    st.write(f"""
    ### 過去**{days}日間**のGAFA株価 
    """)

    tickers = {
        'apple':'AAPL',
        'facebook':'FB',
        'google':'GOOGL',
        'microsoft':'MSFT',
        'netflix':'NFLX',
        'amazon':'AMZN'
    }

    @st.cache # データをキャッシュにためる（データ読み込みを早める）
    # 株価を表形式で取得
    def get_data(days,tickers):
        df = pd.DataFrame()
        for company in tickers.keys():

            # 株価を取得
            tkr = yf.Ticker(tickers[company])
            hist = tkr.history(period=f'{days}d')

            # 日付の形式変更
            hist.index = hist.index.strftime('%d %B %Y')

            # Close項目のみ使用して、項目名変更するよー
            hist = hist[['Close']]
            hist.columns = [company]

            # 行列の入れ替え
            hist = hist.T
            hist.index.name = 'Name'

            # 行の連結
            df = pd.concat([df, hist])
        return df

    df = get_data(days, tickers)

    companys = st.multiselect(
        '会社名を選択してください。',
        list(df.index),
        ['google', 'amazon', 'facebook', 'apple']
    )

    if not companys:
        st.error('少なくとも1社は選んでください！')
    else:
        # 株価を表形式で表示
        data = df.loc[companys]
        st.write("### 株価(USD)",data.sort_index())
        data = data.T.reset_index()
        # id_varsで指定した以外の項目を分割して表示する。
        data = pd.melt(data, id_vars=['Date'])
        data = data.rename(
            columns={'value':'Stock Prices(USD)'}
        )
        #グラフの作成
        chart = (
            alt.Chart(data)
            .mark_line(opacity=0.8, clip=True)
            .encode(
                x="Date:T",
                y=alt.Y("Stock Prices(USD):Q",stack=None, scale=alt.Scale(domain=[ymin, ymax])),
                color="Name:N"
            )
        )
        #グラフの表示
        st.altair_chart(chart, use_container_width=True)
except:
    st.error(
   "例外が発生しました。" 
   )