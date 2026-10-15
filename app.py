import streamlit as st

st.set_page_config(page_title="海外決済比較アプリ", page_icon="💱")
st.title("💱 海外決済比較アプリ")
st.write("タイバーツでの支払いを日本円に換算し、WiseとRevolutを比較します。")
st.caption("為替レートと手数料は練習用の仮定値です。実際の各社の条件ではありません。")

baht = st.number_input("支払額（タイバーツ）", min_value=0.0, value=1000.0, step=100.0)
col1, col2 = st.columns(2)
with col1:
    st.subheader("Wise")
    wise_rate = st.number_input("レート（円/バーツ）", min_value=0.0, value=4.70, step=0.01, format="%.3f", key="wise_rate")
    wise_fee = st.number_input("手数料（%）", min_value=0.0, value=0.5, step=0.1, key="wise_fee")
with col2:
    st.subheader("Revolut")
    revolut_rate = st.number_input("レート（円/バーツ）", min_value=0.0, value=4.72, step=0.01, format="%.3f", key="revolut_rate")
    revolut_fee = st.number_input("手数料（%）", min_value=0.0, value=0.0, step=0.1, key="revolut_fee")

if st.button("比較する", type="primary", use_container_width=True):
    wise_yen = baht * wise_rate * (1 + wise_fee / 100)
    revolut_yen = baht * revolut_rate * (1 + revolut_fee / 100)
    st.metric("Wiseの支払額", f"{wise_yen:,.2f} 円")
    st.metric("Revolutの支払額", f"{revolut_yen:,.2f} 円")
    if abs(wise_yen - revolut_yen) < 0.005:
        st.info("ほぼ同額です。")
    elif wise_yen < revolut_yen:
        st.success("Wiseの方が有利です。")
    else:
        st.success("Revolutの方が有利です。")
    st.write(f"差額：**{abs(wise_yen - revolut_yen):,.2f} 円**")
