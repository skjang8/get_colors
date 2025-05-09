# get_colors

쉽게 사용할 수 있는 컬러맵 유틸리티 함수입니다. 데이터 시각화나 플롯 작성 시 필요한 색상 세트를 생성합니다.

## 설치 방법

pip를 이용해 설치할 수 있습니다:

```bash
pip install git+https://github.com/skjang8/get_colors.git
```

## 사용 방법

```python
from get_colors import get_colors

# 5개의 무지개색 색상 생성
colors = get_colors(5, colormap='rainbow')
print(colors)
# 출력 예: [(255, 127, 0), (0, 255, 0), (0, 0, 255), (127, 0, 255), (255, 0, 127)]

# 다른 컬러맵 사용
viridis_colors = get_colors(3, colormap='viridis')
print(viridis_colors)

# 컬러맵의 특정 구간만 사용
colors_subset = get_colors(4, colormap='plasma', start=0.2, end=0.8)
print(colors_subset)
```

## 지원하는 컬러맵

- `rainbow`: 무지개 색상
- `viridis`: 파란색-녹색-노란색 그라데이션
- `plasma`: 보라색-빨간색-노란색 그라데이션
- `inferno`: 검정색-빨간색-노란색 그라데이션
- `magma`: 검정색-보라색-핑크색-노란색 그라데이션
- `cividis`: 파란색-노란색 그라데이션(색맹에 친화적)

## 라이센스

MIT 