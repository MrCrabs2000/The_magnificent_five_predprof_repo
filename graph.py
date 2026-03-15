import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path


def create_graph(y,
                x=None,
                xlabel='X',
                ylabel='Y',
                title='График',
                filename='graph.png',
                transparent=False,
                grid=True):

    dirr = Path(__file__).parent
    last_dirr = dirr / 'static' / 'images'
    last_dirr.mkdir(parents=True, exist_ok=True)
    path = last_dirr / filename

    if path.exists():
        print(f"Файл {filename} уже существует в {dir}")
        return False

    fig, ax = plt.subplots(figsize=(10, 6))

    if x is None:
        x = range(len(y))

    ax.plot(x, y, linewidth=2, marker='o', markersize=4)

    ax.set_xlabel(xlabel, fontsize=12)
    ax.set_ylabel(ylabel, fontsize=12)
    ax.set_title(title, fontsize=14, fontweight='bold')

    if grid:
        ax.grid(grid, linestyle='--')

    if transparent:
        fig.patch.set_alpha(0.0)
        ax.patch.set_alpha(0.0)
    else:
        fig.patch.set_facecolor('white')
        ax.set_facecolor('#f8f9fa')

    plt.tight_layout()
    plt.savefig(
        path,
        dpi=300,
        bbox_inches='tight',
        transparent=transparent
    )
    plt.close(fig)

    return True


def create_chart(data,
                 chart_type='bar',
                 title='Диаграмма',
                 filename='chart.png',
                 transparent=False):
    dirr = Path(__file__).parent
    path = dirr / 'static' / 'images' / filename
    path.parent.mkdir(parents=True, exist_ok=True)

    if path.exists():
        print(f"Файл {filename} уже существует в {dir}")
        return False

    fig, ax = plt.subplots(figsize=(10, 6))

    labels = list(data.keys())
    values = list(data.values())

    if chart_type == 'bar':
        ax.bar(labels, values, color='#4e73df', edgecolor='black', alpha=0.8)
        ax.grid(axis='y', linestyle='--', alpha=0.7)
    elif chart_type == 'pie':
        num_colors = len(values)
        colors = plt.cm.tab20(range(num_colors))
        ax.pie(values, labels=labels, autopct='%1.1f%%', startangle=140,
               colors=colors)

    ax.set_title(title, fontsize=14, fontweight='bold')

    if transparent:
        fig.patch.set_alpha(0.0)
        ax.patch.set_alpha(0.0)

    plt.tight_layout()
    plt.savefig(path, dpi=300, bbox_inches='tight', transparent=transparent)
    plt.close(fig)
    return True


def data_accuracy_graph(data, filename='graph.png'):
    return create_graph(y=data.values(), x=data.keys(), ylabel='точность', xlabel="кол-во эпох", title="Зависимость точности",
                 filename=filename)


def civilization_records_chart(data, filename='chart.png', top5=False):
    return create_chart(data=data, filename=filename,
                        title="Записи по цивилизациям" + (" (топ 5)" if top5 else ""), chart_type='pie')


def accuracy_determination_chart(data, filename='chart.png'):
    return create_chart(data=data, filename=filename, title="Точность определения записей")


def top5_class_chart(data, filename='chart.png'):
    selected_data = dict(sorted(data.items(), key=lambda item: item[1])[-5:])
    return civilization_records_chart(data=selected_data, filename=filename, top5=True)