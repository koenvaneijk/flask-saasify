from flask import jsonify
from flask_saasify.core import core_bp
import os


@core_bp.route("/manifest.json")
def manifest():
    return jsonify(
        {
            "name": os.environ.get("META_DEFAULT_TITLE"),
            "short_name": os.environ.get("META_DEFAULT_TITLE"),
            "description": os.environ.get("META_DEFAULT_DESCRIPTION"),
            "icons": [
                {
                    "src": "/static/48x48.png",
                    "sizes": "48x48",
                    "type": "image/png",
                },
                {
                    "src": "/static/96x96.png",
                    "sizes": "96x96",
                    "type": "image/png",
                },
                {
                    "src": "/static/144x144.png",
                    "sizes": "144x144",
                    "type": "image/png",
                },
                {
                    "src": "/static/168x168.png",
                    "sizes": "168x168",
                    "type": "image/png",
                },
                {
                    "src": "/static/180x180.png",
                    "sizes": "180x180",
                    "type": "image/png",
                },
                {
                    "src": "/static/192x192.png",
                    "sizes": "192x192",
                    "type": "image/png",
                },
                {
                    "src": "/static/256x256.png",
                    "sizes": "256x256",
                    "type": "image/png",
                },
                {
                    "src": "/static/512x512.png",
                    "sizes": "512x512",
                    "type": "image/png",
                },
            ],
            "start_url": "/",
            "display": "standalone",
            "theme_color": "#ffffff",
            "background_color": "#ffffff",
        }
    )
