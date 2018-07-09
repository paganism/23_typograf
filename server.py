from flask import Flask, render_template, request
from flask_wtf.csrf import CSRFProtect
from typograf import apply_rule_to_text
import logging


logging.basicConfig(level=logging.INFO)
app = Flask(__name__)
csrf = CSRFProtect(app)
app.config['SECRET_KEY'] = 'lemon wedges'


@app.route('/', methods=['POST', 'GET'])
def form():
    if request.method == 'POST':
        input_text = request.form.get('text')
        if not input_text:
            app.logger.info('Ничего не введено')
        output_text = apply_rule_to_text(input_text)
        return render_template(
            'form.html',
            raw_text=input_text,
            processed_text=output_text)
    else:
        return render_template('form.html')


if __name__ == "__main__":
    app.run()
