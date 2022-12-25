import pandas as pd
import pandas_gbq as pdgbq

sql ='''
-- calling a CTE to make the table name actually readable

WITH data AS (
SELECT 
  * 
FROM 
  `chess-371023.chessPuzzles.puzzlesClean`
)

SELECT
  week,
  year,
  SUM(score) AS score,
  COUNT(*) AS puzzles,
  ROUND(SUM(score)/COUNT(*)*100,2) AS pct
FROM 
  data
GROUP BY
  week,
  year
'''

weekly_data = pd.read_gbq(query=sql,project_id='chess-371023')

print(weekly_data)