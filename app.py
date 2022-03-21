from flask import Flask, render_template, request, session

app = Flask(__name__)


@app.route('/')
def render_homepage():
    return render_template("home.html")

@app.route('/menu')
def render_menu():
    products_list = [["Flat white", "Definitely created in New Zealand (not in the West Island) - a classic.", "180mL", "flatwhite", "4.00"],
                     ["Latte", "The New Zealand latte is larger than a flat white and has more foamy milk.", "240mL", "latte", "4.00"],
                     ["Espresso", "Straight from the machine", "60mL including crema.", "60mL", "espresso", "3.00"],
                     ["Long black", "Hot water + espresso.", "120mL.", "90mL", "longblack", "3.00"],
                     ["Chemex (filter)", "The most beautiful pourover method, in our opinion. The thicker chemex removes most of the oils from the coffee, giving a lighter mouthfeel. We brew our pourovers with a 1:16 ratio.", "400mL", "chemex", "5.00"],
                     ["V60 (filter)", "The least forgiving pourover methody, but the most delicious when you get it right. We use tabbed filters, deal with it! We brew our pourovers with a 1:16 ratio.", "600mL", "v60", "5.00"],
                     ["Aeropress", "Probably the youngest coffee brewing method, the aeropress combines immersion, filter. Try it to find out why the Aeropress has a cult following, and its own World Championship. We're continually tweaking our process but use about a 1:12 ratio at the moment", "200mL", "aeropress", "5.00"],
                     ["Cafetière", "In New Zealand this is normally referred to as ""plunger coffee"" but we associate a plunger with a blocked toilet so we use the European name. We use a relatively long brew process and never actually 'plunge'.", "600mL", "plunger", "8.00"],
                     ["Moka", "Espresso-style coffee brewed by pressurising water (with steam) to pass it through coffee. We serve ours latte-style, with steamed milk.", "240mL", "moka", "4.00"],
                     ["Hot chocolate", "We use a sugar-free Galaxy hot chocolate, served with marshmallows or chocloate fish (depending on what we have in the pantry)." ,"240mL", "hotchoc", "4.00"],
                     ["Cold brew", "Coarse-ground coffee, soaked for 24 hours and then double strained. We use a mesh filter and then a chemex filter to create a light mouthfeel.", "300mL", "coldbrew", "4.50"]]
    return render_template("menu.html", products=products_list)

@app.route('/contact')
def render_contact():
    return render_template("contact.html")

@app.route('/login')
def render_login():
    return render_template("login.html")

app.run(host="0.0.0.0")
