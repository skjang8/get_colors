def get_colors(n, colormap='rainbow', start=0, end=1):
    """
    Returns a list of n colors from a specified colormap.
    
    Parameters:
    -----------
    n : int
        Number of colors to return
    colormap : str, default='rainbow'
        Name of the colormap. Options: 'rainbow', 'viridis', 'plasma', 'inferno', 'magma', 'cividis'
    start : float, default=0
        Start point in the colormap (0-1)
    end : float, default=1
        End point in the colormap (0-1)
        
    Returns:
    --------
    list of tuples
        Each tuple contains RGB values (0-255)
    """
    import numpy as np
    
    # Define colormaps
    colormaps = {
        'rainbow': _rainbow_colormap,
        'viridis': _viridis_colormap,
        'plasma': _plasma_colormap,
        'inferno': _inferno_colormap,
        'magma': _magma_colormap,
        'cividis': _cividis_colormap
    }
    
    if colormap not in colormaps:
        raise ValueError(f"Colormap '{colormap}' not found. Available options: {', '.join(colormaps.keys())}")
    
    # Generate colors
    colormap_func = colormaps[colormap]
    indices = np.linspace(start, end, n)
    colors = [colormap_func(i) for i in indices]
    
    # Convert to RGB 0-255 format
    rgb_colors = [(int(r*255), int(g*255), int(b*255)) for r, g, b in colors]
    
    return rgb_colors

# Colormap functions (simplified versions)
def _rainbow_colormap(x):
    """Simple rainbow colormap"""
    import numpy as np
    r = np.sin(2 * np.pi * x)
    g = np.sin(2 * np.pi * (x + 1/3))
    b = np.sin(2 * np.pi * (x + 2/3))
    r = (r + 1) / 2
    g = (g + 1) / 2
    b = (b + 1) / 2
    return (r, g, b)

def _viridis_colormap(x):
    """Simplified viridis colormap"""
    r = 0.267004 + 0.004334 * x + 0.609349 * x**2 - 0.289708 * x**3
    g = 0.004184 + 0.996599 * x - 0.892622 * x**2 + 0.364725 * x**3
    b = 0.329415 + 1.205766 * x - 0.236311 * x**2 - 0.860769 * x**3
    return (max(0, min(1, r)), max(0, min(1, g)), max(0, min(1, b)))

def _plasma_colormap(x):
    """Simplified plasma colormap"""
    r = 0.050383 + 2.419416 * x - 1.269078 * x**2 - 0.219252 * x**3
    g = -0.494022 + 4.216742 * x - 6.862027 * x**2 + 3.710021 * x**3
    b = 0.435589 + 1.380345 * x - 4.141389 * x**2 + 2.622029 * x**3
    return (max(0, min(1, r)), max(0, min(1, g)), max(0, min(1, b)))

def _inferno_colormap(x):
    """Simplified inferno colormap"""
    r = 0.001462 + 1.325968 * x + 1.098073 * x**2 - 1.538687 * x**3
    g = -0.002279 + 0.188537 * x + 1.315485 * x**2 - 1.427050 * x**3
    b = 0.003969 + 0.052995 * x - 0.311907 * x**2 - 0.661653 * x**3
    return (max(0, min(1, r)), max(0, min(1, g)), max(0, min(1, b)))

def _magma_colormap(x):
    """Simplified magma colormap"""
    r = -0.002136 + 0.846715 * x + 1.881522 * x**2 - 1.827672 * x**3
    g = -0.000749 + 0.053352 * x + 1.026376 * x**2 - 0.391702 * x**3
    b = 0.010756 + 1.268900 * x - 1.553634 * x**2 + 0.518829 * x**3
    return (max(0, min(1, r)), max(0, min(1, g)), max(0, min(1, b)))

def _cividis_colormap(x):
    """Simplified cividis colormap"""
    r = 0.0 + 1.0 * x
    g = 0.3 + 0.7 * x
    b = 0.9 - 0.9 * x
    return (max(0, min(1, r)), max(0, min(1, g)), max(0, min(1, b)))

# Usage example
if __name__ == "__main__":
    colors = get_colors(5, colormap='rainbow')
    print(colors) 