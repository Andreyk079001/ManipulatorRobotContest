class VerticalZone:
    def __init__(self, name, z_range, speed):
        self.name = name
        self.z_range = z_range  # (min_z, max_z)
        self.speed = speed

    def contains(self, z):
        return self.z_range[0] <= z <= self.z_range[1]


class VerticalZoneManager:
    def __init__(self, zones):
        self.zones = zones

    def get_zone(self, z):
        for zone in self.zones:
            if zone.contains(z):
                return zone
        return None