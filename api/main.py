
import yolov5, torch
from yolov5.utils.general import (xyxy2xywh)
from yolov5.utils.plots import Annotator, colors
import cv2





#app = FastAPI()

# Define a route for your prediction endpoint
#@app.post("/predict/")
#async def predict(file: UploadFile = File(...)):
def predict(file1):
    """contents = await file.read()
    img = Image.open(io.BytesIO(contents))
    """
    img = cv2.imread(file1)
    predict1=pr()
    processed_img=predict1.preprocess_image(img)
    # Make predictions using the model
    predictions = predict1.predict_model(processed_img)

    # Get the predicted label
    label = predict1.get_label(predictions)

    return {"label": label}
print(predict("api/img_109.jpg"))
#new branch content