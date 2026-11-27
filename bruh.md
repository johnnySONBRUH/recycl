## Inspiration
Improper waste disposal is a major global issue that pollutes the environment and indirectly destroys ecosystems and wildlife. A significant part of the problem is that waste is often not disposed of according to its category—such as plastics, metals, or paper—which makes recycling and other waste-reduction efforts much more difficult. We noticed that many people want to recycle correctly but are unsure how to classify their waste quickly and confidently. That gap inspired us to build **Recyclify**: a tool that makes proper waste categorization simple, fast, and transparent for everyday users.

## What it does
Recyclify uses an image classification model to categorize waste correctly from a user-uploaded image. The app features a simple, easy-to-navigate UI built with Streamlit. Users upload an image of their waste, and the dashboard on the right displays the model’s predictions and confidence scores. Showing confidence scores helps foster trust in users and promotes transparency, so they can understand not just what the model predicts, but how confident it is.

The demo flow is straightforward:
1. The user uploads an image of a waste item.
2. Recyclify runs the image through its trained YOLOv8 classification model.
3. The dashboard displays the predicted waste category along with confidence scores.
4. The user can use this information to dispose of or recycle the item more responsibly.

By making waste classification more accessible, Recyclify aims to reduce confusion around recycling and encourage better waste-disposal habits.

## How we built it
Recyclify is built as an end-to-end image classification application.

- **Model:** We use an Ultralytics YOLOv8 image classification model.
- **Training:** The model was trained for 35 epochs on an extensive dataset of 15,000 images.
- **Performance:** It achieved a Top-1 Accuracy of 0.96, a Top-5 Accuracy of 1.00, and an inference speed of 2.02 milliseconds per image.
- **Frontend and hosting:** The UI is built and hosted with Streamlit.
- **User experience:** The interface is intentionally simple: users upload an image, and the dashboard shows predictions and confidence scores to build trust and promote transparency.

The project combines machine learning, model evaluation, and a user-friendly web interface into a single working prototype that can be demonstrated live.

## Challenges we ran into
One challenge was ensuring the model could generalize well across different waste categories and real-world image conditions. Waste items can vary significantly in shape, lighting, background, and angle, so building a robust classifier required careful dataset preparation and training.

We also had to balance model performance with speed. Since Recyclify is designed for quick, everyday use, predictions need to appear fast. Achieving strong accuracy while maintaining an inference speed of 2.02 milliseconds per image was an important technical goal.

Another challenge was designing the UI to clearly present predictions and confidence scores in a way that users can easily understand. We wanted the app to be simple, but also transparent enough that users feel informed rather than confused by the model’s output.

## Accomplishments that we're proud of
We’re proud of building a complete, working prototype that connects a trained image classification model to a clean and usable web interface. Specifically, we achieved:

- A **Top-1 Accuracy of 0.96**
- A **Top-5 Accuracy of 1.00**
- An inference speed of **2.02 milliseconds per image**
- A simple Streamlit UI that makes the model’s predictions and confidence scores easy to understand
- An end-to-end workflow that demonstrates how AI can support better waste disposal and recycling decisions

We’re especially proud that Recyclify is not just a model, but a usable application that addresses a real-world sustainability problem.

## What we learned
Through this project, we learned how to train and evaluate an image classification model on a large dataset, how to interpret metrics such as Top-1 and Top-5 accuracy, and how to integrate a trained model into a user-facing web application.

We also learned the importance of transparency in AI applications. Showing confidence scores helps users understand the model’s certainty and builds trust. Finally, we gained hands-on experience in balancing model accuracy, inference speed, and UI simplicity—three factors that are critical for real-world AI tools.

## What's next for Recyclify
Next, we hope to expand Recyclify’s waste categories and improve its robustness on real-world images. We’d also like to:

- Add more detailed recycling guidance based on the predicted category
- Explore mobile-friendly deployment so users can classify waste on the go
- Collect user feedback to improve the model over time
- Continue improving accuracy and generalization across different environments and waste types
- Integrate Recyclify into community recycling or sustainability initiatives

Ultimately, we hope Recyclify can make a meaningful impact in helping reduce global waste and promote recycling.