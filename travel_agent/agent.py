import os
from pyspark.sql import SparkSession

try:
    from google.adk.agents import Agent
except Exception:
    # Fallback minimal Agent stub when google.adk.agents isn't available
    class Agent:
        def __init__(self, name: str, model: str, instruction: str, description: str = ""):
            self.name = name
            self.model = model
            self.instruction = instruction
            self.description = description
        def __repr__(self):
            return f"<Agent name={self.name!r} model={self.model!r}>"

# 1. Initialize the Apache Spark Session
# This is the "Engine Room" that will handle millions of travel data points.
spark = SparkSession.builder \
    .appName("TravelAgent_BigData_Engine") \
    .config("spark.executor.memory", "2g") \
    .getOrCreate()

# 2. General Travel Assistant (The Brain)
# This agent handles the conversation and coordinates with the data engine.
root_agent = Agent(
    name="travel_assistant",
    model="gemini-2.5-flash",
    instruction="""You are a high-performance travel assistant. 
    You have access to a massive Apache Spark data engine. 
    When users ask for complex trends (like 'cheapest month to fly to Boston') 
    or specific niche requests (like 'highly-rated Bengali restaurants with 1000+ reviews'), 
    you use the Data Analyst Agent to process that information.""",
    description="Main interface for the user."
)

# 3. Spark Data Analyst Agent (The Muscle)
# This specialized agent's instruction focuses on using Spark to query datasets.
data_analyst_agent = Agent(
    name="spark_data_analyst",
    model="gemini-2.5-flash",
    instruction="""You are an expert data analyst. Your job is to take user 
    requests and translate them into Spark SQL queries to find patterns 
    in millions of rows of travel, hotel, and flight data.""",
    description="An agent that specializes in high-speed data processing using Apache Spark."
)

# Example helper function (How the agent would actually use Spark)
def query_travel_data(destination_city):
    """
    This is an example of how your agent would use Spark to find 
    the best deals in a massive dataset (e.g., searching for 
    authentic Bengali food options in a city like Boston).
    """
    # In a real app, this would load a massive Parquet or CSV file
    # df = spark.read.parquet("s3://travel-data/global_listings.parquet")
    # result = df.filter(df.city == destination_city).orderBy("rating", ascending=False)
    # return result.limit(5)
    pass