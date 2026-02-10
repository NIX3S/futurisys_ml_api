import psycopg2

try:
    conn = psycopg2.connect(
        dbname="futurisys_ml",
        user="postgres",
        password="5345",
        host="127.0.0.1",
        port="5432"
    )
    print("Connexion réussie !")
    conn.close()
except Exception as e:
    print("Erreur :", e)
