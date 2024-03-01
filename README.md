# Flask-SaaSify

Provides a simple way to create a SaaS application with Python and Flask. It includes the most common features of a SaaS company, such as sign-up, login, payments, and more.

## Features
- Single, fully documented `.env` config
- Bootstrap 5 and Bootstrap Icons
- SEO and meta tags
- Server Side Analytics
    - Response times
- Sign-up and login
    - Magic links

## Planned features
- Progressive Web App
- Blog
    - Markdown
    - Comments
- Admin panel
    - Manage users
    - View analytics
- Sign-up and login
    - Social login (Google, Facebook, X, GitHub)
- Payments
    - Subscriptions
    - Stripe Checkout API
    - Webhooks to update subscription status
    - Pricing page
- Email
    - SendGrid?
    - E-mail templates
    - Drip campaigns
- Landing pages
    - Landing page
    - Waitlist
    - Affiliate program page

## Tech stack
- Docker
- Python
- Flask/SQLAlchemy
- SQLite

## Example
In your `.env` file:
```bash
# Flask
SECRET_KEY=
EXTERNAL_BASE_URL=http://127.0.0.1:5000
ADMINS=youremail@domain.com

# Database locations
DATABASE_URI=sqlite:///database.sqlite

# Default meta title for pages; keep concise for clarity and SEO
META_DEFAULT_TITLE=

# Meta description: Aim for 155-160 characters to provide a concise summary of the page's content
META_DEFAULT_DESCRIPTION=

# Meta keywords: List a few relevant keywords. Note: Most search engines ignore this tag due to past overuse
META_DEFAULT_KEYWORDS=

# Open Graph (Facebook) default type (e.g., website, article); specifies the type of content
META_OG_DEFAULT_TYPE=

# OG title: Aim for 60-90 characters to ensure it displays well on social platforms
META_OG_DEFAULT_TITLE=

# OG description: Keep under 200 characters for optimal display on social media
META_OG_DEFAULT_DESCRIPTION=

# OG image: Use high-quality images, at least 1200 x 630 pixels for best display on high-resolution devices
META_OG_DEFAULT_IMAGE=

# Twitter card type (e.g., summary, summary_large_image); defines the style of card displayed
META_TWITTER_DEFAULT_CARD=

# Twitter title: Keep concise, similar to OG title, for clarity and impact
META_TWITTER_DEFAULT_TITLE=

# Twitter description: Aim for less than 200 characters, focusing on engaging and concise summary
META_TWITTER_DEFAULT_DESCRIPTION=

# Twitter image: Optimal resolution is similar to OG image, with a minimum of 600 x 335 pixels for best display
META_TWITTER_DEFAULT_IMAGE=

```
```python
from flask import Flask
from flask_saasify import Saasify, login_required

app = Flask(__name__)
saasify = Saasify(app)

@app.route('/public')
def index():
    return 'Hello, World!'

@app.route('/private')
@login_required
def protected():
    return 'You are logged in!'

if __name__ == '__main__':
    app.run()
```

## License
AGPL-3.0, need a different license? Please [e-mail](mailto:vaneijk.koen@gmail.com) me.

## Publish to PyPi
```
python3 setup.py sdist bdist_wheel
twine upload dist/*
```