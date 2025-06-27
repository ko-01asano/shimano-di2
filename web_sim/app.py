from flask import Flask, render_template, request

app = Flask(__name__)

# Air density at sea level (kg/m^3)
RHO = 1.225

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/simulate', methods=['POST'])
def simulate():
    try:
        velocity = float(request.form.get('velocity', 0))
        area = float(request.form.get('area', 0))
        drag_coeff = float(request.form.get('drag_coeff', 0))
    except ValueError:
        return render_template('index.html', error="Invalid input")

    drag_force = 0.5 * RHO * drag_coeff * area * velocity ** 2
    return render_template(
        'index.html',
        result=f"Estimated drag force: {drag_force:.2f} N",
        velocity=velocity,
        area=area,
        drag_coeff=drag_coeff,
    )

if __name__ == '__main__':
    app.run(debug=True)
