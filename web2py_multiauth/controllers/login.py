#############################################################################
# $Date:$
# $Rev:$
# $Author:$
# $URL:$
#############################################################################

def login():
    if not auth.is_logged_in():
        #@TODO: if there is no next on the request we end up doing a bunch more
        #redirects than we need to.  this needs to be fixed.
        login_form = auth.login(next=full_url('http',r=request))
        return response.render('login_area.html', dict(login_form=login_form))
    else:
        redirect(full_url('http', r=request, a='tenthrow', c='default', f='index' ))

