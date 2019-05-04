from flask import request, render_template, redirect, url_for, flash
from app import app
import Solarise_API
import Solarise_API.utils.jwt_helpers

if __name__ == '__main__':
    app.run(debug=True)
