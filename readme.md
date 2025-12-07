# Running Tracker (Python CLI)

A small command-line app for tracking runs.  
Data is stored in a local `runs.json` file.

## Features

- Add a run (date, distance, time in minutes)
- List all saved runs
- Show stats:
  - Average pace (min/km)
  - Total distance
  - Total time
  - Longest run
  - Fastest run
- Save data to `runs.json` and load it on start

## Data format

```json
{
  "date": "2025-07-12",
  "distance": 10.0,
  "time_min": 42.5,
  "pace": 4.25
}


