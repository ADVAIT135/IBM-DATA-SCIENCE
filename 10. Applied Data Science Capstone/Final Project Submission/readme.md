# SpaceX Launches — IBM Data Science Capstone (Final Project)

Author: Advait Gurunath Chavan (ADVAIT135)  
Course: IBM Applied Data Science Capstone

This directory contains the final project submission for the IBM Applied Data Science Capstone. The project collects, cleans, explores, and models SpaceX launch data (Falcon 9 and Falcon Heavy) and includes a Dash app for interactive exploration and basic predictions.

Project goal (short)
- Collect launch data (web-scraped + SpaceX API) and prepare a consolidated dataset.
- Perform EDA and create visualizations to understand launch success drivers.
- Train basic machine learning models to predict launch success probability.
- Provide an interactive Dash app to explore the data and model output.

Contents
- Final report (PDF)
  - ADVAIT GURUNATH CHAVAN _ IBM DATA SCIENCE_CAPSTONE PROJECT.pdf
  - Link: https://github.com/ADVAIT135/IBM-DATA-SCIENCE/blob/098aab89f71b8cbe6778be95500bc8ba1e919391/10.%20Applied%20Data%20Science%20Capstone/Final%20Project%20Submission/ADVAIT%20GURUNATH%20CHAVAN%20_%20IBM%20DATA%20SCIENCE_CAPSTONE%20PROJECT.pdf
- Notebooks
  - SpaceX-Machine-Learning-Prediction-Final.ipynb — final modeling and summary
    - https://github.com/ADVAIT135/IBM-DATA-SCIENCE/blob/098aab89f71b8cbe6778be95500bc8ba1e919391/10.%20Applied%20Data%20Science%20Capstone/Final%20Project%20Submission/SpaceX-Machine-Learning-Prediction-Final.ipynb
  - Web scraping Falcon 9 and Falcon Heavy Launches Records from Wikipedia.ipynb — scraping & initial parsing
    - https://github.com/ADVAIT135/IBM-DATA-SCIENCE/blob/098aab89f71b8cbe6778be95500bc8ba1e919391/10.%20Applied%20Data%20Science%20Capstone/Final%20Project%20Submission/Web%20scraping%20Falcon%209%20and%20Falcon%20Heavy%20Launches%20Records%20from%20Wikipedia.ipynb
  - lab-jupyter-launch-site-location_final.ipynb — launch-site location analysis & mapping
    - https://nbviewer.org/github/ADVAIT135/IBM-DATA-SCIENCE/blob/ced8d356aaf8eeddd78ac496b21035df8e507601/10.%20Applied%20Data%20Science%20Capstone/Final%20Project%20Submission/lab-jupyter-launch-site-location_final.ipynb
  - Additional labs and EDA notebooks:
    - Lab 1_ Collecting the data_jupyter-labs-spacex-data-collection-api.ipynb
    - Lab 2_ Data wrangling__labs-jupyter-spacex-Data wrangling.ipynb
    - EDA with Visualization Lab.ipynb
    - Assignment__ SQL Notebook for Peer Assignment_jupyter-labs-eda-sql-coursera_sqllite.ipynb
- Dash app
  - spacex-dash-app_final.py — interactive dashboard to explore launches and model predictions
    - https://github.com/ADVAIT135/IBM-DATA-SCIENCE/blob/098aab89f71b8cbe6778be95500bc8ba1e919391/10.%20Applied%20Data%20Science%20Capstone/Final%20Project%20Submission/spacex-dash-app_final.py
- Datasets
  - dataset_part_1.csv, dataset_part_2.csv, dataset_part_3.csv — intermediate parts of the scraped/compiled dataset
    - https://github.com/ADVAIT135/IBM-DATA-SCIENCE/blob/098aab89f71b8cbe6778be95500bc8ba1e919391/10.%20Applied%20Data%20Science%20Capstone/Final%20Project%20Submission/dataset_part_1.csv
    - https://github.com/ADVAIT135/IBM-DATA-SCIENCE/blob/098aab89f71b8cbe6778be95500bc8ba1e919391/10.%20Applied%20Data%20Science%20Capstone/Final%20Project%20Submission/dataset_part_2.csv
    - https://github.com/ADVAIT135/IBM-DATA-SCIENCE/blob/098aab89f71b8cbe6778be95500bc8ba1e919391/10.%20Applied%20Data%20Science%20Capstone/Final%20Project%20Submission/dataset_part_3.csv
  - spacex_launch_geo (2).csv — launch-site geolocation dataset used for maps
    - https://github.com/ADVAIT135/IBM-DATA-SCIENCE/blob/098aab89f71b8cbe6778be95500bc8ba1e919391/10.%20Applied%20Data%20Science%20Capstone/Final%20Project%20Submission/spacex_launch_geo%20(2).csv
- Visualizations / images (examples included)
  - pred chart.png, data_wrang.png, data scrap.png, payload.png, Success launch pieplot.png, highest launch.png, etc.

Quick start — requirements
- Python 3.8+ recommended
- Typical Python packages used (install with pip):
  - pandas, numpy, scikit-learn, matplotlib, seaborn, plotly, dash, requests, beautifulsoup4, lxml, jupyterlab
- Example:
  - pip install pandas numpy scikit-learn matplotlib seaborn plotly dash requests beautifulsoup4 lxml jupyterlab

How to run the notebooks
1. Clone the repository (or open directly on GitHub).
2. Open JupyterLab or Jupyter Notebook in the project directory:
   - jupyter lab
3. Open the notebook of interest (for final model/readme start with SpaceX-Machine-Learning-Prediction-Final.ipynb).
4. Run the cells in order. If a cell expects raw scraped data, run the web-scraping notebook first or use the provided CSV parts.

How to run the Dash app
1. Ensure the required datasets are present in the same folder as spacex-dash-app_final.py (the script reads CSVs in this directory).
2. Start the app:
   - python spacex-dash-app_final.py
3. Open http://127.0.0.1:8050/ in your browser to interact with the dashboard.

Notes on the data and reproducibility
- The project combines data from:
  - Wikipedia pages (Falcon 9 & Falcon Heavy launch tables — scraped)
  - SpaceX public APIs (where used)
  - Processed CSVs included in this folder
- If you want to reproduce the dataset from scratch, run the web scraping notebook first and follow the data-wrangling notebooks to produce a cleaned dataset used by the final notebook.

Results & deliverables
- Final report (PDF) summarizes approach, EDA, model selection, evaluation and conclusions.
- Final Jupyter notebook contains the end-to-end model build and interpretation.
- Dash app demonstrates interactive visualization of launch success rates and allows basic selection of payload/mass/launch site for model-based probability inspection.

Tips & troubleshooting
- Large notebooks (images/plots) can be slow to render — use JupyterLab for better performance.
- If a notebook fails because of missing columns or file not found, confirm the CSV parts are present in this directory and were not renamed.
- If Dash app fails to start due to missing package, pip-install the missing dependency (e.g., pip install dash).

Credits & acknowledgements
- IBM Data Science Capstone course materials (assignments and lab structure)
- SpaceX public data and Wikipedia tables used for scraping

License
- This repository content is provided by the author for educational/demo purposes. 

Contact
- Author: Advait Gurunath Chavan — https://github.com/ADVAIT135
