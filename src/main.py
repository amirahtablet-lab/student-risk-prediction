from src.models.model_factory import ModelFactory

def main():
    print("=== Student Risk Prediction ===")
    
    # Memanggil model lewat Factory, bukan mengimpor class model secara langsung
    model_name = "random_forest"
    print(f"Membuat model via Factory: {model_name}")
    model = ModelFactory.create(model_name)
    
    print("Berhasil membuat object model tanpa ketergantungan langsung!")

if __name__ == "__main__":
    main()
