from flask import Flask, render_template, request
from random import randint
app = Flask(__name__)

count=0
reponse=0
prenom=""
nom=""

@app.route('/')
def index():
	count=0
	return render_template("index.html", error="")




@app.route('/formcheck', methods=["POST"])
def formcheck():
	global count, reponse, prenom, nom

	if count == 0:
		prenom = request.form.get("prenom") 
		nom = request.form.get("nom")
		email = request.form.get("email")
		if "" in [prenom, nom, email]:
			return render_template("index.html", error="Veuillez remplir tous les champs !")
		else:
			global num1, num2, operation
			num1 = randint(0, 10)
			num2 = randint(0, 10)
			operation = ["+", "-", "x"][randint(0, 2)]
			if operation == "+":
				reponse = num1 + num2
			elif operation == "-":
				reponse = num1 - num2
			elif operation == "x":
				reponse = num1 * num2
			count += 1
			return render_template("bienvenue.html", nom=nom, prenom=prenom, num1=num1, operation=operation, num2=num2, form=True, msg="")
	elif 0 < count <= 5:
		is_right = False
		if request.form.get("number") is not None and request.form.get("number")!="":	
			is_right = int(request.form.get("number")) == reponse
		if is_right:
			temp_count = count
			count=0	
			return render_template("bienvenue.html", nom=nom, prenom=prenom, num1=num1, operation=operation, num2=num2, msg="Félicitations, vous avez trouvé la réponse en : " +str(temp_count)+" essais", form=False)
		else:
			if count == 5:
				count = 0
				return render_template("bienvenue.html", nom=nom, prenom=prenom, num1=num1, operation=operation, num2=num2, msg="Vous avez atteint un max de 5 essais", form=False)
			count += 1
			return render_template("bienvenue.html", nom=nom, prenom=prenom, num1=num1, operation=operation, num2=num2, form=True, msg="Réponse fausse réeassayez")
	