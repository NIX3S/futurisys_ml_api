import gradio as gr
from app.services.prediction import predict
from app.api.endpoints import InputData

# Fonction d'adaptation pour Gradio
def gradio_predict(*args):
    columns = [
        "NumberofFloors", "NumberofBuildings", "GFAPerFloor", "PropertyGFATotal",
        "GFA_Prison_Incarceration", "GFA_College_University", "GFA_Office",
        "GFA_Parking", "GFA_Medical_Office", "GFA_Indoor_Arena",
        "GFA_Hospital_General_Medical_Surgical", "GFA_Data_Center",
        "GFA_Laboratory", "GFA_Supermarket_Grocery_Store",
        "GFA_Urgent_Care_Clinic_Other_Outpatient",
        "BuildingType_Nonresidential_WA", "ZipCode_infrequent_sklearn",
        "EPAPropertyType_infrequent_sklearn"
    ]
    # Convertir le tuple en dict
    data_dict = dict(zip(columns, args))
    
    # Créer l'objet Pydantic
    data = InputData(**data_dict)
    
    # Prédiction
    prediction = predict(data)
    return prediction

# Créer les inputs Gradio selon ton modèle
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
