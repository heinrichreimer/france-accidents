from collections.abc import Set, Collection
from datetime import datetime
from enum import IntEnum
from typing import Optional, NamedTuple


class Light(IntEnum):
    DAYLIGHT = 1
    DUSK_OR_DAWN = 2
    NIGHT_WITHOUT_PUBLIC_LIGHTING = 3
    NIGHT_WITH_PUBLIC_LIGHTING_OFF = 4
    NIGHT_WITH_PUBLIC_LIGHTING_ON = 5


class Intersection(IntEnum):
    OUT_OF_INTERSECTION = 1
    X_INTERSECTION = 2
    T_INTERSECTION = 3
    Y_INTERSECTION = 4
    INTERSECTION_WITH_MORE_THAN_4_BRANCHES = 5
    ROUNDABOUT = 6
    PLACE = 7
    LEVEL_CROSSING = 8
    OTHER_INTERSECTION = 9


class AtmosphericConditions(IntEnum):
    NORMAL = 1
    LIGHT_RAIN = 2
    HEAVY_RAIN = 3
    SNOW_HAIL = 4
    FOG_SMOKE = 5
    STRONG_WIND_STORM = 6
    DAZZLING_WEATHER = 7
    OVERCAST_WEATHER = 8
    OTHER = 9


class Collision(IntEnum):
    TWO_VEHICLES_FRONT = 1
    TWO_VEHICLES_FROM_THE_REAR = 2
    TWO_VEHICLES_FROM_THE_SIDE = 3
    THREE_OR_MORE_VEHICLES_IN_A_CHAIN = 4
    THREE_OR_MORE_VEHICLES_MULTIPLE_COLLISIONS = 5
    OTHER_COLLISION = 6
    WITHOUT_COLLISION = 7


class LocationRegime(IntEnum):
    OUT_OF_TOWN = 1
    IN_BUILT_UP_AREAS = 2


class AccidentId(NamedTuple):
    accident_id: int


class Characteristic(NamedTuple):
    timestamp: datetime
    latitude: Optional[float]
    longitude: Optional[float]
    address: str
    light: Optional[Light]
    intersection: Optional[Intersection]
    atmospheric_conditions: Optional[AtmosphericConditions]
    collision: Optional[Collision]
    location: Optional[LocationRegime]
    department: str
    commune: str


class RoadCategory(IntEnum):
    HIGHWAY = 1
    NATIONAL_ROAD = 2
    DEPARTMENTAL_ROAD = 3
    MUNICIPAL_ROADS = 4
    OFF_THE_PUBLIC_NETWORK = 5
    PARKING_LOT_OPEN_TO_PUBLIC_TRAFFIC = 6
    URBAN_METROPOLITAN_ROADS = 7
    OTHER = 9


class TrafficRegime(IntEnum):
    ONE_WAY = 1
    BIDIRECTIONAL = 2
    WITH_SEPARATE_LANES = 3
    WITH_VARIABLE_ASSIGNMENT_LANES = 4


class DedicatedLane(IntEnum):
    NONE = 0
    BICYCLE_PATH = 1
    CYCLE_LANE = 2
    RESERVED_LANE = 3


class Profile(IntEnum):
    FLAT = 1
    SLOPE = 2
    TOP_OF_HILL = 3
    BOTTOM_OF_HILL = 4


class Curvature(IntEnum):
    STRAIGHT = 1
    LEFT_HAND_CURVE = 2
    RIGHT_HAND_CURVE = 3
    S_CURVE = 4


class Location(NamedTuple):
    road_category: RoadCategory
    road: str
    road_index_number: Optional[int]
    road_index_alpha: Optional[str]
    traffic_regime: Optional[TrafficRegime]
    lanes_count: Optional[int]
    dedicated_lane: Optional[DedicatedLane]
    profile: Optional[Profile]
    upstream_terminal: Optional[int]
    upstream_terminal_distance_meters: Optional[float]
    curvature: Optional[Curvature]
    central_reservation_width_meters: int
    road_traffic_width_meters: float


class Place(IntEnum):
    FRONT_LEFT_MOTORCYCLE_FRONT = 1
    FRONT_RIGHT_MOTORCYCLE_REAR = 2
    REAR_RIGHT_MOTORCYCLE_SIDECAR = 3
    REAR_LEFT = 4
    REAR_CENTER = 5
    FRONT_CENTER = 6
    CENTER_LEFT = 7
    CENTER_MIDDLE = 8
    CENTER_RIGHT = 9
    PEDESTRIAN = 10


class PersonCategory(IntEnum):
    DRIVER = 1
    PASSENGER = 2
    PEDESTRIAN = 3


class Severity(IntEnum):
    UNHARMED = 1
    KILLED = 2
    INJURED_HOSPITALIZED = 3
    SLIGHTLY_INJURED = 4


class Sex(IntEnum):
    FEMALE = 2
    MALE = 1


class TravelReason(IntEnum):
    HOME_TO_WORK = 1
    HOME_TO_SCHOOL = 2
    SHOPPING = 3
    PROFESSIONAL = 4
    WALKING_LEISURE = 5
    OTHER = 9


class SafetyEquipment(IntEnum):
    BELT = 1
    HEADSET = 2
    CHILDREN_DEVICE = 3
    REFLECTIVE_VEST = 4
    AIRBAG = 5  # todo or 7
    GLOVES = 6  # todo or 7
    OTHER = 9


class PedestrianLocation(IntEnum):
    ON_PAVEMENT_AT_LEAST_50_M_FROM_PEDESTRIAN_CROSSING = 1
    ON_PAVEMENT_AT_MOST_50_M_FROM_PEDESTRIAN_CROSSING = 2
    ON_PEDESTRIAN_CROSSING_WITHOUT_LIGHT_SIGNAL = 3
    ON_PEDESTRIAN_CROSSING_WITH_LIGHT_SIGNAL = 4
    ON_SIDEWALK = 5
    ON_ROAD_SHOULDER = 6
    ON_EMERGENCY_BAY_OR_SHOULDER = 7
    ON_COUNTER_AISLE = 8


class PedestrianAction(IntEnum):
    DIRECTION_OF_IMPACTING_VEHICLE = 1
    OPPOSITE_DIRECTION_OF_IMPACTING_VEHICLE = 2
    CROSSING = 3
    MASKED = 4
    PLAYING_RUNNING = 5
    WITH_ANIMAL = 6
    OTHER = 9
    GETTING_ON_OFF_VEHICLE = 99  # todo A


class PedestrianCompany(IntEnum):
    ALONE = 1
    ACCOMPANIED = 2
    GROUP = 3


class Person(NamedTuple):
    place: Optional[Place]
    category: Optional[PersonCategory]
    severity: Severity
    sex: Sex
    birth_year: Optional[int]
    travel_reason: Optional[TravelReason]
    safety_equipment: Set[SafetyEquipment]
    pedestrian_location: Optional[PedestrianLocation]
    pedestrian_action: Optional[PedestrianAction]
    pedestrian_company: Optional[PedestrianCompany]

    def to_json(self) -> dict:
        return {

        }


class TrafficDirection(IntEnum):
    INCREASING_REFERENCE_NUMBER = 1
    DECREASING_REFERENCE_NUMBER = 2
    NO_REFERENCE = 3


class VehicleCategory(IntEnum):
    BICYCLE = 1
    MOPED_LESS_THAN_50_CM_3 = 2
    QUAD_WITH_BODY = 3
    REGISTERED_SCOOTER = 4
    MOTORCYCLE = 5
    SIDECAR = 6
    LIGHT_VEHICLE_ONLY = 7
    LIGHT_VEHICLE_WITH_CARAVAN = 8
    LIGHT_VEHICLE_WITH_TRAILER = 9
    COMMERCIAL_VEHICLE_ONLY_WEIGHT_RATING_AT_LEAST_1_5_T_AT_MOST_3_5_T = 10
    COMMERCIAL_VEHICLE_WITH_CARAVAN_WEIGHT_RATING_AT_LEAST_1_5_T_AT_MOST_3_5_T = 11
    COMMERCIAL_VEHICLE_WITH_TRAILER_WEIGHT_RATING_AT_LEAST_1_5_T_AT_MOST_3_5_T = 12
    TRUCK_ONLY_WEIGHT_RATING_MORE_THAN_3_5_T_AT_MOST_7_5_T = 13
    TRUCK_ONLY_WEIGHT_RATING_MORE_THAN_7_5_T = 14
    TRUCK_MORE_THAN_3_5_T_WITH_TRAILER = 15
    ROAD_TRACTOR_ONLY = 16
    ROAD_TRACTOR_WITH_SEMI_TRAILER = 17
    PUBLIC_TRANSPORT = 18
    # TRAMWAY = 19
    SPECIAL_MACHINE = 20
    AGRICULTURAL_TRACTOR = 21
    SCOOTER_LESS_THAN_50_CM_3 = 30
    MOTORCYCLE_MORE_THAN_50_CM_3_AT_MOST_125_CM_3 = 31
    SCOOTER_MORE_THAN_50_CM_3_AT_MOST_125_CM_3 = 32
    MOTORCYCLE_MORE_THAN_125_CM_3 = 33
    SCOOTER_MORE_THAN_125_CM_3 = 34
    QUAD_WITHOUT_BODY_AT_MOST_50_CM_3 = 35
    QUAD_WITHOUT_BODY_MORE_THAN_50_CM_3 = 36
    BUSES = 37
    BUS = 38
    TRAIN = 39
    TRAMWAY = 40
    TRICYCLE_AT_MOST_50_CM_3 = 41
    TRICYCLE_MORE_THAN_50_CM_3_AT_MOST_125_CM_3 = 42
    TRICYCLE_MORE_THAN_125_CM_3 = 43
    PERSONAL_TRANSPORTER_MOTORIZED = 50
    PERSONAL_TRANSPORTER_UNMOTORIZED = 60
    PEDELEC = 80
    OTHER = 99


class FixedObstacle(IntEnum):
    PARKED_VEHICLE = 1
    TREE = 2
    METAL_SLIDE = 3
    CONCRETE_CHUTE = 4
    OTHER_SLIDE = 5
    BUILDING_WALL_BRIDGE_PIER = 6
    VERTICAL_SIGNAL_SUPPORT_EMERGENCY_CALL_STATION = 7
    POST = 8
    STREET_FURNITURE = 9
    PARAPET = 10
    ISLAND_REFUGE_HIGH_POST = 11
    SIDEWALK_CURB = 12
    DITCH_EMBANKMENT_ROCK_FACE = 13
    OTHER_ON_ROAD = 14
    OTHER_ON_SIDEWALK_OR_SHOULDER = 15
    OBSTACLE_FREE_ROADWAY_EXIT = 16
    NOZZLE_AQUEDUCT_HEAD = 17


class MobileObstacle(IntEnum):
    PEDESTRIAN = 1
    VEHICLE = 2
    RAIL_VEHICLE = 4
    DOMESTIC_ANIMAL = 5
    WILD_ANIMAL = 6
    OTHER = 9


class ShockPoint(IntEnum):
    FRONT = 1
    FRONT_RIGHT = 2
    FRONT_LEFT = 3
    REAR = 4
    REAR_RIGHT = 5
    REAR_LEFT = 6
    SIDE_RIGHT = 7
    SIDE_LEFT = 8
    MULTIPLE_IMPACTS_ROLLOVERS = 9


class Manoeuvre(IntEnum):
    NO_CHANGE_OF_DIRECTION = 1
    SAME_DIRECTION_SAME_LINE = 2
    BETWEEN_TWO_LINES = 3
    REVERSING = 4
    OPPOSITE_DIRECTION = 5
    CROSSING_CENTRAL_RESERVATION = 6
    ON_BUS_LANE_SAME_DIRECTION = 7
    ON_BUS_LANE_OPPOSITE_DIRECTION = 8
    MERGING = 9
    TURNING_AROUND_ON_ROAD = 10
    CHANGING_LANES_LEFT = 11
    CHANGING_LANES_RIGHT = 12
    DEPORTED_LEFT = 13
    DEPORTED_RIGHT = 14
    TURNING_LEFT = 15
    TURNING_RIGHT = 16
    EXCEEDING_LEFT = 17
    EXCEEDING_RIGHT = 18
    CROSSING_ROADWAY = 19
    PARKING_MANOEUVRE = 20
    AVOIDANCE_MANOEUVRE = 21
    DOOR_OPENING = 22
    STOPPED_EXCLUDING_PARKING = 23
    PARKED_WITH_OCCUPANTS = 24
    DRIVING_ON_SIDEWALK = 25
    OTHER = 26


class Engine(IntEnum):
    HYDROCARBON = 1
    ELECTRIC_HYBRID = 2
    ELECTRIC = 3
    HYDROGEN = 4
    HUMAN = 5
    OTHER = 6


class VehicleId(NamedTuple):
    vehicle_name: str
    vehicle_id: Optional[int]


class Vehicle(NamedTuple):
    vehicle_name: str
    vehicle_id: Optional[int]
    traffic_direction: Optional[TrafficDirection]
    vehicle_category: Optional[VehicleCategory]
    fixed_obstacle: Optional[FixedObstacle]
    mobile_obstacle: Optional[MobileObstacle]
    shock_point: Optional[ShockPoint]
    primary_manoeuvre: Optional[Manoeuvre]
    engine: Optional[Engine]
    occupancy: Optional[int]
    persons: Collection[Person]


class Accident(NamedTuple):
    accident_id: int
    timestamp: datetime
    latitude: Optional[float]
    longitude: Optional[float]
    address: str
    light: Optional[Light]
    intersection: Optional[Intersection]
    atmospheric_conditions: Optional[AtmosphericConditions]
    collision: Optional[Collision]
    location: Optional[LocationRegime]
    department: str
    commune: str
    road_category: RoadCategory
    road: str
    road_index_number: Optional[int]
    road_index_alpha: Optional[str]
    traffic_regime: Optional[TrafficRegime]
    lanes_count: Optional[int]
    dedicated_lane: Optional[DedicatedLane]
    profile: Optional[Profile]
    upstream_terminal: Optional[int]
    upstream_terminal_distance_meters: Optional[float]
    curvature: Optional[Curvature]
    central_reservation_width_meters: int
    road_traffic_width_meters: float
    vehicles: Collection[Vehicle]
