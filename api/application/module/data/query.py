from sqlalchemy import and_

from application.database.utils import cvt_str_to_regex
from application.database.models import ScrapingResult

def get_scraping_result(db, query_params):
    pattern_cols = ["website", "category", "native_category"]
    params = {
        col:
            cvt_str_to_regex(value) if (col in pattern_cols)
            else value
        for col, value in query_params.items()
    }

    query = db.query(
        ScrapingResult.title,
        ScrapingResult.website,
        ScrapingResult.channel,
        ScrapingResult.category,
        ScrapingResult.native_category,
        ScrapingResult.url
    ).select_from(
        ScrapingResult
    ).filter(
        and_(
            ScrapingResult.load_dt >= params["start_date"],
            ScrapingResult.load_dt <= params["end_date"],
            ScrapingResult.channel.like(params["website"]),
            ScrapingResult.channel.like(params["category"]),
            ScrapingResult.channel.like(params["native_category"]),
        )
    )
    return query.all()
