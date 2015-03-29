import os
import webapp2
import jinja2
from google.appengine.ext import db
from random import randint
import time

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)

class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)
    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)
    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))
        
#databases

class Survey(db.Model):
    vam_id = db.StringProperty()
    subject = db.StringProperty(required = True)
    description = db.StringProperty(required = True)
    created = db.DateTimeProperty(auto_now_add = True)
    q1 = db.StringProperty(required = True)
    o11 = db.StringProperty(required = True)
    o12 = db.StringProperty(required = True)
    o13 = db.StringProperty(required = True)
    q2 = db.StringProperty(required = True)
    o21 = db.StringProperty(required = True)
    o22 = db.StringProperty(required = True)
    o23 = db.StringProperty(required = True)
    q3 = db.StringProperty(required = True)
    o31 = db.StringProperty(required = True)
    o32 = db.StringProperty(required = True)
    o33 = db.StringProperty(required = True)
    q4 = db.StringProperty(required = True)
    o41 = db.StringProperty(required = True)
    o42 = db.StringProperty(required = True)
    o43 = db.StringProperty(required = True) 
    q5 = db.StringProperty(required = True)
    o51 = db.StringProperty(required = True)
    o52 = db.StringProperty(required = True)
    o53 = db.StringProperty(required = True)

class Votes(db.Model):
    vam_id = db.StringProperty(required = True)
    q1_opt = db.StringProperty(required = True)
    q2_opt = db.StringProperty(required = True)
    q3_opt = db.StringProperty(required = True)
    q4_opt = db.StringProperty(required = True)
    q5_opt = db.StringProperty(required = True)
        



class MainPage(Handler):
    def get(self):
        self.render("homepage.html")
        
class NewSurvey(Handler):
    def get(self):
        self.render("newsurvey.html")
    def post(self):
        vam_id = str(randint(1, 500))
        subject = self.request.get("title")
        description = self.request.get("description")
        q1 = self.request.get("q1")
        o11 = self.request.get("o11")
        o12 = self.request.get("o12")
        o13 = self.request.get("o13")
        q2 = self.request.get("q2")
        o21 = self.request.get("o21")
        o22 = self.request.get("o22")
        o23 = self.request.get("o23")
        q3 = self.request.get("q3")
        o31 = self.request.get("o31")
        o32 = self.request.get("o32")
        o33 = self.request.get("o33")
        q4 = self.request.get("q4")
        o41 = self.request.get("o41")
        o42 = self.request.get("o42")
        o43 = self.request.get("o43") 
        q5 = self.request.get("q5")
        o51 = self.request.get("o51")
        o52 = self.request.get("o52")
        o53 = self.request.get("o53")
        
        a = Survey(vam_id = vam_id, subject = subject, description = description, q1 = q1,
                    o11 = o11, o12 = o12, o13 = o13, q2 = q2,
                    o21 = o21, o22 = o22, o23 = o23, q3 = q3,
                    o31 = o31, o32 = o32, o33 = o33, q4 = q4,
                    o41 = o41, o42 = o42, o43 = o43, q5 = q5,
                    o51 = o51, o52 = o52, o53 = o53)
        a.put()      

        self.render("thanx.html")    
        
class Existing(Handler):
    def get(self):
        surveys = Survey.all()
        self.render("existingsurvey.html", surveys = surveys)
        
class PermaSurvey(Handler):
    def get(self):
        vam = self.request.get("vam_id")
        su = Survey.all().filter("vam_id =", vam).get()
        self.render("perma.html", su = su)
    def post(self):
        vam = self.request.get("vam_id")
        q1_opt = self.request.get("q1")
        q2_opt = self.request.get("q2")
        q3_opt = self.request.get("q3")
        q4_opt = self.request.get("q4")
        q5_opt = self.request.get("q5")
        
        v = Votes(vam_id = vam, q1_opt = q1_opt, q2_opt = q2_opt, q3_opt = q3_opt,
                    q4_opt = q4_opt, q5_opt = q5_opt)  
        v.put()
        time.sleep(1)
        
        a = Survey.all().filter("vam_id = ", vam).get()
        q1 = a.q1
        q2 = a.q2
        q3 = a.q3
        q4 = a.q4
        q5 = a.q5
        o11 = a.o11
        b = Survey.all().filter("vam_id = ", vam).get()
        o12 = b.o12
        c = Survey.all().filter("vam_id = ", vam).get()
        o13 = c.o13
        p = Survey.all().filter("vam_id = ", vam).get()
        o21 = p.o21
        d = Survey.all().filter("vam_id = ", vam).get()
        o22 = a.o22
        e = Survey.all().filter("vam_id = ", vam).get()
        o23 = e.o23
        f = Survey.all().filter("vam_id = ", vam).get()
        o31 = f.o31
        g = Survey.all().filter("vam_id = ", vam).get()
        o32 = g.o32
        h = Survey.all().filter("vam_id = ", vam).get()
        o33 = h.o33
        i = Survey.all().filter("vam_id = ", vam).get()
        o41 = i.o41
        j = Survey.all().filter("vam_id = ", vam).get()
        o42 = j.o42
        k = Survey.all().filter("vam_id = ", vam).get()
        o43 = k.o43
        l = Survey.all().filter("vam_id = ", vam).get()
        o51 = l.o51
        m = Survey.all().filter("vam_id = ", vam).get()
        o52 = m.o52
        n = Survey.all().filter("vam_id = ", vam).get()
        o53 = n.o53
		
        count_11 = Votes.all().filter("vam_id = ", vam).filter("q1_opt = ", o11).count()
        count_12 = Votes.all().filter("vam_id = ", vam).filter("q1_opt = ", o12).count()
        count_13 = Votes.all().filter("vam_id = ", vam).filter("q1_opt = ", o13).count()
        count_21 = Votes.all().filter("vam_id = ", vam).filter("q2_opt = ", o21).count()
        count_22 = Votes.all().filter("vam_id = ", vam).filter("q2_opt = ", o22).count()
        count_23 = Votes.all().filter("vam_id = ", vam).filter("q2_opt = ", o23).count()
        count_31 = Votes.all().filter("vam_id = ", vam).filter("q3_opt = ", o31).count()
        count_32 = Votes.all().filter("vam_id = ", vam).filter("q3_opt = ", o32).count()
        count_33 = Votes.all().filter("vam_id = ", vam).filter("q3_opt = ", o33).count()
        count_41 = Votes.all().filter("vam_id = ", vam).filter("q4_opt = ", o41).count()
        count_42 = Votes.all().filter("vam_id = ", vam).filter("q4_opt = ", o42).count()
        count_43 = Votes.all().filter("vam_id = ", vam).filter("q4_opt = ", o43).count()
        count_51 = Votes.all().filter("vam_id = ", vam).filter("q5_opt = ", o51).count()
        count_52 = Votes.all().filter("vam_id = ", vam).filter("q5_opt = ", o52).count()
        count_53 = Votes.all().filter("vam_id = ", vam).filter("q5_opt = ", o53).count()
        
        self.render("vis.html", q1 = q1, o11 = o11, o12 = o12, o13 = o13,
              count_11 = count_11, count_12 = count_12, count_13 = count_13,
              q2 = q2, o21 = o21, o22 = o22, o23 = o23,
              count_21 = count_21, count_22 = count_22, count_23 = count_23,
              q3 = q3, o31 = o31, o32 = o32, o33 = o33,
              count_31 = count_31, count_32 = count_32, count_33 = count_33,
              q4 = q4, o41 = o41, o42 = o42, o43 = o43,
              count_41 = count_41, count_42 = count_42, count_43 = count_43,
              q5 = q5, o51 = o51, o52 = o52, o53 = o53,
              count_51 = count_51, count_52 = count_52, count_53 = count_53)
              
app = webapp2.WSGIApplication([('/', MainPage),
                               ('/new', NewSurvey),
                               ('/existing', Existing),
                               ('/perma', PermaSurvey)], debug=True)