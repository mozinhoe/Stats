import argparse
import csv
from typing import List


def load_data(path: str):
    """Load CSV data into a list of dictionaries with numeric values."""
    data = []
    with open(path, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            for key, value in row.items():
                if key not in ('Player', 'Team'):
                    row[key] = float(value)
            data.append(row)
    return data


def compare_player(data, player: str, stats: List[str], top: int):
    player_row = next((r for r in data if r['Player'] == player), None)
    if not player_row:
        raise ValueError(f"Player '{player}' not found in dataset")
    stats = [s.strip() for s in stats]

    def distance(row):
        return sum((row[s] - player_row[s]) ** 2 for s in stats) ** 0.5

    results = [(row['Player'], distance(row)) for row in data if row['Player'] != player]
    results.sort(key=lambda x: x[1])
    return results[:top]


def main():
    parser = argparse.ArgumentParser(description="Find players with similar statistics")
    parser.add_argument('--player', required=True, help='Name of the player to compare')
    parser.add_argument('--stats', required=True, help='Comma separated list of statistics to compare')
    parser.add_argument('--top', type=int, default=5, help='Number of similar players to display')
    parser.add_argument('--data', default='data/sample_stats.csv', help='Path to the CSV data file')
    args = parser.parse_args()

    data = load_data(args.data)
    try:
        results = compare_player(data, args.player, args.stats.split(','), args.top)
    except ValueError as e:
        print(e)
        return

    stat_list = ', '.join([s.strip() for s in args.stats.split(',')])
    print(f"Players most similar to {args.player} based on {stat_list}:")
    for name, dist in results:
        print(f"{name}: distance={dist:.2f}")


if __name__ == '__main__':
    main()
