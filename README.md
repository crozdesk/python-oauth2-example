# python-oauth2-crozdesk

Crozdesk login example integration for python.

## Requirements

This example requires `webapp2`, `httplib2` and `oauth2client`, to install them type:
```bash
pip install webapp2 httplib2 oauth2client
```

## Configuration

- Edit `crozdesk.py`, paste the api key and secret you get from [https://crozdesk.com/users/developers](https://crozdesk.com/users/developers)
- Update the callback url on the developers page to `http://localhost:3000/users/auth/crozdesk/callback`

## Running

To run the webapp, type in a terminal:
```bash
python crozdesk.py
```

And open [http://localhost:3000](http://localhost:3000) in a browser.
