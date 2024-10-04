import pandas as pd
from sqlalchemy import create_engine


def create_df(table_name, database_uri):
    engine = create_engine(database_uri)
    query = f"SELECT agent_id, call_duration_sec FROM {table_name}"
    df = pd.read_sql(query, engine)
    return df

def find_avg_call_length(df):
    average_call_length = df.groupby("agent_id")["call_duration_sec"].mean()
    return agent_avg_call_length

def find_percentile_call_length(df, percentile):
    agent_call_length = df.groupby("agent_id")["call_duration_sec"].quantile(percentile)
    return agent_call_length


if __name__ == "__main__":
    database_uri = "sqlite:///conversations.db"
    table_name = "conversations"
    conversation_df = create_df(table_name, database_uri)
    average_df = find_avg_call_length(conversation_df)
    percentile_df = find_percentile_call_length(conversation_df, 0.9)
    customer_info_df = pd.merge(average_df, percentile_df, on='id')
    customer_info_df.to_csv("s3://cresta-takehome/average_call_lengths.csv", index=False)

    print(customer_info_df)
