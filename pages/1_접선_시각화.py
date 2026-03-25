import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# 폰트 설정
font_path = 'font/NanumGothic-Bold.ttf'
fm.fontManager.addfont(font_path)
plt.rcParams['font.family'] = 'NanumGothic'

st.title("접선 시각화")
st.markdown("""
**접선 시각화 설명:**  
접선은 함수의 그래프 위의 한 점에서 그 점에서의 미분값(기울기)을 갖는 직선입니다.  
삼차함수 f(x) = ax³ + bx² + cx + d에 대해, 점 (a, f(a))에서의 접선은  
y - f(a) = f'(a)(x - a)로 표현됩니다.  
슬라이더를 움직여 다른 점에서의 접선을 확인해보세요!
""")

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

# a 초기화
if 'a' not in st.session_state:
    st.session_state.a = 0.0
else:
    st.session_state.a = float(st.session_state.a)

st.subheader("접선 점 선택")
col1, col2 = st.columns([3, 1])
with col1:
    st.session_state.a = st.slider("슬라이더:", -10.0, 10.0, st.session_state.a, step=0.1, key="a_slider")
with col2:
    st.session_state.a = st.number_input("직접 입력:", -10.0, 10.0, value=st.session_state.a, step=0.1, key="a_input")

a = st.session_state.a

# 점의 좌표
y_a = f(a)

# 접선 방정식: y - y_a = m(x - a), m = f_prime(a)
m = f_prime(a)

# 접선 함수
def tangent(x):
    return m*(x - a) + y_a

# 그래프 그리기
x_vals = np.linspace(-10, 10, 400)
y_vals = f(x_vals)
tangent_vals = tangent(x_vals)

fig, ax = plt.subplots()
ax.plot(x_vals, y_vals, label=f'f(x) = {a_coeff}x³ + {b_coeff}x² + {c_coeff}x + {d_coeff}')
ax.plot(x_vals, tangent_vals, label=f'접선 at x={a}', linestyle='--')
ax.scatter([a], [y_a], color='red', zorder=5)
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

# 접선 방정식 표시
y_a_fmt = format_num(y_a)
m_fmt = format_num(m)
b_fmt = format_num(y_a - m*a)
st.write(f"접선 방정식: y - {y_a_fmt} = {m_fmt}(x - {a})")
st.write(f"또는: y = {m_fmt}x + {b_fmt}")

# 계수 표시
st.write(f"함수 계수: a={a_coeff}, b={b_coeff}, c={c_coeff}, d={d_coeff}")
