# Authentication

## Login

Users log in via Slack. This is done via Slack's OAuth authorization process, resulting in an access token.

### Access Token Scope

The access token has the minimal scope of `users.profile:read` as the only information required for this application to function is a Slack ID, a display name, and a link to an avatar image.

---

## Session

A unique secure HttpOnly session cookie is stored to keep a user signed into a specific account, and then read by the application server on each client request to retrieve user info such as display name and avatar image. This cookie is bound to the access token received when the user logs in via Slack.

### Cookie Expiration

Cookies and their corresponding access token expire when the user actively logs out, or the access token is revoked. When the application server attempts to use a revoked access token it will then invalidate the session cookie associated with it, and if an invalidated session cookie is sent to the application server it will tell the client to delete the cookie. Following cookie invalidation on the backend and deletion on the client, the binding between the session cookie and the access token is erased from the database.