from flask import Blueprint
import os

core_bp = Blueprint(
    "core", __name__, template_folder="templates", static_folder="static"
)


@core_bp.app_context_processor
def inject_meta_tags():
    meta_tags = {
        "title": os.environ.get("META_DEFAULT_TITLE"),
        "description": os.environ.get("META_DEFAULT_DESCRIPTION"),
        "keywords": os.environ.get("META_DEFAULT_KEYWORDS"),
        "og_type": os.environ.get("META_OG_DEFAULT_TYPE"),
        "og_title": os.environ.get("META_OG_DEFAULT_TITLE"),
        "og_description": os.environ.get("META_OG_DEFAULT_DESCRIPTION"),
        "og_image": os.environ.get("META_OG_DEFAULT_IMAGE"),
        "twitter_card": os.environ.get("META_TWITTER_DEFAULT_CARD"),
        "twitter_title": os.environ.get("META_TWITTER_DEFAULT_TITLE"),
        "twitter_description": os.environ.get("META_TWITTER_DEFAULT_DESCRIPTION"),
        "twitter_image": os.environ.get("META_TWITTER_DEFAULT_IMAGE"),
    }
    return {"meta": meta_tags}
