import pandas as pd
from elasticsearch import Elasticsearch
from elasticsearch import helpers


def get_es_insert_data(df):
    df['author'] = df['姓']+df['名']
    df['author_yomi'] = df['姓読み']+df['名読み']
    return df[['作品ID', '作品名', '作品名読み', 'author', 'author_yomi']].rename(columns={'作品ID': 'id', '作品名': 'title', '作品名読み': 'title_yomi'})

def main():
    es = Elasticsearch(host='localhost', port=9200)
    BOOK_LIST_PATH = './es-data/list_person_all_extended_utf8.csv'
    ES_INDEX = "aozora"

    book_list = pd.read_csv(BOOK_LIST_PATH)
    bulk_book = []

    for _, row in get_es_insert_data(book_list).iterrows():
        bulk_book.append({"_index":ES_INDEX, "_type":"_doc", "_id": _, "_source": row.fillna("").to_dict()})
        if len(bulk_book) > 1000:
            helpers.bulk(es, bulk_book)
            bulk_book = []
    
    if len(bulk_book) > 0:
        helpers.bulk(es, bulk_book)

if __name__ == '__main__':
    main()