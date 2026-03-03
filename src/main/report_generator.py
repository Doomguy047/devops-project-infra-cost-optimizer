def generate_html_report(recommendations):
    with open("cost-report.html", "w") as f:
        f.write("<html>")
        f.write("<head><title>Cost Optimization Report</title></head>")
        f.write("<body>")
        f.write("<h1>Infrastructure Cost Optimization Report</h1>")
        f.write("<ul>")

        for rec in recommendations:
            f.write(f"<li>{rec}</li>")

        f.write("</ul>")
        f.write("</body>")
        f.write("</html>")
