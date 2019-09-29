# Relational Database Schema

## Tables

* credential(**id**: serial, slack_id: char_9)
* token(**id**: serial, credential_id: credential->id, token: char_30, valid: boolean)
* session_cookie(**token**: token->id, cookie: char_32)
* resource(**id**: serial, owner_id: credential->id, title: text, link: text, description: text)
* article(**id**: serial, owner_id: credential->id, title: text, body: text)
* project(**id**: serial, owner_id: credential->id, title: text, description: text)

### Credentials

`credential` stores a unique identifier for users to track them across sessions and access tokens. Slack IDs for non-enterprise workspaces are 9 characters long.

### Tokens

`token` stores a Slack access token

### Cookies

`session_cookie` stores session cookies indexed by their bound access token. The cookie is 32 characters long as it is a SHA256 hash encrypted with AES128.