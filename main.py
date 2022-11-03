from parser import Parser
from models import Deputat, db


def check_conection(func):
    def wrapper(*args, **kwargs):
        try:
            db.connect()
            func(*args, **kwargs)
        finally:
            db.close()
    return wrapper

@check_conection
def insert_data():
    db.create_tables([Deputat])   
    obj = Parser().data  
    with db.atomic():
        Deputat.insert_many(obj).execute()
    # for deputat in objs:   
    #     Deputat.create(**deputat)       

if __name__ == '__main__':
    insert_data()