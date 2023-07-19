## Authorization code flow:
+ => Register a new application with the following properties from admin or: http://127.0.0.1:8000/o/applications/register/ \
	```
  [with all required properties, keep unhashed clientSecret in somewhere maybe in note]
  Name: App 1
	Client type: Confidential
  Authorization grant type: Authorization code
	redirect uris (must be same): http://127.0.0.1:8000/noexist/callback
  ```

+ => Generate CodeVerifier & CodeChallenge using PKCE from `generate_codes.py` and keep them.
	```CodeVerifier: OUFYT0dEM1pNNVZDUDhXN1o5MlAxMUZUMDNRVFZHTFBMOURHVDIxQlBJQjlOM0tNSDEzSERVVkI2NURaREhTTVYyS1BZSEs0SllEUDlSVTNMWTdTUUJCWkpKUk1ST0YxMkszMUJXQkJSQ0tOSzg0WDRDS1VV
	CodeChallenge: scoOckF2se3sBkgRPI5U6bol2n5fQVOoC3btjRXbIVo```

+ => URL to start authorization code flow: used params: `(response_type, code_challenge, code_challenge_method, client_id, redirect_uri)` \
	http://127.0.0.1:8000/o/authorize/?response_type=code&code_challenge=scoOckF2se3sBkgRPI5U6bol2n5fQVOoC3btjRXbIVo&code_challenge_method=S256&client_id=jQgcqIptu1rCiWBkZALczHeojozazD37FIGjHsBN&redirect_uri=http://127.0.0.1:8000/noexist/callback

+ => Authorize App 1 the scopes: Reading scope, Writing scope by clicking authorize button.

+ => Recieved CODE: `FjNx4TjskQQj1liTFWRD5TcN4OcfhC` (Get it from the url-parameter)

+ => Make http request with `clientId, clientSecret, code & codeVerifier` to get Bearer+Refresh tokens. \
	**Note:** Make sure client and server time zone are same (django settings + http-client)
```
curl -X POST \
    -H "Cache-Control: no-cache" \
    -H "Content-Type: application/x-www-form-urlencoded" \
    "http://127.0.0.1:8000/o/token/" \
    -d "client_id=${ID}" \
    -d "client_secret=${SECRET}" \
    -d "code=${CODE}" \
    -d "code_verifier=${CODE_VERIFIER}" \
    -d "redirect_uri=http://127.0.0.1:8000/noexist/callback" \
    -d "grant_type=authorization_code"
```

+ => Recieved response should look like: \
	```
  {
	  "access_token": "<some_token>",
	  "expires_in": 36000,
	  "token_type": "Bearer",
	  "scope": "read write",
	  "refresh_token": "<some_refresh_token>"
	}
  ```

