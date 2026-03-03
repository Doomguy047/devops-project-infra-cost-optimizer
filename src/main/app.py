from cost_engine import analyze_costs
from report_generator import generate_html_report


def main():
    recommendations = analyze_costs()
    generate_html_report(recommendations)
    print("Cost analysis complete. Report generated: cost-report.html")


if __name__ == "__main__":
    main()
