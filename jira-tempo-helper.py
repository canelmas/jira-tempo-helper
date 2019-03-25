from datetime import datetime
import os
import requests
from dateutil.relativedelta import relativedelta
from flask import Flask
import json

app = Flask(__name__)

base_url = os.environ["JIRA_REST_URL"]
headers = {"Accept": "application/json",
           "Authorization": "Basic {}".format(os.environ["JIRA_AUTH_TOKEN"])}
DATE_FORMAT = "%Y-%m-%d"


@app.route("/hometeam/<author>")
def home_team(author):
    from_ = datetime.now() - relativedelta(years=3)

    data = get("/tempo-teams/2/teammember/{}/memberships?from={}&to={}".format(author,
                                                                               from_.strftime(
                                                                                   DATE_FORMAT),
                                                                               datetime.now().strftime(DATE_FORMAT)))

    home_team = []
    for info in data:
        team_name = info["team"]["name"]
        if team_name.startswith("DT "):
            home_team.append({"key": info["team"]["id"], "value": team_name})
            break

    return json.dumps({"values": home_team})


@app.route("/users/<author>/teams")
def teams(author):
    data = get("/tempo-teams/2/user/{}/memberships".format(author))

    return json.dumps(data)


def get(url, params=None):
    r = requests.get(base_url + url,
                     params=params,
                     headers=headers)
    r.raise_for_status()
    return r.json()


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=False, port=80)
