import gradio as gr
from app.services.predictions import predict
from app.api.endpoints import InputData

# Fonction d'adaptation pour Gradio
def gradio_predict(**kwargs):
    """
    Gradio envoie un dict kwargs → on le convertit en InputData pour predict()
    """
    input_data = InputData(**kwargs)
    return predict(input_data)

# Créer les inputs Gradio selon modèle
inputs = [
    gr.Number(label="NumberofFloors"),
    gr.Number(label="NumberofBuildings"),
    gr.Number(label="GFAPerFloor"),
    gr.Number(label="PropertyGFATotal"),
    gr.Number(label="GFA_Prison_Incarceration"),
    gr.Number(label="GFA_College_University"),
    gr.Number(label="GFA_Office"),
    gr.Number(label="GFA_Parking"),
    gr.Number(label="GFA_Medical_Office"),
    gr.Number(label="GFA_Indoor_Arena"),
    gr.Number(label="GFA_Hospital_General_Medical_Surgical"),
    gr.Number(label="GFA_Data_Center"),
    gr.Number(label="GFA_Laboratory"),
    gr.Number(label="GFA_Supermarket_Grocery_Store"),
    gr.Number(label="GFA_Urgent_Care_Clinic_Other_Outpatient"),
    gr.Number(label="BuildingType_Nonresidential_WA"),
    gr.Number(label="ZipCode_infrequent_sklearn"),
    gr.Number(label="EPAPropertyType_infrequent_sklearn")
]

outputs = gr.Number(label="Prediction")

iface = gr.Interface(
    fn=gradio_predict,
    inputs=inputs,
    outputs=outputs,
    title="Futurisys ML API",
    description="Entrez les données pour obtenir la prédiction du modèle."
)

if __name__ == "__main__":
    iface.launch(server_name="0.0.0.0", server_port=7860)
