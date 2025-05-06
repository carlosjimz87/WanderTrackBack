# WanderTrack Data Uploader

This Python script (`parser.py`) reads city-level population data from SimpleMaps and transforms it into a JSON format compatible with Firebase Firestore for the WanderTrack app.

## 📦 Data Sources
- City and population data from: [SimpleMaps World Cities Database](https://simplemaps.com/data/world-cities) _(free tier)_

## 📁 Files
- `worldcities.csv`: Original input file (must be placed in the project root)
- `parser.py`: Script to parse and convert the data
- `wandertrack.json`: Generated file ready to upload to Firestore

## 🔧 Usage
1. Download `worldcities.csv` from [SimpleMaps](https://simplemaps.com/data/world-cities)
2. Place it in the root folder of this script
3. Run:
```bash
python parser.py
```
4. In`wandertrack.json`.

## 🙏Acknowledgements

Data used in this project is sourced from [SimpleMaps](https://simplemaps.com/data/world-cities). The script is designed to facilitate the integration of city-level population data into the WanderTrack app.

