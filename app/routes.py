from flask import Blueprint, render_template, request

from app.ml.model import predict_url

from app import db
from app.models import ScanHistory


main = Blueprint("main", __name__)



@main.route("/")
def home():
    return render_template("index.html")



@main.route("/scan", methods=["POST"])
def scan():

    url = request.form.get("url")


    if not url:
        return "No URL provided"



    ai_result = predict_url(url)



    result = {
        "url": url,
        "score": ai_result["score"],
        "risk": ai_result["risk"],
        "message": ai_result["message"]
    }



    scan = ScanHistory(
        url=url,
        risk=ai_result["risk"],
        score=ai_result["score"]
    )


    db.session.add(scan)
    db.session.commit()



    return render_template(
        "result.html",
        result=result
    )



@main.route("/history")
def history():

    scans = ScanHistory.query.order_by(
        ScanHistory.date.desc()
    ).all()


    return render_template(
        "history.html",
        scans=scans
    )



@main.route("/dashboard")
def dashboard():

    total = ScanHistory.query.count()


    safe = ScanHistory.query.filter_by(
        risk="Safe"
    ).count()


    malicious = ScanHistory.query.filter_by(
        risk="Malicious"
    ).count()



    scans = ScanHistory.query.all()


    if total > 0:

        avg_score = sum(
            scan.score for scan in scans
        ) / total

    else:

        avg_score = 0



    return render_template(
        "dashboard.html",
        total=total,
        safe=safe,
        malicious=malicious,
        avg_score=int(avg_score)
    )