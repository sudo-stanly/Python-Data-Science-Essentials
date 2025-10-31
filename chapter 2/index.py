import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
def draw_mondrian( painting_id ):
    rects = features.query('painting_id == @painting_id')
    total_width = rects.eval("x + width").max()
    total_height = rects.eval("y + height").max()
    
    fig, ax = plt.subplots()
    
    for (idx, row) in rects.iterrows():
        x, y, w, h, rgb = row[['x','y','width','height','rgb']]
        patch = mpatches.Rectangle((x, y), w, h, facecolor=rgb)
        ax.add_patch(patch)
    
    ax.axis([0, total_width, 0, total_height])
    ax.set_aspect('equal')
    ax.axis('off')
    fig.text(0.5, 0.01, painting_id, ha="center", fontsize=14)
    fig.show()
    
    ===
    
    import pandas as pd
import matplotlib.pyplot as plt

# DataFrame
painting_info = pd.DataFrame({
    "painting_id": ["b104", "b105", "b106", "b107", "b108", "b292", "b293", "b294", "b295", "b296"],
    "year": [1920, 1920, 1920, 1920, 1920, 1939, 1939, 1939, 1939, 1940],
    "title": [
        "No. VI",
        "Composition A",
        "Composition B",
        "Composition C",
        "Composition I",
        "Composition no. 1",
        "Composition of red, blue and white: II",
        "Trafalgar Square",
        "Composition no. 8",
        "Composition no. 11"
    ],
    "width": [1010, 918, 575, 610, 646, 1023, 330, 1200, 681, 711],
    "height": [1007, 900, 677, 603, 750, 1052, 435, 1452, 752, 825],
    "complexity": [41, 42, 41, 44, 44, 31, 26, 62, 47, 49]
})

plt.scatter(painting_info['year'], painting_info['complexity'], color='blue', label='Data points')
plt.plot(painting_info['year'], painting_info['complexity'], color='orange', marker='o', label='Trend line')

plt.xlabel('Year')
plt.ylabel('Complexity')
plt.title('Painting Complexity Over the Years')
plt.legend()
plt.grid(True)
plt.show()

===