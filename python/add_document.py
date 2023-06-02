import pandas as pd
import meilisearch


if __name__ == '__main__':
    df = pd.read_csv('./livedoornews.csv')
    df.loc[:, 'id'] = [i for i in range(1, df.shape[0] + 1)]
    documents = df.to_dict(orient='records')

    client = meilisearch.Client('http://host.docker.internal:7700')
    try:
        client.create_index('news', {'primaryKey': 'id'})
    except:
        pass

    index = client.index('news')
    print(len(documents))
    index.add_documents(documents)