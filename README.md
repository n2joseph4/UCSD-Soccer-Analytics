# UCSD Soccer Analytics
 
## Description of Layout of Github

### Men's Folder

- The games folder holds the notebooks that contains code used for reports for each individual game. The code for a specific game can be found under the folder with the name of the opponent

 - Under the league and then histograms folder you can find histograms relating UCSD as a team and player specific to the other teams and players in the Big West

 - The Reports folder contains a few examples of formal reports used to report statistics and analysis of seasons and games as well as certain aspects of play.
     - The 2024 analysis report contains a report of UCSD's most recent season and highlights areas of stregnth and improvement
     - The 2023 analysis analyzes the 2023 season and what KPI's led to success and what aspects of play most correlated to success. In addition this report utilized machine learning models to establish goals for each KPI
     - The midseason analysis report contains an update on the goals set at the beginning of the season and an analysis of our strengths and weaknesses so far. Only contains games before league play.
     - The league comparison report contains an analysis of UCSD's players compared to the rest of the players in the Big West by position in certain statistical measures.
- The datacollector.py file contains the code for the application I created to track events in games such as passes, tackles, and shots.
- The rest of the notebooks in the men's folder (besides for midseasonanalysis) contain the code for whole season analysis of certain aspects
     - Check out shotsAgainst.ipynb for analysis of opponen'ts chances against UCSD
     - The offensive/defensive duels notebook maps all offensive and defensive duels and accuracies across pitch
     - Passes maps out all the passes UCSD had an accuracies in certain parts of the pitch as well as key passes and player specifics.
     - postSeasonAnalysis contains the code used to create the statistical KPI's and create histograms to compare players and teams in the Big West.
