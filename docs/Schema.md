# Relational Database Schema

## Tables

* credential(**id**: serial, slack_id: char_9)
* token(**id**: serial, credential_id: credential->id, token: char_30, valid: boolean)
* session_cookie(**token**: token->id, cookie: char_32)
* resource(**id**: serial, owner_id: credential->id, title: varchar_200, link: varchar_2500, description: varchar_5000)
* article(**id**: serial, owner_id: credential->id, title: varchar_200, body: varchar_25000)
* project(**id**: serial, owner_id: credential->id, title: varchar_200, description: varchar_5000)

### Credentials

`credential` stores a unique identifier for users to track them across sessions and access tokens. Slack IDs for non-enterprise workspaces are 9 characters long.

### Tokens

`token` stores a Slack access token

### Cookies

`session_cookie` stores session cookies indexed by their bound access token. The cookie is 32 characters long as it is a SHA256 hash encrypted with AES128.