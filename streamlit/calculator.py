import streamlit as st

st.set_page_config(page_title="Calculator", page_icon="🧮", layout="centered")

st.markdown("""
<style>
    .main { background-color: #1a1a2e; }
    .stApp { background-color: #1a1a2e; }

    .calc-container {
        background: linear-gradient(145deg, #16213e, #0f3460);
        border-radius: 20px;
        padding: 30px;
        box-shadow: 0 20px 60px rgba(0,0,0,0.5);
        max-width: 380px;
        margin: 20px auto;
    }

    .display-box {
        background: #0d0d1a;
        border-radius: 12px;
        padding: 20px;
        margin-bottom: 20px;
        border: 1px solid #e94560;
        text-align: right;
    }

    .expression {
        color: #a0a0c0;
        font-size: 14px;
        min-height: 20px;
        font-family: 'Courier New', monospace;
    }

    .result {
        color: #ffffff;
        font-size: 42px;
        font-weight: bold;
        font-family: 'Courier New', monospace;
        word-break: break-all;
    }

    .history-box {
        background: #0d0d1a;
        border-radius: 12px;
        padding: 15px;
        margin-top: 20px;
        border: 1px solid #333;
        max-height: 180px;
        overflow-y: auto;
    }

    .history-item {
        color: #a0a0c0;
        font-size: 13px;
        font-family: 'Courier New', monospace;
        padding: 4px 0;
        border-bottom: 1px solid #1e1e3a;
    }

    div[data-testid="column"] button {
        width: 100% !important;
        height: 65px !important;
        font-size: 20px !important;
        font-weight: 600 !important;
        border-radius: 12px !important;
        border: none !important;
        cursor: pointer !important;
        transition: all 0.15s ease !important;
    }

    /* Number buttons */
    div[data-testid="column"]:nth-child(n) button[kind="secondary"] {
        background: #1e2d5a !important;
        color: #ffffff !important;
    }

    .stButton > button {
        width: 100%;
        height: 65px;
        font-size: 20px;
        font-weight: 700;
        border-radius: 12px;
        border: none;
        transition: transform 0.1s ease, box-shadow 0.1s ease;
    }

    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(233, 69, 96, 0.4);
    }

    .stButton > button:active {
        transform: translateY(0px);
    }

    h1 { color: #e94560 !important; text-align: center; }
    h4 { color: #a0a0c0 !important; }
    p  { color: #a0a0c0 !important; }
</style>
""", unsafe_allow_html=True)

# --- State ---
if "expression" not in st.session_state:
    st.session_state.expression = ""
if "display" not in st.session_state:
    st.session_state.display = "0"
if "history" not in st.session_state:
    st.session_state.history = []
if "just_evaluated" not in st.session_state:
    st.session_state.just_evaluated = False

def press(val):
    ops = {"+", "-", "×", "÷", "%"}

    if val == "C":
        st.session_state.expression = ""
        st.session_state.display = "0"
        st.session_state.just_evaluated = False

    elif val == "⌫":
        st.session_state.expression = st.session_state.expression[:-1]
        st.session_state.display = st.session_state.expression or "0"
        st.session_state.just_evaluated = False

    elif val == "=":
        if st.session_state.expression:
            try:
                expr = (st.session_state.expression
                        .replace("×", "*")
                        .replace("÷", "/")
                        .replace("%", "/100"))
                result = eval(expr)
                result = int(result) if isinstance(result, float) and result.is_integer() else round(result, 10)
                st.session_state.history.append(f"{st.session_state.expression} = {result}")
                st.session_state.display = str(result)
                st.session_state.expression = str(result)
                st.session_state.just_evaluated = True
            except ZeroDivisionError:
                st.session_state.display = "Cannot ÷ by 0"
                st.session_state.expression = ""
            except Exception:
                st.session_state.display = "Error"
                st.session_state.expression = ""

    elif val == "+/-":
        if st.session_state.expression:
            try:
                result = eval(st.session_state.expression.replace("×", "*").replace("÷", "/"))
                result = -result
                st.session_state.expression = str(result)
                st.session_state.display = str(result)
            except Exception:
                pass

    else:
        if st.session_state.just_evaluated and val not in ops:
            st.session_state.expression = ""
            st.session_state.just_evaluated = False

        if val in ops and st.session_state.expression and st.session_state.expression[-1] in ops:
            st.session_state.expression = st.session_state.expression[:-1]

        st.session_state.expression += val
        st.session_state.display = st.session_state.expression
        if val not in ops:
            st.session_state.just_evaluated = False

# --- UI ---
st.markdown("<h1>🧮 Calculator</h1>", unsafe_allow_html=True)

# Display
expr_html = st.session_state.expression if st.session_state.expression else "&nbsp;"
display_val = st.session_state.display

st.markdown(f"""
<div class="calc-container">
  <div class="display-box">
    <div class="expression">{expr_html}</div>
    <div class="result">{display_val}</div>
  </div>
</div>
""", unsafe_allow_html=True)

# Button layout
buttons = [
    ["C",   "+/-", "%",  "÷"],
    ["7",   "8",   "9",  "×"],
    ["4",   "5",   "6",  "-"],
    ["1",   "2",   "3",  "+"],
    ["⌫",  "0",   ".",  "="],
]

OPERATOR_STYLE = "background-color:#e94560; color:white;"
FUNC_STYLE     = "background-color:#533483; color:white;"
EQUAL_STYLE    = "background-color:#e94560; color:white;"
NUM_STYLE      = "background-color:#1e2d5a; color:white;"

def get_style(v):
    if v in {"÷", "×", "-", "+"}:
        return OPERATOR_STYLE
    if v in {"C", "+/-", "%", "⌫"}:
        return FUNC_STYLE
    if v == "=":
        return EQUAL_STYLE
    return NUM_STYLE

for row in buttons:
    cols = st.columns(len(row))
    for col, val in zip(cols, row):
        with col:
            style = get_style(val)
            if st.button(val, key=f"btn_{val}_{row.index(val)}", use_container_width=True):
                press(val)
                st.rerun()

# History
if st.session_state.history:
    st.markdown("---")
    st.markdown("<h4>📋 History</h4>", unsafe_allow_html=True)
    items = "".join(
        f'<div class="history-item">{h}</div>'
        for h in reversed(st.session_state.history[-10:])
    )
    st.markdown(f'<div class="history-box">{items}</div>', unsafe_allow_html=True)

    if st.button("Clear History", use_container_width=True):
        st.session_state.history = []
        st.rerun()
