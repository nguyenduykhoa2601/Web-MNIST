from flask import Flask, render_template, request, jsonify, send_from_directory
from flask_bootstrap import Bootstrap
from helpers.image_preprocessing import ImageProcessor
from helpers.tensorflow_model import TensorflowModel
import os


app = Flask(__name__)
bootstrap = Bootstrap(app)
model = TensorflowModel('./model/cnn_model.h5')


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        image_url = request.values['imgBase64']

        processor = ImageProcessor(image_url)
        prepared_image = processor.prepare_image_for_evaluation()

        prediction = model.predict(prepared_image)

        return jsonify(prediction=str(prediction))

    return render_template('routes/home.html')


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico')


@app.errorhandler(404)
def not_found_error(error):
    return render_template('errors/error_404.html'), 404


@app.errorhandler(403)
def forbidden_error(error):
    return render_template('errors/error_403.html'), 403


@app.errorhandler(500)
def internal_error(error):
    return render_template('errors/error_500.html'), 500


if __name__ == '__main__':
    app.run()