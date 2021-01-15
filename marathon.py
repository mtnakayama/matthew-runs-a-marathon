import math

import matplotlib.pyplot as plt
import pandas as pd



YEAR = 2021

DISTANCES = [3.1, 6.2, 9.3, 13.1, 15.5, 18.6, 21.7, 26.2, 31.1]
DISTANCE_LABELS = ["5K", "10K", "15K", "½ Marathon", "25K", "30K", "35K", "Marathon", "50K"]

MAX_MILES = math.ceil(DISTANCES[-1])

def all_sundays(year, fmt='%Y-%m-%d'):
    return pd.date_range(start=str(year), end=str(year+1),
                         freq='W-SUN').strftime(fmt).tolist()


def main():
    sundays = all_sundays(2021, fmt='%m/%d')

    width = 11
    height = 8.5
    fig = plt.figure(figsize=(width, height))
    margin_left = 1.5 / width
    margin_right = 1 / width
    margin_bottom = 1 / height
    ax = fig.add_axes(
        (
            margin_left,
            margin_bottom,
            1 - margin_left - margin_right,
            1 - 2 * margin_bottom
        ),
        xlim=(0, len(sundays)),
        ylim=(0, MAX_MILES)
    )

    ax.set_title("Matthew Runs a Marathon", fontdict={
        'fontsize': 20
    })
    ax.set_frame_on(False)  # remove border

    ax.set_xticks(range(len(sundays)))
    ax.set_xticklabels(sundays, rotation=75)

    ax.set_yticks(DISTANCES)
    y_tick_labels = (f'{dl}\n({d}mi)' for d, dl
                     in zip(DISTANCES, DISTANCE_LABELS))

    ax.set_yticklabels(y_tick_labels)
    ax.set_yticks(range(MAX_MILES), minor=True)
    ax.tick_params(axis='y', which='both', left=False, right=False)

    ax.grid(b=True, which='major', axis='y', color='black', linewidth=1)
    ax.grid(b=True, which='minor', axis='y', linestyle=':')

    plt.show()

if __name__ == "__main__":
    main()
