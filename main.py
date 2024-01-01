from flask import Flask, render_template, request, redirect, send_file
from extractors.wanted import extract_wanted_jobs
from extractors.remoteok import extract_remoteOK_jobs
from file import save_to_file



app = Flask("JobScrapper")

db = {}


@app.route("/")
def home():
  return render_template("home.html")


@app.route("/search")
def search():
  keyword = request.args.get("keyword")
  if keyword == None:
    return redirect("/")

  if keyword == "":
    return redirect("/")

  if keyword in db:
    jobs = db[keyword]
  else:
    wanted = extract_wanted_jobs(keyword)
    remoteok = extract_remoteOK_jobs(keyword)
    jobs = wanted + remoteok
    app.logger.info("Extracted jobs: %s", jobs)
    db[keyword] = jobs
  return render_template("search.html", keyword=keyword, jobs=jobs)

@app.route("/export")
def export():
  keyword = request.args.get("keyword")
  if keyword == None:
    return redirect("/")
  if keyword not in db:
    return redirect(f"/search?keyword={keyword}")
  save_to_file(keyword, db[keyword])
  return send_file(f"{keyword}.csv", as_attachment=True)



if __name__ == '__main__':
    app.run(debug=True)