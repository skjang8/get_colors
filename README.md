# get_colors

CIE Lab 색 공간을 기반으로 시각적으로 균일한 색상을 생성하는 함수입니다. 데이터 시각화나 플롯 작성 시 필요한 색상 세트를 생성합니다.

## 설치 방법

pip를 이용해 설치할 수 있습니다:

```bash
pip install git+https://github.com/skjang8/get_colors.git
```

## 사용 방법

```python
from get_colors import get_colors
import numpy as np

# 5개의 색상 생성
colors = get_colors(5)
print(colors)

# RGB 0-255 값으로 변환
rgb_colors = [(int(r*255), int(g*255), int(b*255)) for r, g, b in colors]
print(rgb_colors)

# 밝기와 채도 조절
light_colors = get_colors(3, L=80, C=40)  # 더 밝고 덜 채도높은 색상
dark_colors = get_colors(3, L=50, C=70)   # 더 어둡고 채도높은 색상
```

## 매개변수 설명

- `n`: 생성할 색상 수
- `L`: 밝기 값 (0-100 범위, 기본값: 70)
- `C`: 채도 값 (0-128 권장, 기본값: 60)

이 함수는 색상(Hue)을 균등하게 분포시키고, 모든 색상의 밝기(Lightness)와 채도(Chroma)를 일정하게 유지하여 시각적으로 일관된 색상 팔레트를 생성합니다.

## 라이센스

MIT 