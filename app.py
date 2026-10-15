import streamlit as st

st.set_page_config(page_title="海外決済比較アプリ", page_icon="💱")
st.title("💱 海外決済比較アプリ")
st.write("タイバーツの支払いについて、Wise・Revolut・現金両替を比較します。")
st.caption("レートと手数料は練習用の仮定値です。実際の適用条件ではありません。")

baht = st.number_input("支払額（タイバーツ）", min_value=0.0, value=1000.0, step=100.0)

with st.expander("Wiseの条件", expanded=True):
    wise_rate = st.number_input("1バーツあたりの円", min_value=0.0, value=4.70, step=0.01, format="%.3f", key="wise_rate")
    wise_fee = st.number_input("追加手数料（%）", min_value=0.0, value=0.5, step=0.1, key="wise_fee")
with st.expander("Revolutの条件", expanded=True):
    revolut_rate = st.number_input("1バーツあたりの円", min_value=0.0, value=4.72, step=0.01, format="%.3f", key="revolut_rate")
    revolut_fee = st.number_input("追加手数料（%）", min_value=0.0, value=0.0, step=0.1, key="revolut_fee")
with st.expander("現金両替の条件", expanded=True):
    cash_rate = st.number_input("1バーツあたりの円", min_value=0.0, value=4.75, step=0.01, format="%.3f", key="cash_rate")
    cash_fee = st.number_input("追加手数料（%）", min_value=0.0, value=0.0, step=0.1, key="cash_fee")

results = {
    "Wise": baht * wise_rate * (1 + wise_fee / 100),
    "Revolut": baht * revolut_rate * (1 + revolut_fee / 100),
    "現金両替": baht * cash_rate * (1 + cash_fee / 100),
}
st.subheader("比較結果（入力すると自動更新）")
for name, yen in sorted(results.items(), key=lambda x: x[1]):
    st.metric(name, f"{yen:,.2f} 円")
minimum = min(results.values())
winners = [name for name, yen in results.items() if abs(yen - minimum) < 0.005]
if len(winners) == 3:
    st.info("3種類ともほぼ同額です。")
else:
    st.success("最も安い方法：" + "・".join(winners))
st.write(f"最高額との差：**{max(results.values()) - minimum:,.2f} 円**")
st.caption("この計算は入力したレートに追加手数料を上乗せする単純モデルです。現金の入手費用やカードの条件などは別途考慮してください。")
