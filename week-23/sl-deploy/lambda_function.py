"""
This script grabs the NBA league leaders in points
and writes it to:

- AWS S3
- mLab database

Note that AWS and mLab accounts must be created and setup.
"""

import random
import datetime
import csv
import logging
import os
import json
from io import StringIO

import requests
import boto3
from bs4 import BeautifulSoup
from pymongo import MongoClient


# Create logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter(
    '%(asctime)s.%(msecs)d [%(levelname)s] "%(message)s"',
    datefmt='%Y-%m-%d %H:%M:%S')
)
logger.addHandler(handler)


def get_data():
    """
    Scrape NBA top 10 scoring leaders
    """
    url = 'http://www.espn.com/nba/statistics/player/_/stat/scoring'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('table', class_='tablehead')
    rows = soup.find_all('tr', class_=['oddrow', 'evenrow'])
    player_data = []
    for row in rows[:10]:
        cells = row.find_all('td')
        player_data.append({
            'name': cells[1].text.split(',')[0],
            'points': cells[5].text
        })
    logger.info('Successfully pulled data')
    return player_data


def write_to_s3(data, bucket, datetime_now):
    """
    Write file to AWS S3
    """
    output = StringIO()
    rows = [['name', 'points']]
    for item in data:
        rows.append([item['name'], item['points']])
    csv.writer(output).writerows(rows)
    s3 = boto3.client('s3')
    s3.put_object(
        Body=output.getvalue().encode(),
        Bucket=bucket,
        Key='bball/data_{}.csv'.format(datetime_now.strftime('%Y-%m-%d_%H-%M-%S'))
    )
    logger.info('Data written to S3 bucket: {}'.format(bucket))


def write_to_mlab(
    data,
    datetime_now,
    mongo_uri,
    collection_name
):
    """
    Write data to mLab (cloud hosted MongoDB database)
    """
    client = MongoClient(mongo_uri)
    db_name = mongo_uri.split('/')[-1]
    db = client[db_name]
    collection = db[collection_name]
    record = {
        'data': data,
        'created_on': datetime_now.strftime('%Y-%m-%d_%H-%M-%S')
    }
    collection.insert_one(record)
    logger.info('Data written to mLab collection: {}'.format(collection_name))


def main():
    """
    Grab a todo and write it to S3 and mLab
    """
    now = datetime.datetime.utcnow()
    todo = get_data()
    write_to_s3(
        data=todo,
        bucket=os.environ['AWS_S3_BUCKET'],  # must be unique
        datetime_now=now
    )
    write_to_mlab(
        data=todo,
        datetime_now=now,
        mongo_uri=os.environ['MLAB_URI'],
        collection_name='bball'
    )


def lambda_handler(event, context):
    """
    Handler for AWS Lambda
    """
    main()
    return {
        'statusCode': 200,
        'body': json.dumps('Lambda executed successfully!')
    }


if __name__ == "__main__":
    main()
