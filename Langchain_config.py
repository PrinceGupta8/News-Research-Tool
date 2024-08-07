from langchain.llms import OpenAI  # or the correct path based on the documentation
from langchain import LLMChain, PromptTemplate
from dotenv import load_dotenv
load_dotenv()
import os
openai_api_key=os.getenv('OPENAI_API_KEY')
openai=OpenAI(api_key=openai_api_key)

from newsapi import NewsApiClient
newsapi_key = os.getenv('newsapi_key')
newsapi = NewsApiClient(api_key=newsapi_key)

def get_news_articles(query):
    articles = newsapi.get_everything(q=query, language='en', sort_by='relevancy')
    return articles['articles']

def summarize_articles(articles):
    summaries = []
    for article in articles:
        summaries.append(article['description'])
    return ' '.join(summaries)

def get_summary(query):
    articles = get_news_articles(query)
    summary = summarize_articles(articles)
    return summary

template = """
You are an AI assistant helping an news researcher. Given
the following query and the provided news article summaries, provide
an overall summary.
Query: {query}
Summaries: {summaries}
"""

prompt = PromptTemplate(template=template, input_variables=['query', 'summaries'])
llm_chain = LLMChain(prompt=prompt, llm=openai)

