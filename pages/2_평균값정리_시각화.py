import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize
import matplotlib.font_manager as fm

# 폰트 설정
font_path = 'font/NanumGothic-Bold.ttf'
fm.fontManager.addfont(font_path)
plt.rcParams['font.family'] = 'NanumGothic'

st.title("삼차함수와 접선")

# 계수 초기화 (세션 유지)
if 'coeffs' not in st.session_state:
    st.session_state.coeffs = [np.random.randint(-5, 6) for _ in range(4)]

a_coeff, b_coeff, c_coeff, d_coeff = st.session_state.coeffs

# 새 함수 생성 버튼
if st.button("새 함수 생성"):
    st.session_state.coeffs = [np.random.randint(-5, 6) for _ in range(4)]
    st.rerun()

# 사용자 정의 함수 입력
st.subheader("사용자 정의 함수")
col1, col2, col3, col4 = st.columns(4)
with col1:
    a_input = st.number_input("a (x³ 계수)", value=a_coeff, step=1)
with col2:
    b_input = st.number_input("b (x² 계수)", value=b_coeff, step=1)
with col3:
    c_input = st.number_input("c (x 계수)", value=c_coeff, step=1)
with col4:
    d_input = st.number_input("d (상수)", value=d_coeff, step=1)

if st.button("사용자 정의 함수 적용"):
    st.session_state.coeffs = [a_input, b_input, c_input, d_input]
    st.rerun()

# 삼차함수 정의
def f(x):
    return a_coeff * x**3 + b_coeff * x**2 + c_coeff * x + d_coeff

def f_prime(x):
    return 3*a_coeff * x**2 + 2*b_coeff * x + c_coeff

# 숫자 포맷 함수
def format_num(n):
    if n == int(n):
        return str(int(n))
    else:
        s = f"{n:.2f}".rstrip('0').rstrip('.')
        return s

st.header("평균값 정리 시각화")
st.markdown("""
**평균값 정리 설명:**  
닫힌 구간 [x1, x2]에서 연속이고 열린 구간 (x1, x2)에서 미분 가능한 함수 f에 대해,  
f(x2) - f(x1) = f'(c)(x2 - x1)를 만족하는 c ∈ (x1, x2)가 적어도 하나 존재합니다.  
c 슬라이더를 움직여 f'(c)가 평균 기울기와 같아지는 점을 찾아보세요!
""")
x1 = st.slider("첫 번째 점 x1:", -10, 10, -2, key="x1_slider")
x2 = st.slider("두 번째 점 x2:", -10, 10, 2, key="x2_slider")

if x1 >= x2:
    st.error("x1은 x2보다 작아야 합니다.")
else:
    m_avg = (f(x2) - f(x1)) / (x2 - x1)
    st.write(f"두 점 사이 평균 기울기: {format_num(m_avg)}")

    c = st.slider("c점 찾기 (x1 < c < x2):", float(x1+0.1), float(x2-0.1), (x1+x2)/2.0, key="c_slider")
    m_c = f_prime(c)
    st.write(f"f'({format_num(c)}) = {format_num(m_c)}")

    diff = abs(m_c - m_avg)
    st.write(f"기울기 차이: {format_num(diff)}")

    if st.button("c점 정답 확인"):
        def equation(c_val):
            return f_prime(c_val) - m_avg
        try:
            from scipy.optimize import fsolve
            c_exact = fsolve(equation, (x1 + x2) / 2.0)[0]
            st.write(f"정답 c점: {format_num(c_exact)}")
        except:
            st.write("해를 찾을 수 없습니다.")

    # 그래프
    x_vals = np.linspace(-10, 10, 400)
    y_vals = f(x_vals)
    fig, ax = plt.subplots()
    ax.plot(x_vals, y_vals, label=f'f(x) = {a_coeff}x³ + {b_coeff}x² + {c_coeff}x + {d_coeff}')
    # 두 점 사이 직선
    ax.plot([x1, x2], [f(x1), f(x2)], 'g--', label='평균 기울기 선')
    # c에서의 접선
    tangent_c_vals = m_c * (x_vals - c) + f(c)
    ax.plot(x_vals, tangent_c_vals, 'r-', label=f'접선 at x={format_num(c)}')
    ax.scatter([x1, x2, c], [f(x1), f(x2), f(c)], color=['blue', 'blue', 'red'], zorder=5)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_xticks(range(-10, 11))
    # y축 범위 동적 설정 (삼차함수만 고려)
    ymin, ymax = y_vals.min(), y_vals.max()
    margin = (ymax - ymin) * 0.1 if ymax > ymin else 10
    ax.set_ylim(ymin - margin, ymax + margin)
    ax.legend()
    ax.grid(False)

    st.pyplot(fig)

# 계수 표시
st.write(f"함수 계수: a={a_coeff}, b={b_coeff}, c={c_coeff}, d={d_coeff}")
