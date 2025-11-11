class Zone:
    def __init__(self, name, x, y, z, speed):
        self.name = name
        self.x, self.y, self.z = x, y, z
        self.speed = speed

    def contains(self, x, y, z):
        return (self.x[0] <= x <= self.x[1] and
                self.y[0] <= y <= self.y[1] and
                self.z[0] <= z <= self.z[1])

class ZoneManager:
    def __init__(self, zones):
        self.zones = zones

    def get_zone(self, x, y, z):
        for zone in self.zones:
            if zone.contains(x, y, z):
                return zone
        return None