import pymongo
import calendar


class Monggg:
    def __init__(self):
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        cli = "To-do_list"
        db = client[cli]
        database = "My_list"
        self.collection = db[database]

    def first_update(self, day_name):
        qu = {day_name: {"$exists": True}}
        projection = {day_name: 1, "_id": 0}

        rez = self.collection.find_one(qu, projection)
        # if rez is not None:
        #     day_list_dict[day] = rez.get(day)
        return rez.get(day_name)

    def sunday_update(self, txt):
        qu = {"Sunday": {"$exists": True}}
        projection = {"Sunday": 1, "_id": 0}

        rez = self.collection.find_one(qu, projection)
        if rez is None:
            self.collection.insert_one({"Sunday": "huh"})
            self.collection.update_one(qu, {"$set": {"Sunday": txt}})
        elif rez is not None:
            self.collection.update_one(qu, {"$set": {"Sunday": txt}})

    def monday_update(self, txt):
        qu = {"Monday": {"$exists": True}}
        projection = {"Monday": 1, "_id": 0}

        rez = self.collection.find_one(qu, projection)
        if rez is None:
            self.collection.insert_one({"Monday": "huh"})
            self.collection.update_one(qu, {"$set": {"Monday": txt}})
        elif rez is not None:
            self.collection.update_one(qu, {"$set": {"Monday": txt}})

    def tuesday_update(self, txt):
        qu = {"Tuesday": {"$exists": True}}
        projection = {"Tuesday": 1, "_id": 0}

        rez = self.collection.find_one(qu, projection)
        if rez is None:
            self.collection.insert_one({"Tuesday": "huh"})
            self.collection.update_one(qu, {"$set": {"Tuesday": txt}})
        elif rez is not None:
            self.collection.update_one(qu, {"$set": {"Tuesday": txt}})

    def wednesday_update(self, txt):
        qu = {"Wednesday": {"$exists": True}}
        projection = {"Wednesday": 1, "_id": 0}

        rez = self.collection.find_one(qu, projection)
        if rez is None:
            self.collection.insert_one({"Wednesday": "huh"})
            self.collection.update_one(qu, {"$set": {"Wednesday": txt}})
        elif rez is not None:
            self.collection.update_one(qu, {"$set": {"Wednesday": txt}})

    def thursday_update(self, txt):
        qu = {"Thursday": {"$exists": True}}
        projection = {"Thursday": 1, "_id": 0}

        rez = self.collection.find_one(qu, projection)
        if rez is None:
            self.collection.insert_one({"Thursday": "huh"})
            self.collection.update_one(qu, {"$set": {"Thursday": txt}})
        elif rez is not None:
            self.collection.update_one(qu, {"$set": {"Thursday": txt}})

    def friday_update(self, txt):
        qu = {"Friday": {"$exists": True}}
        projection = {"Friday": 1, "_id": 0}

        rez = self.collection.find_one(qu, projection)
        if rez is None:
            self.collection.insert_one({"Friday": "huh"})
            self.collection.update_one(qu, {"$set": {"Friday": txt}})
        elif rez is not None:
            self.collection.update_one(qu, {"$set": {"Friday": txt}})

    def saturday_update(self, txt):
        qu = {"Saturday": {"$exists": True}}
        projection = {"Saturday": 1, "_id": 0}

        rez = self.collection.find_one(qu, projection)
        if rez is None:
            self.collection.insert_one({"Saturday": "huh"})
            self.collection.update_one(qu, {"$set": {"Saturday": txt}})
        elif rez is not None:
            self.collection.update_one(qu, {"$set": {"Saturday": txt}})


if __name__ == '__main__':
    obj1 = Monggg()
    # returend = obj1.first_update()
    # for ke, val in returend:
    #     print(f"{ke}: {val}")
    # obj1.first_update("Wednesday")
    # obj1.sunday_update("I love you")
