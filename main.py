import webapp2

MAIN_PAGE_HTML = """\
<!DOCTYPE HTML>
<html>
  <head>
      <title>jdMirror</title>
      <meta name="description" content="Atomi J.D. Mirror App" />
      <meta name="keywords" content="bath mirror traffic weather" />
      <meta http-equiv="content-type" content="text/html; charset=UTF-8" />
      <link rel="stylesheet" type="text/css" href="jd.css" title="style" />

  </head>
  <body>
    <div id="site_content">
      <div class="sidebar">
        <h3><script> document.write(new Date().toLocaleDateString()); </script></h3>
        <h2>Nachricht</h2>
        <p>Heute ist alles gut, wir habe es geschafft. Bitte alle zum Feiern vorbeikommen.</p>
        <p></p>
        <h2>Nachricht</h2>
        <p>Heute ist alles gut, wir habe es geschafft. Bitte alle zum Feiern vorbeikommen.</p>        
        <div id="cont_33774d8518cfc09d18e9a3e1941165e5"><script type="text/javascript" async src="https://www.daswetter.com/wid_loader/33774d8518cfc09d18e9a3e1941165e5"></script></div>
      </div>
      <div id="content">
        <h1>Weg zur Arbeit</h1>
        <p>Heute sehr lang!</p>
        <iframe width="600" height="450" frameborder="0" style="border:0" src="https://www.google.com/maps/embed/v1/directions?origin=place_id:Ei9SYXRoYXVzc3RyYcOfZSAxNiwgNjQ1NzkgR2VybnNoZWltLCBEZXV0c2NobGFuZA&destination=place_id:ChIJs47CqO9wvUcRI5dCwz58MgA&key=AIzaSyB6lf-HXqFsjQXfjB3Yh4loH-xzMHsyzYI" allowfullscreen></iframe>        
      </div>
      <div id="footer">
        <p></p>      
        <h1>Achim, Du siehst fantastisch aus!</h1>
      </div>
    </div>      
  </body>
</html>
"""

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.write(MAIN_PAGE_HTML)

app = webapp2.WSGIApplication([
    ('/', MainPage)
], debug=True)
