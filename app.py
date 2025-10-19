from flask import Flask, render_template, request
import sympy as sp
import numpy as np
import plotly.graph_objs as go
import plotly.offline as pyo

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    plot_div = None
    functions = []
    x_vals = []
    y_vals = []
    action = request.form.get("action", "")
    a = float(request.form.get("a", 0))
    b = float(request.form.get("b", 1))

    x = sp.symbols("x")

    # Collect all function inputs
    i = 0
    while True:
        func_str = request.form.get(f"function_{i}")
        if not func_str:
            break
        try:
            f = sp.sympify(func_str, locals={"x": x})
            f_lambdified = sp.lambdify(x, f, modules=["numpy"])
            x_range = np.linspace(a, b, 400)
            y_range = f_lambdified(x_range)
            functions.append((func_str, x_range, y_range))
        except Exception as e:
            print(f"Error with function {func_str}: {e}")
        i += 1

    # Plot using Plotly
    traces = []
    for idx, (label, x_range, y_range) in enumerate(functions):
        traces.append(go.Scatter(x=x_range, y=y_range, mode='lines', name=f"f{idx}(x) = {label}"))

    layout = go.Layout(
        title="Graph of Entered Function(s)",
        xaxis=dict(
            zeroline=True,
            zerolinewidth=2,
            zerolinecolor='black',
            showline=True,
            linecolor='black',
            mirror=True,
            ticks='outside',
            showgrid=True,
            gridcolor='lightgray',
            tickfont=dict(size=12)
        ),
        yaxis=dict(
            zeroline=True,
            zerolinewidth=2,
            zerolinecolor='black',
            showline=True,
            linecolor='black',
            mirror=True,
            ticks='outside',
            showgrid=True,
            gridcolor='lightgray',
            tickfont=dict(size=12)
        ),
        plot_bgcolor='white',
        margin=dict(t=40, b=40, l=40, r=40),
        width=800,
        height=500,
        showlegend=False
    )

    # 👇 These go AFTER the layout, not inside it
    fig = go.Figure(data=traces, layout=layout)
    plot_div = pyo.plot(fig, output_type='div')

    return render_template("index.html", plot_div=plot_div, num_functions=i)

if __name__ == "__main__":
    app.run(debug=True)
