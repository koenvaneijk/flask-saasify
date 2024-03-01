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
```python
from flask import Flask
from saasify import Saasify, login_required

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