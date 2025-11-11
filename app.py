from flask import Flask, render_template, request, send_file
import os
from datetime import datetime

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['REPORT_FOLDER'] = 'reports'

# Ensure folders exist
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['REPORT_FOLDER'], exist_ok=True)


def analyze_ewaste(filename):
    """Simulated AI analysis for demonstration."""
    name = filename.lower()

    if "pcb" in name or "board" in name:
        useful = ["Copper", "Gold", "Silver"]
        hazard = ["Lead", "Mercury"]
    elif "battery" in name:
        useful = ["Lithium", "Cobalt"]
        hazard = ["Acid", "Nickel"]
    elif "phone" in name or "mobile" in name:
        useful = ["Gold", "Plastic", "Glass"]
        hazard = ["Lead", "Brominated Flame Retardants"]
    else:
        useful = ["Plastic", "Metal parts"]
        hazard = ["Unknown chemicals"]

    return useful, hazard


def get_disposal_info(hazard_list):
    """Return safe disposal information for each hazardous material."""
    info = {
        "Lead": "Take to authorized e-waste recycling centers. Never dispose of in household trash or burn.",
        "Mercury": "Place in sealed, labeled containers. Hand over to certified hazardous waste handlers.",
        "Acid": "Never pour down drains. Return to battery recycling or authorized hazardous waste facilities.",
        "Nickel": "Can be recycled by licensed metal recyclers. Avoid landfill disposal.",
        "Brominated Flame Retardants": "Take to authorized facilities for controlled disposal. Do not incinerate openly.",
        "Unknown chemicals": "Consult authorized e-waste management services for safe disposal.",
    }
    return {h: info.get(h, "Consult certified e-waste facility for disposal.") for h in hazard_list}


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload():
    if 'image' not in request.files:
        return "No file uploaded", 400

    file = request.files['image']
    if file.filename == '':
        return "No selected file", 400

    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(filepath)

    # Analyze e-waste
    useful, hazard = analyze_ewaste(file.filename)
    disposal_info = get_disposal_info(hazard)

    # Create report with disposal details
    report_name = f"report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    report_path = os.path.join(app.config['REPORT_FOLDER'], report_name)

    with open(report_path, 'w') as f:
        f.write("==============================================\n")
        f.write("      CMRIT E-WASTE ANALYSIS REPORT\n")
        f.write("==============================================\n")
        f.write("Institution: CMR Institute of Technology, Bengaluru\n")
        f.write("Department: Computer Science & Engineering\n")
        f.write(f"Analyzed File: {file.filename}\n")
        f.write(f"Report Generated: {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}\n")
        f.write("==============================================\n\n")

        f.write("🔹 Useful Materials:\n")
        for u in useful:
            f.write(f"   - {u}\n")

        f.write("\n🔸 Hazardous Materials:\n")
        for h in hazard:
            f.write(f"   - {h}\n")

        f.write("\n♻️ Safe Disposal Guidelines:\n")
        for h, tip in disposal_info.items():
            f.write(f"   - {h}: {tip}\n")

        f.write("\n==============================================\n")
        f.write("Note: Always follow authorized e-waste disposal procedures.\n")
        f.write("Developed by: Chethan,Charan,Sandeep (7th Sem, CSE)\n")
        f.write("Guided by: Kashif sir, CMRIT Bengaluru\n")
        f.write("==============================================\n")

    return render_template(
        'index.html',
        useful=useful,
        hazard=hazard,
        disposal=disposal_info,
        report=report_path
    )


@app.route('/download/<path:filename>')
def download(filename):
    return send_file(filename, as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True)
