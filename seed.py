from models import Robot, Base, engine
from sqlalchemy.orm import Session
from datetime import datetime

with Session(engine) as session:
    new_robot = Robot(name = "R1", x = 0.0, y = 0.0, battery_pct=100.0, status = "idle", updated_at=datetime.now())
    session.add(new_robot)
    session.commit()
    # it adds same one everytime i run the code

with Session(engine) as session:
    robots = session.query(Robot).all()
    for r in robots:
        print(r.name, r.x, r.y, r.battery_pct, r.status, r.updated_at)