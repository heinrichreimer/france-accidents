module Model exposing (Accident, AtmosphericConditions(..), Collision(..), Curvature(..), DedicatedLane(..), Engine(..), FixedObstacle(..), Intersection(..), Light(..), LocationRegime(..), Manoeuvre(..), MobileObstacle(..), PedestrianAction(..), PedestrianCompany(..), PedestrianLocation(..), Person, PersonCategory(..), Place(..), Profile(..), Resource(..), RoadCategory(..), SafetyEquipment(..), Severity(..), Sex(..), ShockPoint(..), TrafficDirection(..), TrafficRegime(..), TravelReason(..), Vehicle, VehicleCategory(..))

import Time exposing (Posix)


type Light
    = LightDaylight
    | LightDuskOrDawn
    | LightNightWithoutPublicLighting
    | LightNightWithPublicLightingOff
    | LightNightWithPublicLightingOn


type Intersection
    = IntersectionOutOfIntersection
    | IntersectionXIntersection
    | IntersectionTIntersection
    | IntersectionYIntersection
    | IntersectionIntersectionWithMoreThan4Branches
    | IntersectionRoundabout
    | IntersectionPlace
    | IntersectionLevelCrossing
    | IntersectionOtherIntersection


type AtmosphericConditions
    = AtmosphericConditionsNormal
    | AtmosphericConditionsLightRain
    | AtmosphericConditionsHeavyRain
    | AtmosphericConditionsSnowHail
    | AtmosphericConditionsFogSmoke
    | AtmosphericConditionsStrongWindStorm
    | AtmosphericConditionsDazzlingWeather
    | AtmosphericConditionsOvercastWeather
    | AtmosphericConditionsOther


type Collision
    = CollisionTwoVehiclesFront
    | CollisionTwoVehiclesFromTheRear
    | CollisionTwoVehiclesFromTheSide
    | CollisionThreeOrMoreVehiclesInAChain
    | CollisionThreeOrMoreVehiclesMultipleCollisions
    | CollisionOtherCollision
    | CollisionWithoutCollision


type LocationRegime
    = LocationRegimeOutOfTown
    | LocationRegimeInBuiltUpAreas


type RoadCategory
    = RoadCategoryHighway
    | RoadCategoryNationalRoad
    | RoadCategoryDepartmentalRoad
    | RoadCategoryMunicipalRoads
    | RoadCategoryOffThePublicNetwork
    | RoadCategoryParkingLotOpenToPublicTraffic
    | RoadCategoryUrbanMetropolitanRoads
    | RoadCategoryOther


type TrafficRegime
    = TrafficRegimeOneWay
    | TrafficRegimeBidirectional
    | TrafficRegimeWithSeparateLanes
    | TrafficRegimeWithVariableAssignmentLanes


type DedicatedLane
    = DedicatedLaneNone
    | DedicatedLaneBicyclePath
    | DedicatedLaneCycleLane
    | DedicatedLaneReservedLane


type Profile
    = ProfileFlat
    | ProfileSlope
    | ProfileTopOfHill
    | ProfileBottomOfHill


type Curvature
    = CurvatureStraight
    | CurvatureLeftHandCurve
    | CurvatureRightHandCurve
    | CurvatureSCurve


type Place
    = PlaceFrontLeftMotorcycleFront
    | PlaceFrontRightMotorcycleRear
    | PlaceRearRightMotorcycleSidecar
    | PlaceRearLeft
    | PlaceRearCenter
    | PlaceFrontCenter
    | PlaceCenterLeft
    | PlaceCenterMiddle
    | PlaceCenterRight
    | PlacePedestrian


type PersonCategory
    = PersonCategoryDriver
    | PersonCategoryPassenger
    | PersonCategoryPedestrian


type Severity
    = SeverityUnharmed
    | SeverityKilled
    | SeverityInjuredHospitalized
    | SeveritySlightlyInjured


type Sex
    = SexFemale
    | SexMale


type TravelReason
    = TravelReasonHomeToWork
    | TravelReasonHomeToSchool
    | TravelReasonShopping
    | TravelReasonProfessional
    | TravelReasonWalkingLeisure
    | TravelReasonOther


type SafetyEquipment
    = SafetyEquipmentBelt
    | SafetyEquipmentHeadset
    | SafetyEquipmentChildrenDevice
    | SafetyEquipmentReflectiveVest
    | SafetyEquipmentAirbag
    | SafetyEquipmentGloves
    | SafetyEquipmentOther


type PedestrianLocation
    = PedestrianLocationOnPavementAtLeast50MFromPedestrianCrossing
    | PedestrianLocationOnPavementAtMost50MFromPedestrianCrossing
    | PedestrianLocationOnPedestrianCrossingWithoutLightSignal
    | PedestrianLocationOnPedestrianCrossingWithLightSignal
    | PedestrianLocationOnSidewalk
    | PedestrianLocationOnRoadShoulder
    | PedestrianLocationOnEmergencyBayOrShoulder
    | PedestrianLocationOnCounterAisle


type PedestrianAction
    = PedestrianActionDirectionOfImpactingVehicle
    | PedestrianActionOppositeDirectionOfImpactingVehicle
    | PedestrianActionCrossing
    | PedestrianActionMasked
    | PedestrianActionPlayingRunning
    | PedestrianActionWithAnimal
    | PedestrianActionOther
    | PedestrianActionGettingOnOffVehicle


type PedestrianCompany
    = PedestrianCompanyAlone
    | PedestrianCompanyAccompanied
    | PedestrianCompanyGroup


type alias Person =
    { place : Maybe Place
    , category : Maybe PersonCategory
    , severity : Severity
    , sex : Sex
    , birthYear : Maybe Int
    , travelReason : Maybe TravelReason
    , safetyEquipment : List SafetyEquipment
    , pedestrianLocation : Maybe PedestrianLocation
    , pedestrianAction : Maybe PedestrianAction
    , pedestrianCompany : Maybe PedestrianCompany
    }


type TrafficDirection
    = TrafficDirectionIncreasingReferenceNumber
    | TrafficDirectionDecreasingReferenceNumber
    | TrafficDirectionNoReference


type VehicleCategory
    = VehicleCategoryBicycle
    | VehicleCategoryMopedLessThan50Cm3
    | VehicleCategoryQuadWithBody
    | VehicleCategoryRegisteredScooter
    | VehicleCategoryMotorcycle
    | VehicleCategorySidecar
    | VehicleCategoryLightVehicleOnly
    | VehicleCategoryLightVehicleWithCaravan
    | VehicleCategoryLightVehicleWithTrailer
    | VehicleCategoryCommercialVehicleOnlyWeightRatingAtLeast1Point5TAtMost3Point5T
    | VehicleCategoryCommercialVehicleWithCaravanWeightRatingAtLeast1Point5TAtMost3Point5T
    | VehicleCategoryCommercialVehicleWithTrailerWeightRatingAtLeast1Point5TAtMost3Point5T
    | VehicleCategoryTruckOnlyWeightRatingMoreThan3Point5TAtMost7Point5T
    | VehicleCategoryTruckOnlyWeightRatingMoreThan7Point5T
    | VehicleCategoryTruckMoreThan3Point5TWithTrailer
    | VehicleCategoryRoadTractorOnly
    | VehicleCategoryRoadTractorWithSemiTrailer
    | VehicleCategoryPublicTransport
    | VehicleCategorySpecialMachine
    | VehicleCategoryAgriculturalTractor
    | VehicleCategoryScooterLessThan50Cm3
    | VehicleCategoryMotorcycleMoreThan50Cm3AtMost125Cm3
    | VehicleCategoryScooterMoreThan50Cm3AtMost125Cm3
    | VehicleCategoryMotorcycleMoreThan125Cm3
    | VehicleCategoryScooterMoreThan125Cm3
    | VehicleCategoryQuadWithoutBodyAtMost50Cm3
    | VehicleCategoryQuadWithoutBodyMoreThan50Cm3
    | VehicleCategoryBuses
    | VehicleCategoryBus
    | VehicleCategoryTrain
    | VehicleCategoryTramway
    | VehicleCategoryTricycleAtMost50Cm3
    | VehicleCategoryTricycleMoreThan50Cm3AtMost125Cm3
    | VehicleCategoryTricycleMoreThan125Cm3
    | VehicleCategoryPersonalTransporterMotorized
    | VehicleCategoryPersonalTransporterUnmotorized
    | VehicleCategoryPedelec
    | VehicleCategoryOther


type FixedObstacle
    = FixedObstacleParkedVehicle
    | FixedObstacleTree
    | FixedObstacleMetalSlide
    | FixedObstacleConcreteChute
    | FixedObstacleOtherSlide
    | FixedObstacleBuildingWallBridgePier
    | FixedObstacleVerticalSignalSupportEmergencyCallStation
    | FixedObstaclePost
    | FixedObstacleStreetFurniture
    | FixedObstacleParapet
    | FixedObstacleIslandRefugeHighPost
    | FixedObstacleSidewalkCurb
    | FixedObstacleDitchEmbankmentRockFace
    | FixedObstacleOtherOnRoad
    | FixedObstacleOtherOnSidewalkOrShoulder
    | FixedObstacleObstacleFreeRoadwayExit
    | FixedObstacleNozzleAqueductHead


type MobileObstacle
    = MobileObstaclePedestrian
    | MobileObstacleVehicle
    | MobileObstacleRailVehicle
    | MobileObstacleDomesticAnimal
    | MobileObstacleWildAnimal
    | MobileObstacleOther


type ShockPoint
    = ShockPointFront
    | ShockPointFrontRight
    | ShockPointFrontLeft
    | ShockPointRear
    | ShockPointRearRight
    | ShockPointRearLeft
    | ShockPointSideRight
    | ShockPointSideLeft
    | ShockPointMultipleImpactsRollovers


type Manoeuvre
    = ManoeuvreNoChangeOfDirection
    | ManoeuvreSameDirectionSameLine
    | ManoeuvreBetweenTwoLines
    | ManoeuvreReversing
    | ManoeuvreOppositeDirection
    | ManoeuvreCrossingCentralReservation
    | ManoeuvreOnBusLaneSameDirection
    | ManoeuvreOnBusLaneOppositeDirection
    | ManoeuvreMerging
    | ManoeuvreTurningAroundOnRoad
    | ManoeuvreChangingLanesLeft
    | ManoeuvreChangingLanesRight
    | ManoeuvreDeportedLeft
    | ManoeuvreDeportedRight
    | ManoeuvreTurningLeft
    | ManoeuvreTurningRight
    | ManoeuvreExceedingLeft
    | ManoeuvreExceedingRight
    | ManoeuvreCrossingRoadway
    | ManoeuvreParkingManoeuvre
    | ManoeuvreAvoidanceManoeuvre
    | ManoeuvreDoorOpening
    | ManoeuvreStoppedExcludingParking
    | ManoeuvreParkedWithOccupants
    | ManoeuvreDrivingOnSidewalk
    | ManoeuvreOther


type Engine
    = EngineHydrocarbon
    | EngineElectricHybrid
    | EngineElectric
    | EngineHydrogen
    | EngineHuman
    | EngineOther


type alias Vehicle =
    { name : String
    , id : Maybe Int
    , trafficDirection : Maybe TrafficDirection
    , vehicleCategory : Maybe VehicleCategory
    , fixedObstacle : Maybe FixedObstacle
    , mobileObstacle : Maybe MobileObstacle
    , shockPoint : Maybe ShockPoint
    , primaryManoeuvre : Maybe Manoeuvre
    , engine : Maybe Engine
    , occupancy : Maybe Int
    , persons : List Person
    }


type alias Accident =
    { id : Int
    , timestamp : Posix
    , latitude : Maybe Float
    , longitude : Maybe Float
    , address : String
    , light : Maybe Light
    , intersection : Maybe Intersection
    , atmosphericConditions : Maybe AtmosphericConditions
    , collision : Maybe Collision
    , location : Maybe LocationRegime
    , department : String
    , commune : String
    , roadCategory : RoadCategory
    , road : String
    , roadIndexNumber : Maybe Int
    , roadIndexAlpha : Maybe String
    , trafficRegime : Maybe TrafficRegime
    , lanesCount : Maybe Int
    , dedicatedLane : Maybe DedicatedLane
    , profile : Maybe Profile
    , upstreamTerminal : Maybe Int
    , upstreamTerminalDistanceMeters : Maybe Float
    , curvature : Maybe Curvature
    , centralReservationWidthMeters : Float
    , roadTrafficWidthMeters : Float
    , vehicles : List Vehicle
    }


type Resource t
    = Failure String
    | Loading
    | Success t
