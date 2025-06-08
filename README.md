# Soccer Stats Comparison Tool

This project provides a simple command-line program for comparing soccer players using underlying statistics. It is inspired by the data available on sites like FBref. The included dataset is a small sample of player metrics per 90 minutes.

## Dataset

The CSV file `data/sample_stats.csv` contains example statistics such as:

- `Progressive_Carries_per90`
- `Successful_Take_ons_per90`
- `Progressive_Passes_per90`
- `Shot_Creating_Actions_per90`

The numbers are illustrative and not meant to match official sources exactly.

## Usage

Run the comparison script with Python:

```bash
python src/compare_players.py --player "Lionel Messi" --stats Progressive_Carries_per90,Successful_Take_ons_per90
```

You can specify any combination of stats (comma separated) and choose how many similar players to display with `--top`:

```bash
python src/compare_players.py --player "Kevin De Bruyne" --stats Progressive_Passes_per90,Shot_Creating_Actions_per90 --top 3
```

By default the script uses `data/sample_stats.csv`, but another CSV path can be supplied via the `--data` flag.

## Example Output

```
Players most similar to Lionel Messi based on Progressive_Carries_per90, Successful_Take_ons_per90:
Vinicius Junior: distance=1.67
Kylian Mbappe: distance=2.52
Bukayo Saka: distance=2.61
```

This helps identify players with comparable statistical profiles across one or more metrics.
