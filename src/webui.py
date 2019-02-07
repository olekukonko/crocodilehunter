#!/usr/bin/env python3
from flask import Flask, Response, render_template, redirect, url_for

class Webui:
    def __init__(self, watchdog):
        self.app = Flask(__name__)
        self.watchdog = watchdog

    def start_daemon(self):
        print(f"\b* Starting WebUI")

        #Add each endpoint manually
        self.add_endpoint("/", "index", self.index)
        self.add_endpoint("/check_all", "checkall", self.calculate_all)
        self.add_endpoint("/check_all", "checkall", self.calculate_all)

        self.app.run()

    def index(self):
        return render_template('index.html', name=self.watchdog.project_name,
                               towers=self.watchdog.get_all_by_suspicioussnes())
    def calculate_all(self):
        self.watchdog.calculate_all()
        return redirect(url_for('index'))

    def detail(self):
        self.watchdog.calculate_all()
        return redirect(url_for('index'))

    def add_endpoint(self, endpoint=None, endpoint_name=None, handler=None):
        self.app.add_url_rule(endpoint, endpoint_name, EndpointAction(handler))


class EndpointAction(object):

    def __init__(self, action):
        self.action = action

    def __call__(self, *args):
        action = self.action()
        response = Response(action, status=200, headers={})
        return response
