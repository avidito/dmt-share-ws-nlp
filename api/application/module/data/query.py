from application.database.utils import cvt_str_to_regex

from google.cloud import bigquery

def get_scraping_result(query_params):
    pattern_cols = ["website", "category", "native_category"]
    params = {
        col:
            cvt_str_to_regex(value) if (col in pattern_cols)
            else value
        for col, value in query_params.items()
    }

    client = bigquery.Client()
    query_str = """
    SELECT
        title,
        website,
        channel,
        category,
        native_category,
        url,
        publish_dt
    FROM ws.scraping_result
    WHERE publish_dt BETWEEN "{start_date}" AND "{end_date}"
      AND website LIKE "{website}"
      AND category LIKE "{category}"
      AND native_category LIKE "{native_category}"
    """.format(**params)
    query = client.query(query_str)

    return query.result()
