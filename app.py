from flask import Flask, request, send_file
from rembg import remove
from io import BytesIO
from PIL import Image

app = Flask(__name__)


@app.route('/')
def index():
    return "Rembg API is running."


@app.route("/remove-bg", methods=["POST"])
def remove_bg():
    print("Received request")

    if "file" not in request.files:
        print("No file part in the request")
        return {"error": "No file part"}, 400

    file = request.files["file"]

    if file.filename == "":
        print("No selected file")
        return {"error": "No selected file"}, 400

    try:
        # Read the image file
        img = Image.open(file.stream)
        print("Image file opened")

        # Remove the background
        output = remove(img)
        print("Background removed")

        # Save to a BytesIO object
        img_io = BytesIO()
        output.save(img_io, "PNG")
        img_io.seek(0)
        print("Image processed and saved to BytesIO")

        return send_file(img_io, mimetype="image/png")

    except Exception as e:
        print(f"Error occurred: {e}")
        return {"error": str(e)}, 500


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
