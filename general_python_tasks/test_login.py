def google_login(request):
    token_request_uri = "https://accounts.google.com/o/oauth2/auth"
    response_type = "code"
    client_id = '440710361292-olcog70jbfqf0if3s2emo9s4tc0jvet5.apps.googleusercontent.com'
    redirect_uri = "http://localhost"
    scope = "https://www.googleapis.com/auth/userinfo.profile https://www.googleapis.com/auth/userinfo.email"
    url = "{token_request_uri}?response_type={response_type}&client_id={client_id}&redirect_uri={redirect_uri}&scope={scope}".format(
        token_request_uri = token_request_uri,
        response_type = response_type,
        client_id = client_id,
        redirect_uri = redirect_uri,
        scope = scope)
    return HttpResponseRedirect(url)


def google_authenticate(request):
    parser = Http()
    login_failed_url = '/'
    if 'error' in request.GET or 'code' not in request.GET:
        return HttpResponseRedirect('{loginfailed}'.format(loginfailed = login_failed_url))

    access_token_uri = 'https://accounts.google.com/o/oauth2/token'
    redirect_uri = "http://localhost"
    params = urllib.urlencode({
        'code':request.GET['code'],
        'redirect_uri':redirect_uri,
        'client_id':'440710361292-olcog70jbfqf0if3s2emo9s4tc0jvet5.apps.googleusercontent.com',
        'client_secret':'xiAuWzWElCx11dSvGM434l54',
        'grant_type':'authorization_code'
    })
    headers={'content-type':'application/x-www-form-urlencoded'}
    resp, content = parser.request(access_token_uri, method = 'POST', body = params, headers = headers)
    token_data = jsonDecode(content)
    resp, content = parser.request("https://www.googleapis.com/oauth2/v1/userinfo?access_token={accessToken}".format(accessToken=token_data['access_token']))
    #this gets the google profile!!
    google_profile = jsonDecode(content)
    #log the user in-->
    #HERE YOU LOG THE USER IN, OR ANYTHING ELSE YOU WANT
    #THEN REDIRECT TO PROTECTED PAGE
    return HttpResponseRedirect('/dashboard')