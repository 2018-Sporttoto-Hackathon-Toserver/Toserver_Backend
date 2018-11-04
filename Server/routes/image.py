from flask import Blueprint, request as req, jsonify
from Server.utils import utils
from Server.mysql import db, Site
from datetime import datetime
import os

check = False

app = Blueprint('image', __name__)

@app.route('/', methods=['GET'])
def image_main():
    return "<h1>Image Route</h1>"


@app.route('/check', methods=['POST'])
def image_check():

    r_url = req.form['url']

    time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    db_site = Site.query.filter_by(url=r_url).first()

    if db_site != None:
        site = db_site.serialize

        return_data = {
            "count" : site["count"],
            "check" : site["check"],
            "time" : time
        }

        return jsonify(return_data), 200

    else:

        state_data, count = utils.crawling(r_url)

        site = Site(r_url, count, time, state_data)

        db.session.add(site)
        db.session.commit()

        return_data = {
            "check": state_data,
            "count": count,
            "time": time,
        }

        return jsonify(return_data)

    # if check == False:
    #     check = True
    #     return_data = {
    #             "check": True,
    #             "count": 18,
    #             "time": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
    #         }
    #
    # else :
    #     return_data = {
    #         "check": False,
    #         "count": 0,
    #         "time": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
    #     }
    #
    # return return_data

@app.route('/excel', methods=['POST'])
def excel():

    return_data = []

    db_site = Site.query.all()

    # sites = db_site.serialize_list(db_site)

    for i in db_site:
        return_data.append(i.serialize)

    #sites = db_site.serialize

    # print(sites)
    print(return_data)

    return jsonify(return_data)

















