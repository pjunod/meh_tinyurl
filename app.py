from flask import Flask, make_response, request, redirect, Response,\
    render_template
import logging
import pprint
import random
import string

import manage_urls
from db import create_tables


app = Flask(__name__)

server = "http://127.0.0.1:5000"
prefix = "u"


@app.route("/create/<string:url>")
def create_url(url):
    short_url = ''.join(random.choices(string.ascii_lowercase, k=8))
    res = manage_urls.create_url(url, short_url)
    if res is True:
        response = make_response(f"{server}/{prefix}/{short_url}", 201)
        return response
    else:
        response = make_response("Error inserting url into database", 500)
        return response


@app.route("/u/<string:url>")
def redir_url(url):
    res = manage_urls.get_url(url)
    if len(res) == 1:
        reslist = [row[0] for row in res]
        redir = reslist[0]
        app.logger.info("reslist is [%s]" % reslist)
        resp_url = f"https://{redir}"
        return redirect(resp_url, code=302)
    else:
        return Response("Error URL not found", 404)


@app.route("/admin/debug")
def do_debug():
    resp = pprint.pformat(request.environ, depth=5)
    return Response(resp, mimetype="text/text")


@app.route("/admin/urllist")
def list_urls():
    url_list = manage_urls.get_urllist()
    app.logger.info("db list is:")
    for row in url_list:
        app.logger.info(row)
    return render_template('admin.html', data=url_list)


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    create_tables()
    app.run(host='127.0.0.1', port=5000, debug=False)
