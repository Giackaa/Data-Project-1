League Data Project

Welcome to the League Data Project repository! This project documents my journey and challenges as I explore and analyze data related to League of Legends, a game I am passionate about. From raw data exploration to advanced analytics, this repository will grow with insights, experiments, and solutions I discover along the way.

-----
About the Project

The League Data Project is centered on leveraging data to uncover patterns, improve gameplay strategies, and better understand the dynamics of League of Legends. The project will include a variety of topics such as:

Data Cleaning: Preparing raw data for analysis.

Visualization: Creating intuitive graphs and dashboards to represent trends.

Statistics: Applying statistical methods to derive meaningful conclusions.

Game Mechanics Insights: Analyzing in-game metrics to enhance performance.

-----

Python

Initially used the individualPosition column to determine roles but discovered inaccuracies (e.g., players with utility roles who weren't supports).

Switched to teamPosition data after scraping accurate data from the League API.

Consulted ChatGPT to draft a standard code for API scraping and modified it to meet specific needs.

-----

Filtered out:

Non-relevant roles (Jungle and Utility retained).

Games shorter than 20 minutes (less than 1200 seconds).

Analyzed gold differences between junglers and supports, grouping players by gameID.

Excluded games with significant gold discrepancies (> 100 gold per minute).

-----

Excel

Sorted players into teams and used formulas to auto increment across rows.

Verified data validity by checking game lengths and win/loss outcomes.

Compartmentalized vision scores and pick kills into percentiles for better readability.

Used scatter charts and trend lines to illustrate relationships between vision scores and jungler pick kills.

Joined jungler and support data tables for pivot analysis using PowerQuery.

Used PowerQuery to condense data into useful tables.

Grouped data by gameID to provide a general overview of each game.

Transformed champion IDs into names using PowerQuery by unpivoting, joining, and pivoting columns.

Unified multiple champion tables into one culmination table.

Organized games into categories based on time intervals (e.g., 15-20, 20-25 minutes).

Identified champions that carried games based on damage output relative to game time.

Evaluated champions' performance compared to the average performance in their respective time slots.

-----
Tableau

Investigated correlations between gold earned and wards placed but noted both metrics increase with game length.

Used percentiles to evaluate jungler performance in games with low vs. high support ward placements within specific time slots.

Utilized LOD expressions to calculate fixed 75th/25th percentiles for each time slot.

Used calculated fields with IF statements to categorize data into "Above 75th", "Below 25th", or "Other" categories.

Excluded games with durations beyond 3000 seconds due to significantly lower sample sizes, limiting statistical illusions.

-----
Problems and Solutions

Data Grouping: Debated between PowerQuery and MySQL; opted for PowerQuery due to quicker imports.

Formula Refresh: Reviewed COUNTIF and other formulas to regain proficiency.

Correlation Challenges: Gold earned and wards placed increased with game length; used percentiles within time slots to normalize data.

Low Sample Sizes: Excluded game times beyond 3000 seconds to avoid statistical illusions.

-----
To-Do List

Continue refining data analysis methods.

Explore deeper insights into jungler-support dynamics.

Optimize workflows between PowerQuery and MySQL.

Develop additional visualizations to enhance interpretability.

-----
Findings and Recommendations

Those who place more wards than 75% of other players increase their jungler’s gold earning by an average of 618 gold vs. 162 gold for those who has killed more wards

Killing more wards increases an extra 0.42 to the jungler's gank kills, while placing more wards is an extra 0.93, more than 2x more efficient than killing more wards.

In fostering a better performative environment for the jungler, I would recommend a support to focus on placing more wards around the map rather than seeking to kill more wards.

-----
Feedback and Collaboration

I am open to suggestions and feedback as I refine my methods and learn more about data analysis and League of Legends. If you want to collaborate or discuss ideas, feel free to reach out!

Disclaimer

This repository is a work in progress. It will grow over time as I upload more information and tackle new challenges. Stay tuned for updates!
