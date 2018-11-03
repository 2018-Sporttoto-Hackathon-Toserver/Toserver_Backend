from flask import Blueprint, request as req, jsonify
from Server.utils import utils
from Server.mysql import db, Site
from datetime import datetime
import os

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













