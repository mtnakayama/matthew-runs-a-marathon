import math

import matplotlib.pyplot as plt
import pandas as pd


YEAR = 2021

DISTANCES = [3.1, 6.2, 9.3, 13.1, 15.5, 18.6, 21.7, 26.2, 31.1]
DISTANCE_LABELS = ["5K", "10K", "15K", "½ Marathon", "25K", "30K", "35K",
                   "Marathon", "50K"]

MAX_MILES = math.ceil(DISTANCES[-1])


def all_sundays(year, fmt='%Y-%m-%d'):
    """Return a list the string representation of all sundays in a year.

    based on <https://stackoverflow.com/a/48241484/1400059>
    """
    return pd.date_range(start=str(year), end=str(year+1),
                         freq='W-SUN').strftime(fmt).tolist()


def main():
    plt.rcParams["font.family"] = "Roboto Slab"

    sundays = all_sundays(2021, fmt='%-m/%-d')

    width = 11
    height = 8.5
    fig = plt.figure(figsize=(width, height))
    margin_left = 1.5 / width
    margin_bottom = 1 / height
    ax = fig.add_axes(
        (
            margin_left,
            margin_bottom,
            1 - 2 * margin_left,
            1 - 2 * margin_bottom
        ),
        xlim=(-0.5, len(sundays) - 0.5),
        ylim=(0, MAX_MILES)
    )

    title = f'Matthew Runs a Marathon {YEAR}'
    ax.set_title(
        title,
        fontsize=36,
        fontfamily='Abril Fatface',
        fontweight='normal'
    )

    ax.set_frame_on(False)  # remove border

    ax.set_xticks(range(len(sundays)))
    ax.set_xticklabels(sundays, rotation=90)

    ax.set_yticks(DISTANCES)
    y_tick_labels = (f'{dl}\n({d}mi)' for d, dl
                     in zip(DISTANCES, DISTANCE_LABELS))

    ax.set_yticklabels(y_tick_labels)
    ax.set_yticks(range(MAX_MILES), minor=True)
    ax.tick_params(axis='y', which='both', left=False, right=False)

    ax.grid(b=True, which='major', axis='y', color='black', linewidth=1)
    ax.grid(b=True, which='minor', axis='y', linestyle=':')

    plt.show()
    fig.savefig(f'{title}.pdf')


if __name__ == "__main__":
    main()
