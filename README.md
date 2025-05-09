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

# Demonstrate color generation
colors = get_colors(10)
plt.figure(figsize=(2*len(colors), 2))

for i, color in enumerate(colors):
    plt.subplot(1, len(colors), i+1)
    plt.imshow([[color]])
    plt.axis('off')
    plt.title(f'Color {i+1}')
    
plt.tight_layout()
plt.show()



# Demonstrate color usage in scatter plot
n_classes = 5
n_points = 100

data = []
labels = []
for i in range(n_classes):
    center = np.random.randn(2) * 3
    points = center + np.random.randn(n_points, 2)
    data.append(points)
    labels.extend([i] * n_points)

data = np.vstack(data)
labels = np.array(labels)

# Get colors using color_picker
colors = get_colors(n_classes, L=65, C=80)

# Create scatter plot
plt.figure(figsize=(10, 8))

for i in range(n_classes):
    mask = labels == i
    plt.scatter(data[mask, 0], data[mask, 1], 
            c=[colors[i]], 
            label=f'Class {i+1}',
            alpha=0.6)

plt.xlabel('X')
plt.ylabel('Y')
plt.title('Random Clusters with Lab Color Space Colors')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()
```

## 매개변수 설명

- `n`: 생성할 색상 수
- `L`: 밝기 값 (0-100 범위, 기본값: 70)
- `C`: 채도 값 (0-128 권장, 기본값: 60)

이 함수는 색상(Hue)을 균등하게 분포시키고, 모든 색상의 밝기(Lightness)와 채도(Chroma)를 일정하게 유지하여 시각적으로 일관된 색상 팔레트를 생성합니다.

## 라이센스

MIT 
