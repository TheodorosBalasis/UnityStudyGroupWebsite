function oauthRedirect() {
  console.log(getAuthEndpoint());
  let request = new XMLHttpRequest();
  request.open('GET', getAuthEndpoint(), false);
  request.send(null);
  let redirectURL = request.responseText;
  redirectURL += '&redirect_uri=' + window.location.hostname + '/loginredirect';
  // The state parameter is used to send the current open page to the backend.
  redirectURL += '&state=' + window.location;
  window.location = redirectURL;
}

// This endpoint returns a redirect URL for Slack's OAuth
// to avoid hardcoding team and client IDs.
function getAuthEndpoint() {
  return location.protocol + '//' + location.hostname + (location.port ? ':' + location.port : '') + '/authredirecturl';
}
