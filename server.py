from flask import Flask, render_template, request
from typograf import apply_rule_to_test
app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
def form():
    if request.method == 'POST':
        input_text = request.form.get('text')
        if not input_text:
            print('Ничего не введено')
        output_text = apply_rule_to_test(input_text)
        return render_template(
            'form.html',
            raw_text=input_text,
            processed_text=output_text)
    else:
        return render_template('form.html')

if __name__ == "__main__":
    app.run()
