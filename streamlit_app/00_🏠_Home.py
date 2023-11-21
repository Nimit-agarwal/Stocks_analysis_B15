import streamlit as st

st.set_page_config(
    page_title="Stock Analysis App",
    page_icon="😎",
)

st.markdown("""
<style>
body {
    font-family: 'Comic Sans MS', sans-serif;
    font-size: 20px;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
## Stock Prediction Application Highlights

1. **Purpose**: The application is designed for **stock prediction**, providing accurate and timely predictions to aid investment decisions.
2. **Methodology**: It uses **Auto Regression**, a statistical method that predicts future values based on time-lagged historical data.
3. **Platform**: The application is built on **Streamlit**, chosen for its user-friendly interface and ease of use.
4. **Functionality**: Users can select any publicly traded company, choose a date range for historical data, and receive a prediction for future stock prices.
5. **Visualization**: The application provides visualizations of the historical data and predicted values for better understanding.
6. **Target Audience**: It is a valuable tool for investors, financial analysts, and anyone interested in the stock market.
7. **User Engagement**: Users are invited to try it out and see how it can enhance their investment strategy.
8. **Future Updates**: More updates and features are to be expected in the future.
9. **Disclaimer**: A disclaimer is provided that while the model strives for accuracy, stock market predictions are inherently uncertain and should not be the sole basis for investment decisions. Users are advised to consult with a financial advisor or conduct their own research when investing in the stock market.
""")

