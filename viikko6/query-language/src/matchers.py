class And:
    def __init__(self, *matchers):
        self._matchers = matchers
    
    def matches(self, player):
        for matcher in self._matchers:
            if not matcher.matches(player):
                return False
        
        return True


class Or:
    def __init__(self, *matchers):
        self._matchers = matchers

    def matches(self, player):
        for matcher in self._matchers:
            if matcher.matches(player):
                return True

        return False

class PlaysIn:
    def __init__(self, team):
        self._team = team

    def matches(self, player):
        return player.team == self._team

class HasAtLeast:
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr

    def matches(self, player):
        player_value = getattr(player, self._attr)

        return player_value >= self._value

class HasFewerThan:
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr

    def matches(self, player):
        player_value = getattr(player, self._attr)

        return player_value < self._value

class Not:
    def __init__(self, olio):
        self.olio = olio

    def matches(self, player):
        return not (self.olio.matches(player))

class All:
    def matches(self, player):
        return True


class QueryBuilder:
    def __init__(self, matcher = All()):
        self._matcher_olio = matcher

    def build(self):
        return self._matcher_olio

    def playsIn(self, team):
        return QueryBuilder(And(PlaysIn(team), self._matcher_olio))

    def hasAtLeast(self, value, attr):
        return QueryBuilder(And(HasAtLeast(value, attr), self._matcher_olio))

    def hasFewerThan(self, value, attr):
        return QueryBuilder(And(HasFewerThan(value, attr), self._matcher_olio))

    def oneOf(self, m1, m2):
        return QueryBuilder(Or(m1, m2))