module Visualization2 exposing (..)

import Html.Styled exposing (Html, br, div, text)
import Model exposing (Accident)


type alias Model =
    {}


type Msg
    = NoOp


label : String
label =
    "Person Characteristics Stick Figures"


init : ( Model, Cmd Msg )
init =
    ( {}, Cmd.none )


update : Msg -> Model -> ( Model, Cmd Msg )
update msg model =
    case msg of
        NoOp ->
            ( model, Cmd.none )


view : Model -> List Accident -> Html msg
view model accidents =
    div
        []
        [ text label
        , br [] []
        , text (String.fromInt (List.length accidents))
        ]
