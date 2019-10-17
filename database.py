from tinydb import TinyDB, where
import time

class AlreadyJoined(Exception): pass
class GiveawayNotFound(Exception): pass
class GiveawayNotActive(Exception): pass
class GiveawayExists(Exception): pass

class Database:
    def __init__(self, path):
        self.path = path
        self.db = TinyDB(self.path)
        self.giveaways = self.db.table('giveaways')
        self.messages = self.db.table('messages')

    def get_giveaway(self, name):
        found = self.giveaways.search(where('name') == name)
        if len(found): return found[0]
        else: raise GiveawayNotFound()

    def create_giveaway(self, name):
        try:
            self.get_giveaway(name)
            raise GiveawayExists()
        except GiveawayNotFound:
            ga = { 'name': name,
                'created': time.time(),
                'active': True,
                'invites': [] }
            self.giveaways.insert(ga)
            return ga
    
    def delete_giveaway(self, name):
        ga = self.get_giveaway(name)
        self.giveaways.remove(where('name') == name)

    def add_message(self, id, name):
        self.messages.insert({
            'id': id, 'name': name
        })
    
    def get_message(self, id):
        found = self.messages.search(where('id') == id)
        if len(found): return found[0]
        else: return False

    def active_giveaways(self):
        return list(filter(lambda x: x['active'], self.all_giveaways()))

    def all_giveaways(self):
        return self.giveaways.all()

    def close_giveaway(self, name):
        ga = self.get_giveaway(name)
        ga['active'] = False
        self.giveaways.update(ga, where('name') == name)

    def record_invite(self, name, code, user):
        ga = self.get_giveaway(name)
        for inv in ga['invites']:
            if inv['user'] == user: raise AlreadyJoined()

        ga['invites'].append({
            'user': user,
            'code': code
        })

        self.giveaways.update(ga, where('name') == name)
