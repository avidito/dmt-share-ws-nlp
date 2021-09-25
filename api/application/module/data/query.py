from sqlalchemy import and_, func

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
        ScrapingResult.url,
        ScrapingResult.publish_dt
    ).select_from(
        ScrapingResult
    ).filter(
        and_(
            func.DATE(ScrapingResult.publish_dt) >= params["start_date"],
            func.DATE(ScrapingResult.publish_dt) <= params["end_date"],
            ScrapingResult.website.like(params["website"]),
            ScrapingResult.category.like(params["category"]),
            ScrapingResult.native_category.like(params["native_category"]),
        )
    )
    return query.all()
