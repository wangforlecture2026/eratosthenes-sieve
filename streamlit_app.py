import streamlit as st

def factorize(n):
    if n <= 1:
        return []
    factors = []
    i = 2
    while i * i <= n:
        if n % i == 0:
            factors.append(i)
            while n % i == 0:
                n //= i
        i += 1
    if n > 1:
        factors.append(n)
    return factors

st.title("에라토스테네스의 체 체험하기")

if 'started' not in st.session_state:
    st.session_state.started = False
    st.session_state.n = 0
    st.session_state.numbers = []
    st.session_state.message = ""
    st.session_state.factors = []

n_input = st.number_input("숫자를 입력하세요 (2 이상):", min_value=2, step=1, value=10)

if st.button("에라토스테네스의 체 시작하기"):
    st.session_state.started = True
    st.session_state.n = n_input
    st.session_state.numbers = list(range(1, n_input + 1))
    st.session_state.message = ""
    st.session_state.factors = factorize(n_input)

if st.session_state.started:
    st.write(f"1부터 {st.session_state.n}까지의 숫자들:")
    
    cols = st.columns(10)  # 10열로 버튼 배치
    for i, num in enumerate(st.session_state.numbers):
        col = cols[i % 10]
        if col.button(str(num), key=f"btn_{num}"):
            # 배수 제거
            multiples = [j for j in st.session_state.numbers if j % num == 0 and j != num and j != 1]
            for m in multiples:
                if m in st.session_state.numbers:
                    st.session_state.numbers.remove(m)
            # 메시지 업데이트
            if st.session_state.n not in st.session_state.numbers:
                st.session_state.message = f"{st.session_state.n}은 합성수입니다. 소인수분해: {' × '.join(map(str, st.session_state.factors))}"
            else:
                st.session_state.message = f"{st.session_state.n}은 소수입니다."
    
    if st.session_state.message:
        st.success(st.session_state.message)
    
    if st.button("초기화"):
        st.session_state.started = False
        st.session_state.n = 0
        st.session_state.numbers = []
        st.session_state.message = ""
        st.session_state.factors = []
        st.rerun()
