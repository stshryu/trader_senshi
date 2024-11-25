# Senshi's very own Calorie Tracker

## Frontend Features

Coming soon.

## Backend Server Features

### Authentication & JWT's

Supports basic authentication with a distiction between Admins and Users (there's currently no difference between the two).

Routes not related to logging in will require authentication before those API endpoints can be accessed.

Authentication is handled in the form of an access token that can be retrieved with a valid username/password.

### Food

Can create food entries into the DB that can track calories, type, name and quantity.

Quantity may be removed into a separate model in the future (maybe meals?)
