import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# 폰트 설정
font_path = 'font/NanumGothic-Bold.ttf'
fm.fontManager.addfont(font_path)
plt.rcParams['font.family'] = 'NanumGothic'

st.set_page_config(page_title="미분불가능 함수와 평균값정리", layout="wide")

st.title("⚠️ 미분불가능 함수에서 평균값정리의 실패")

st.markdown("""
## 평균값정리가 성립하지 않는 경우

평균값정리는 **미분가능성**이 필수 조건입니다. 아래는 미분불가능한 함수들의 예시입니다.

### 📌 예시 1: 절댓값 함수 (꺾인 점)
""")

# 예시 1: 절댓값 함수
col1, col2 = st.columns([2, 1])
with col1:
    st.markdown("**f(x) = |x|**")
    st.markdown("""
    - x = 0에서 미분불가능 (좌미분계수 ≠ 우미분계수)
    - 좌미분계수: -1
    - 우미분계수: +1
    """)
with col2:
    st.info("문제점: 구간 [-2, 2]에서 x=0에서 미분 불가능")

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# 절댓값 함수
x_vals = np.linspace(-3, 3, 200)
y_vals = np.abs(x_vals)

ax = axes[0]
ax.plot(x_vals, y_vals, 'b-', linewidth=2.5, label='f(x) = |x|')

# 구간 [-2, 2]
x1, x2 = -2, 2
m_avg = (np.abs(x2) - np.abs(x1)) / (x2 - x1)  # (2 - 2) / 4 = 0

# 할선
ax.plot([x1, x2], [np.abs(x1), np.abs(x2)], 'g--', linewidth=2, label=f'할선 (기울기 = 0)')

# 점 표시
ax.scatter([x1, x2], [np.abs(x1), np.abs(x2)], color='green', s=100, zorder=5)
ax.scatter([0], [0], color='red', s=150, zorder=5, marker='x', linewidths=3, label='미분불가능 점 (x=0)')

# 좌미분선, 우미분선
ax.plot([-2, 0], [2, 0], 'r:', linewidth=2, alpha=0.7, label='좌미분 (기울기 = -1)')
ax.plot([0, 2], [0, 2], 'orange', linestyle=':', linewidth=2, alpha=0.7, label='우미분 (기울기 = +1)')

ax.set_xlabel('x', fontsize=11)
ax.set_ylabel('y', fontsize=11)
ax.set_xlim(-3, 3)
ax.set_ylim(-0.5, 3.5)
ax.grid(True, alpha=0.3)
ax.legend(fontsize=9)
ax.set_title('예시 1: 절댓값 함수 |x|', fontsize=12, fontweight='bold')

# 문제 설명
ax = axes[1]
ax.text(0.5, 0.9, 'x = 0에서의 상황', ha='center', va='top', fontsize=12, fontweight='bold', transform=ax.transAxes)
ax.text(0.5, 0.75, '• 함수는 연속이다 (조건 만족)', ha='center', va='top', fontsize=10, transform=ax.transAxes)
ax.text(0.5, 0.65, '• 하지만 x=0에서 미분불가능', ha='center', va='top', fontsize=10, transform=ax.transAxes, color='red', fontweight='bold')
ax.text(0.5, 0.55, '  (좌미분계수 ≠ 우미분계수)', ha='center', va='top', fontsize=9, transform=ax.transAxes)

ax.text(0.5, 0.4, '평균값정리 조건:', ha='center', va='top', fontsize=11, fontweight='bold', transform=ax.transAxes, 
        bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.7))
ax.text(0.5, 0.3, '✓ [−2, 2]에서 연속', ha='center', va='top', fontsize=10, transform=ax.transAxes, color='green')
ax.text(0.5, 0.2, '✗ (−2, 2)에서 미분가능하지 않음', ha='center', va='top', fontsize=10, transform=ax.transAxes, color='red', fontweight='bold')

ax.text(0.5, 0.05, '결론: 평균값정리가 적용되지 않음!', ha='center', va='top', fontsize=11, fontweight='bold', 
        transform=ax.transAxes, bbox=dict(boxstyle='round', facecolor='lightcoral', alpha=0.7))

ax.axis('off')

st.pyplot(fig)

st.markdown("""
---
### 📌 예시 2: 분수 함수 (무한 불연속)
""")

col1, col2 = st.columns([2, 1])
with col1:
    st.markdown("""
    **f(x) = 1/(x) if x ≠ 0 else 2**
    
    - x = 0에서 불연속 (무한 불연속)
    - 따라서 미분 불가능
    """)
with col2:
    st.info("문제점: 구간 [-2, 2]에서 x=0에서 불연속")

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# 분수 함수
x_neg = np.linspace(-3, -0.1, 100)
x_pos = np.linspace(0.1, 3, 100)

ax = axes[0]
ax.plot(x_neg, 1/x_neg, 'b-', linewidth=2.5)
ax.plot(x_pos, 1/x_pos, 'b-', linewidth=2.5, label='f(x) = 1/x')

# 음수쪽 점 (-1, -1)과 양수쪽 점 (1, 1)
ax.scatter([-1], [-1], color='green', s=100, zorder=5, label='음수쪽 점 (-1, -1)')
ax.scatter([1], [1], color='green', s=100, zorder=5, label='양수쪽 점 (1, 1)')
ax.axvline(x=0, color='red', linestyle='--', alpha=0.7, linewidth=2, label='불연속점 (x=0)')

ax.set_xlabel('x', fontsize=11)
ax.set_ylabel('y', fontsize=11)
ax.set_xlim(-3, 3)
ax.set_ylim(-5, 5)
ax.grid(True, alpha=0.3)
ax.legend(fontsize=9)
ax.set_title('예시 2: 분수 함수 f(x) = 1/x', fontsize=12, fontweight='bold')

# 문제 설명
ax = axes[1]
ax.text(0.5, 0.9, '불연속점에서의 상황', ha='center', va='top', fontsize=12, fontweight='bold', transform=ax.transAxes)
ax.text(0.5, 0.75, '• x = 0에서 불연속 (함수값 정의 X)', ha='center', va='top', fontsize=10, transform=ax.transAxes)
ax.text(0.5, 0.65, '• 당연히 미분도 불가능', ha='center', va='top', fontsize=10, transform=ax.transAxes, color='red', fontweight='bold')

ax.text(0.5, 0.45, '평균값정리 조건:', ha='center', va='top', fontsize=11, fontweight='bold', transform=ax.transAxes,
        bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.7))
ax.text(0.5, 0.35, '✗ 구간에서 연속이 아님', ha='center', va='top', fontsize=10, transform=ax.transAxes, color='red', fontweight='bold')
ax.text(0.5, 0.25, '✗ 미분 불가능', ha='center', va='top', fontsize=10, transform=ax.transAxes, color='red', fontweight='bold')

ax.text(0.5, 0.1, '결론: 첫 번째 조건부터 위반!', ha='center', va='top', fontsize=11, fontweight='bold',
        transform=ax.transAxes, bbox=dict(boxstyle='round', facecolor='lightcoral', alpha=0.7))

ax.axis('off')

st.pyplot(fig)

st.markdown("""
---
### 📌 예시 3: 계단 함수 (점프 불연속)
""")

col1, col2 = st.columns([2, 1])
with col1:
    st.markdown("""
    **f(x) = 점프 함수**
    
    - x = 2에서 불연속 (점프)
    - 연속이 아니므로 미분 불가능
    """)
with col2:
    st.info("문제점: 구간 [0, 3]에서 x=2에서 불연속")

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

ax = axes[0]

# 계단 함수
x1_seg = np.linspace(0, 2, 100, endpoint=False)
x2_seg = np.linspace(2, 3, 100)

ax.plot(x1_seg, np.ones_like(x1_seg), 'b-', linewidth=2.5, label='f(x) - 구간 [0,2)')
ax.plot(x2_seg, 3*np.ones_like(x2_seg), 'b-', linewidth=2.5, label='f(x) - 구간 [2,3]')

# 끝점
ax.scatter([0], [1], color='blue', s=100, zorder=5)
ax.scatter([2], [1], color='blue', s=100, facecolors='none', zorder=5)  # 열린 점
ax.scatter([2], [3], color='blue', s=100, zorder=5)  # 닫힌 점
ax.scatter([3], [3], color='blue', s=100, zorder=5)

# 점프 표시
ax.arrow(2, 1, 0, 1.5, head_width=0.1, head_length=0.1, fc='red', ec='red', alpha=0.5)
ax.text(2.3, 2, '점프\n불연속', fontsize=9, color='red', fontweight='bold')

ax.set_xlabel('x', fontsize=11)
ax.set_ylabel('y', fontsize=11)
ax.set_xlim(-0.5, 3.5)
ax.set_ylim(0, 3.5)
ax.grid(True, alpha=0.3)
ax.legend(fontsize=9)
ax.set_title('예시 4: 계단 함수 (점프 불연속)', fontsize=12, fontweight='bold')

# 문제 설명
ax = axes[1]
ax.text(0.5, 0.9, 'x = 2에서의 상황', ha='center', va='top', fontsize=12, fontweight='bold', transform=ax.transAxes)
ax.text(0.5, 0.75, '• x = 2에서 불연속 (점프)', ha='center', va='top', fontsize=10, transform=ax.transAxes, color='red', fontweight='bold')
ax.text(0.5, 0.65, '• lim(x→2⁻) f(x) = 1 ≠ 3 = f(2)', ha='center', va='top', fontsize=9, transform=ax.transAxes)
ax.text(0.5, 0.55, '• 당연히 미분도 불가능', ha='center', va='top', fontsize=10, transform=ax.transAxes)

ax.text(0.5, 0.4, '평균값정리 조건:', ha='center', va='top', fontsize=11, fontweight='bold', transform=ax.transAxes,
        bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.7))
ax.text(0.5, 0.3, '✗ [0, 3]에서 연속이 아님', ha='center', va='top', fontsize=10, transform=ax.transAxes, color='red', fontweight='bold')
ax.text(0.5, 0.2, '✗ 미분 불가능', ha='center', va='top', fontsize=10, transform=ax.transAxes, color='red', fontweight='bold')

ax.text(0.5, 0.05, '결론: 연속 조건부터 위반!', ha='center', va='top', fontsize=11, fontweight='bold',
        transform=ax.transAxes, bbox=dict(boxstyle='round', facecolor='lightcoral', alpha=0.7))

ax.axis('off')

st.pyplot(fig)

st.markdown("""
---
## 📋 요약 비교표

| 함수 | 연속 | 미분가능 | 평균값정리 | 이유 |
|------|------|---------|----------|------|
| **|x|** | ✓ | ✗ | ✗ | x=0에서 꺾임 (좌≠우 미분) |
| **1/x** | ✗ | ✗ | ✗ | x=0에서 불연속 (무한 불연속) |
| **계단함수** | ✗ | ✗ | ✗ | x=2에서 점프 불연속 |
| **다항식** | ✓ | ✓ | ✓ | 모든 구간에서 미분가능 |

---
## 🎯 핵심 정리

### ⭐ 평균값정리 성립 조건 (필수!)
1. **닫힌 구간 [a, b]에서 연속** ← 모든 조건의 기초
2. **열린 구간 (a, b)에서 미분가능** ← 이것이 없으면 안 됨

### ⚠️ 흔한 실수
- "함수가 연속이면 되지 않나?" → **NO! 미분가능도 필요**
- "이 점에서 깎아지른 것 같은데?" → **미분불가능한 점!**
- "경계에서는 괜찮지 않나?" → **NO! 특히 경계점에 주의**

### ✅ 안전한 함수들
- 다항식 (polynomial) - 모든 구간에서 미분가능
- 삼각함수 (sin, cos) - 모든 구간에서 미분가능
- 지수함수 (e^x) - 모든 구간에서 미분가능
- 로그함수 - 정의역 내에서 미분가능
""")
