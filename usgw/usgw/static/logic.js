function oauthRedirect() {
  let request = new XMLHttpRequest();
  let authEndPoint = getAuthEndpoint();
  request.open('GET', authEndPoint, false);
  request.send(null);
  let redirectURL = request.responseText;
  redirectURL += '&redirect_uri=' + window.location.hostname + '/slack/auth'; // <- Need to implement SSL
  // The state parameter is used to send the current open page to the backend.
  redirectURL += '&state=' + window.location;
  window.location = redirectURL;
}

// This endpoint returns a redirect URL for Slack's OAuth
// to avoid hardcoding team and client IDs.
function getAuthEndpoint() {
  return location.protocol + '//' + location.hostname + (location.port ? ':' + location.port : '') + '/authredirecturl';
}
