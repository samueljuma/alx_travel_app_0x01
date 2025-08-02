# Notes  

## Seed Script

This `seed.py` management command is used to populate the database with dummy data for testing and development 


### 📦 What It Does

The script uses the [Faker](https://faker.readthedocs.io/) library to generate realistic sample data and seeds the Listing model.

- `Listing`: Populates sample travel listings with fields such as title, description, location, and price.

### ▶️ How to Run
Make sure your virtual environment is activated and dependencies are installed, then run:

```bash
python manage.py seed

