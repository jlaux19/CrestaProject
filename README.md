# Cresta Project

## Introduction

This is the completed Cresta Take Home project for the Customer Engineer role.

## Assignment

The task is to find the average call length and the 90th percentile call length for each agent. There is a `conversations` table provided with various columns.

## Methods

I want to use the pandas library with Python to perform data manipulation, as this is ideal to perform the operations to clean the data and then perform the necessary actions to upload the data.

Given that there is a `call_duration_sec` column, this will be the gauge for the call length. Using the `agent_id` column as well, I will clean the data so that only these two columns are needed.

To find the average, there is a native `mean` function within pandas that can be used. To perform this, the pandas dataframe can be grouped by the `agent_id` column on the `call_duration_sec` values and then take the mean.

To find the 90th percentile call length, this action also has a native pandas function called `quantile`. To perform this, the same action above to group by is performed, but now replacing the end function with the `quantile` method.

After performing these two actions, I will merge the two dataframes into one to make reading this information more accessible. After this, I will send this data in a CSV file straight to the s3 bucket, as the `to_csv` method can take in a s3 bucket file path.
