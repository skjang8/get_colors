def get_colors(n, L=70, C=60):
    """
    Get colors evenly distributed in hue at constant lightness and chroma
    
    Args:
        n: Number of colors to generate
        L: Lightness value (0-100)
        C: Chroma/saturation value (0-128 recommended)
    
    Returns:
        List of RGB colors
    """
    import numpy as np
    
    colors = []
    
    # Distribute hue angles evenly
    hue_angles = np.linspace(0, 360, n, endpoint=False)
    
    for h in hue_angles:
        # Convert LCh to Lab
        LCh = np.array([L, C, h])
        Lab = LCHab_to_Lab(LCh)
        
        # Convert to RGB
        XYZ = Lab_to_XYZ(Lab)
        RGB = XYZ_to_sRGB(XYZ)
        RGB = np.clip(RGB, 0, 1)  # Ensure valid RGB
        
        colors.append(RGB)
        
    return colors

def LCHab_to_Lab(LCh):
    """Convert from CIE LCh to CIE Lab"""
    import numpy as np
    L, C, h = LCh
    h_rad = np.radians(h)
    a = C * np.cos(h_rad)
    b = C * np.sin(h_rad)
    return np.array([L, a, b])

def Lab_to_XYZ(Lab):
    """Convert from CIE Lab to CIE XYZ"""
    import numpy as np
    L, a, b = Lab
    
    # D65 white point
    Xn, Yn, Zn = 0.95047, 1.0, 1.08883
    
    fy = (L + 16) / 116
    fx = a / 500 + fy
    fz = fy - b / 200
    
    def f_inv(t):
        delta = 6/29
        if t > delta:
            return t**3
        else:
            return 3 * delta**2 * (t - 4/29)
    
    X = Xn * f_inv(fx)
    Y = Yn * f_inv(fy)
    Z = Zn * f_inv(fz)
    
    return np.array([X, Y, Z])

def XYZ_to_sRGB(XYZ):
    """Convert from CIE XYZ to sRGB"""
    import numpy as np
    X, Y, Z = XYZ
    
    # XYZ to linear RGB
    r = 3.2404542 * X - 1.5371385 * Y - 0.4985314 * Z
    g = -0.9692660 * X + 1.8760108 * Y + 0.0415560 * Z
    b = 0.0556434 * X - 0.2040259 * Y + 1.0572252 * Z
    
    # Linear RGB to sRGB (gamma correction)
    def to_sRGB(c):
        if c <= 0.0031308:
            return 12.92 * c
        else:
            return 1.055 * c**(1/2.4) - 0.055
    
    R = to_sRGB(r)
    G = to_sRGB(g)
    B = to_sRGB(b)
    
    return np.array([R, G, B])

# Usage example
if __name__ == "__main__":
    import numpy as np
    import matplotlib.pyplot as plt
    
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

    # Get colors
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
