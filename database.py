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

    def get_giveaway(self, name):
        found = self.giveaways.search(where('name') == name)
        if len(found): return found[0]
        else: raise GiveawayNotFound()

    def create_giveaway(self, name):
        try:
            self.get_giveaway(name)
            raise GiveawayExists()
        except GiveawayNotFound:
            self.giveaways.insert({
                'name': name,
                'created': time.time(),
                'active': True,
                'invites': []
            })
    
    def active_giveaways(self):
        return filter(lambda x: x['active'], self.all_giveaways())
    
    def all_giveaways(self):
        return self.giveaways.all()

    def end_giveaway(self, name):
        ga = self.get_giveaway(name)
        ga['active'] = False
        self.giveaways.update(ga, where('name') == name)

    def create_invite(self, name, code, user):
        ga = self.get_giveaway(name)
        for inv in ga['invites']:
            if inv['user'] == user: raise AlreadyJoined()

        ga['invites'].append({
            'user': user,
            'code': code
        })

        self.giveaways.update(ga, where('name') == name)