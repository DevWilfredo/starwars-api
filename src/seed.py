from app import app, db
from models import User, People, Planet, Vehicle, Favorite

def seed_data():
    with app.app_context():  # Necesario para poder usar db.session

        # Borrar datos existentes
        Favorite.query.delete()
        User.query.delete()
        People.query.delete()
        Planet.query.delete()
        Vehicle.query.delete()
        db.session.commit()

        # Crear usuarios
        user1 = User(
            firstname="Luke",
            lastname="Skywalker",
            email="luke@rebellion.com",
            password="force123",
            is_active=True
        )
        user2 = User(
            firstname="Leia",
            lastname="Organa",
            email="leia@rebellion.com",
            password="hope456",
            is_active=True
        )
        db.session.add_all([user1, user2])
        db.session.commit()

        # Crear personajes
        people1 = People(
            name="Luke Skywalker",
            height="172",
            mass="77",
            hair_color="Blond",
            skin_color="Fair",
            eye_color="Blue",
            birth_year="19BBY",
            gender="Male"
        )
        people2 = People(
            name="Darth Vader",
            height="202",
            mass="136",
            hair_color="None",
            skin_color="White",
            eye_color="Yellow",
            birth_year="41.9BBY",
            gender="Male"
        )
        db.session.add_all([people1, people2])
        db.session.commit()

        # Crear planetas
        planet1 = Planet(
            name="Tatooine",
            rotation_period="23",
            orbital_period="304",
            diameter="10465",
            climate="Arid",
            gravity="1 standard",
            terrain="Desert",
            surface_water="1",
            population="200000"
        )
        planet2 = Planet(
            name="Alderaan",
            rotation_period="24",
            orbital_period="364",
            diameter="12500",
            climate="Temperate",
            gravity="1 standard",
            terrain="Grasslands, mountains",
            surface_water="40",
            population="2000000000"
        )
        db.session.add_all([planet1, planet2])
        db.session.commit()

        # Crear vehículos
        vehicle1 = Vehicle(
            name="Snowspeeder",
            model="t-47 airspeeder",
            manufacturer="Incom corporation",
            cost_in_credits="unknown",
            length="4.5",
            max_atmosphering_speed="650",
            crew="2",
            passengers="0",
            cargo_capacity="10",
            consumables="none",
            vehicle_class="airspeeder"
        )
        vehicle2 = Vehicle(
            name="TIE Fighter",
            model="Twin Ion Engine Fighter",
            manufacturer="Sienar Fleet Systems",
            cost_in_credits="unknown",
            length="6.4",
            max_atmosphering_speed="1200",
            crew="1",
            passengers="0",
            cargo_capacity="65",
            consumables="2 days",
            vehicle_class="starfighter"
        )
        db.session.add_all([vehicle1, vehicle2])
        db.session.commit()

        # Crear favoritos
        fav1 = Favorite(user_id=user1.id, item_type="people", item_id=people2.id)
        fav2 = Favorite(user_id=user2.id, item_type="planet", item_id=planet1.id)
        fav3 = Favorite(user_id=user1.id, item_type="vehicle", item_id=vehicle1.id)
        db.session.add_all([fav1, fav2, fav3])
        db.session.commit()

        print("✔ Base de datos poblada con éxito.")

if __name__ == "__main__":
    seed_data()
