from flask import render_template, request

from manage import app, db, mongo, the_immig_gh, the_ec_gh, the_healthinsure_gh


def add_citizens():
    citizen_1 = the_ec_gh(
        first_name="Kwadwo",
        other_name="Adu",
        last_name="Boakye-Yiadom",
        address="13th Tontre Avenue North Gbawe",
        age=22
    )
    citizen_2 = the_immig_gh(
        first_name="Kwadwo",
        other_name="Adu",
        last_name="Boakye-Yiadom",
        address="13th Tontre Avenue North Gbawe",
        age=22
    )
    citizen_3 = the_healthinsure_gh(
        first_name="Kwadwo",
        other_name="Adu",
        last_name="Boakye-Yiadom",
        address="13th Tontre Avenue North Gbawe",
        age=22
    )
    citizen_4 = {
        "first_name": "Kwadwo",
        "other_name": "Adu",
        "last_name": "Boakye-Yiadom",
        "address": "13th Tontre Avenue North Gbawe",
        "age": "22",
    }

    db.session.add(citizen_1)  # Adds new User record to database
    db.session.add(citizen_2)  # Adds new User record to database
    db.session.add(citizen_3)  # Adds new User record to database
    db.session.commit()
    mongo.db.database_dvla.insert(citizen_4)


@app.route('/', methods=['GET', 'POST'])
def index():
    errors = []

    # add_citizens()
    if request.method == "POST":
        first_name = request.form['first_name']
        last_name = request.form['last_name']

        if first_name and last_name:
            results_EC= the_ec_gh.query.filter_by(first_name=first_name, last_name=last_name).all()
            results_GIS = the_immig_gh.query.filter_by(first_name=first_name, last_name=last_name).all()
            results_NHIA = the_healthinsure_gh.query.filter_by(first_name=first_name, last_name=last_name).all()

            citizens = mongo.db.database_dvla
            results_DVLA_1 = []
            for c in citizens.find():
                results_DVLA_1.append(
                    {'first_name': c['first_name'], 'other_name': c['other_name'], 'last_name': c['last_name'],
                     'address': c['address'],
                     'age': c['age']})

            results_DVLA = []
            for citizen in results_DVLA_1:
                if citizen['first_name'] == first_name and citizen['last_name'] == last_name:
                    results_DVLA.append(
                        {'first_name': citizen['first_name'], 'other_name': citizen['other_name'],
                         'last_name': citizen['last_name'], 'address': citizen['address'],
                         'age': citizen['age']})

            return render_template('result.html', results_EC=results_EC, results_GIS=results_GIS,
                                   results_NHIA=results_NHIA, results_DVLA=results_DVLA)
        else:
            errors = {"error": "The request payload is not in JSON format"}

    return render_template('index.html', errors=errors)


@app.route('/result', methods=['GET', ])
def result():
    return render_template('result.html')


if __name__ == "__main__":
    app.run()
