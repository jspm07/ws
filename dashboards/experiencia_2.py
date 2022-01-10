import dash
import dash_bootstrap_components as dbc
from dash import html
from dash import dcc
from dash.dependencies import Input, Output, State
from flask import request, session
import pandas as pd
from utils import utils_google

def serve_layout():
    index = html.Div(
                        [
                            dbc.Row(
                                    [
                                    html.H1(
                                            "Experiencia Digitalia 2.0"
                                            , id="title"
                                            , style={"color":"#1b2b58", "font-size":"28px"}
                                            )
                                    ]
                                    , justify = 'center'
                                    )
                            , dbc.Row(
                                    [
                                    html.Div(
                                            html.H1(
                                                    "¡Hola! En Digitalia estamos reorganizando la empresa así como la experiencia y es vital tener la información de todos nuestros clientes. Por favor te pedimos que llenes este formulario con tu información para que empieces a vivir la nueva experiencia Digitalia :D"
                                                    , id="title-description-experiencia_2"
                                                    , className="title-description"
                                                    )
                                            , id=""
                                            , className="title-description-div"
                                            )
                                    ],
                                    justify = 'center')

                            , dbc.Row(
                                        [
                                        dbc.Col(
                                                    [
                                                    dbc.Form(
                                                                [
                                                                html.Div(
                                                                            [
                                                                                html.Div(
                                                                                            [
                                                                                                dbc.Label(
                                                                                                            "Ingresa tu correo electrónico (de preferencia el empresarial)"
                                                                                                            , html_for="form-email-experiencia_2"
                                                                                                            , className="form-label"
                                                                                                            , id="form-email-label-experiencia_2"
                                                                                                        )
                                                                                                , dbc.Input(
                                                                                                            type="email"
                                                                                                            , id="form-email-experiencia_2"
                                                                                                            , placeholder="email"
                                                                                                            , className="form-input"
                                                                                                        )
                                                                                            ]
                                                                                            , className = "form-input-div"
                                                                                        )
                                                                                , html.Div(
                                                                                            [
                                                                                                dbc.Label(
                                                                                                            "Ingresa tus nombres completos"
                                                                                                            , html_for="form-names-experiencia_2"
                                                                                                            , className="form-label"
                                                                                                            , id="form-names-label-experiencia_2"
                                                                                                        )
                                                                                                , dbc.Input(
                                                                                                            type="text"
                                                                                                            , id="form-names-experiencia_2"
                                                                                                            , placeholder="nombres completos"
                                                                                                            , className="form-input"
                                                                                                        )
                                                                                            ]
                                                                                            , className = "form-input-div"
                                                                                        )

                                                                                , html.Div(
                                                                                            [
                                                                                                dbc.Label(
                                                                                                            "Ingresa tus apellidos completos"
                                                                                                            , html_for="form-lastnames-experiencia_2"
                                                                                                            , className="form-label"
                                                                                                            , id="form-lastnames-label-experiencia_2"
                                                                                                        )
                                                                                                , dbc.Input(
                                                                                                            type="text"
                                                                                                            , id="form-lastnames-experiencia_2"
                                                                                                            , placeholder="apellidos completos"
                                                                                                            , className="form-input"
                                                                                                        )
                                                                                            ]
                                                                                            , className = "form-input-div"
                                                                                        )

                                                                                , html.Div(
                                                                                            [
                                                                                                dbc.Label(
                                                                                                            "Ingresa tu nombre preferido (como quieres que te llamemos)"
                                                                                                            , html_for="form-name-experiencia_2"
                                                                                                            , className="form-label"
                                                                                                            , id="form-name-label-experiencia_2"
                                                                                                        )
                                                                                                , dbc.Input(
                                                                                                            type="text"
                                                                                                            , id="form-name-experiencia_2"
                                                                                                            , placeholder="nombre preferido"
                                                                                                            , className="form-input"
                                                                                                        )
                                                                                            ]
                                                                                            , className = "form-input-div"
                                                                                        )

                                                                                , html.Div(
                                                                                            [
                                                                                                dbc.Label(
                                                                                                            "Ingresa tu puesto en tu organización"
                                                                                                            , html_for="form-role-experiencia_2"
                                                                                                            , className="form-label"
                                                                                                            , id="form-role-label-experiencia_2"
                                                                                                        )
                                                                                                , dbc.Input(
                                                                                                            type="text"
                                                                                                            , id="form-role-experiencia_2"
                                                                                                            , placeholder="nombre preferido"
                                                                                                            , className="form-input"
                                                                                                        )
                                                                                            ]
                                                                                            , className = "form-input-div"
                                                                                        )

                                                                                , html.Div(
                                                                                            [
                                                                                                dbc.Label(
                                                                                                            "Elige tu tipo de documento"
                                                                                                            , html_for="form-tipo_doc-experiencia_2"
                                                                                                            , className="form-label"
                                                                                                            , id="form-tipo_doc-label-experiencia_2"
                                                                                                        )
                                                                                                , dcc.Dropdown(
                                                                                                                id="form-tipo_doc-experiencia_2"
                                                                                                                , options=[
                                                                                                                            {
                                                                                                                                "label":"DNI",
                                                                                                                                "value":"DNI"
                                                                                                                            },
                                                                                                                            {
                                                                                                                                "label":"carnet de extranjería",
                                                                                                                                "value":"carnet_extranjeria"
                                                                                                                            }
                                                                                                                        ]
                                                                                                                , value="DNI"
                                                                                                                , placeholder="tipo de documento"
                                                                                                                , multi=False
                                                                                                                , className="form-input"
                                                                                                            )
                                                                                            ]
                                                                                            , className = "form-input-div"
                                                                                        )

                                                                                , html.Div(
                                                                                            [
                                                                                                dbc.Label(
                                                                                                            "Ingresa tu número de documento"
                                                                                                            , html_for="form-doc-experiencia_2"
                                                                                                            , className="form-label"
                                                                                                            , id="form-doc-label-experiencia_2"
                                                                                                        )
                                                                                                , dbc.Input(
                                                                                                            type="text"
                                                                                                            , id="form-doc-experiencia_2"
                                                                                                            , placeholder="número de documento"
                                                                                                            , className="form-input"
                                                                                                        )
                                                                                            ]
                                                                                            , className = "form-input-div"
                                                                                        )

                                                                                , html.Div(
                                                                                            [
                                                                                                dbc.Label(
                                                                                                            "Ingresa el nombre de tu organización (de preferencia como está inscrita en SUNAT)"
                                                                                                            , html_for="form-org-experiencia_2"
                                                                                                            , className="form-label"
                                                                                                            , id="form-org-label-experiencia_2"
                                                                                                        )
                                                                                                , dbc.Input(
                                                                                                            type="text"
                                                                                                            , id="form-org-experiencia_2"
                                                                                                            , placeholder="nombre de organización"
                                                                                                            , className="form-input"
                                                                                                        )
                                                                                            ]
                                                                                            , className = "form-input-div"
                                                                                        )

                                                                                , html.Div(
                                                                                            [
                                                                                                dbc.Label(
                                                                                                            "Ingresa el RUC de tu organización"
                                                                                                            , html_for="form-RUC-experiencia_2"
                                                                                                            , className="form-label"
                                                                                                            , id="form-RUC-label-experiencia_2"
                                                                                                        )
                                                                                                , dbc.Input(
                                                                                                            type="text"
                                                                                                            , id="form-RUC-experiencia_2"
                                                                                                            , placeholder="nombre de organización"
                                                                                                            , className="form-input"
                                                                                                        )
                                                                                            ]
                                                                                            , className = "form-input-div"
                                                                                        )

                                                                                , html.Div(
                                                                                            [
                                                                                                dbc.Label(
                                                                                                            "Ingresa la dirección de tu organización (por favor incluye provincia y distrito)"
                                                                                                            , html_for="form-org_direc-experiencia_2"
                                                                                                            , className="form-label"
                                                                                                            , id="form-org_direc-label-experiencia_2"
                                                                                                        )
                                                                                                , dbc.Input(
                                                                                                            type="text"
                                                                                                            , id="form-org_direc-experiencia_2"
                                                                                                            , placeholder="dirección de organización"
                                                                                                            , className="form-input"
                                                                                                        )
                                                                                            ]
                                                                                            , className = "form-input-div"
                                                                                        )

                                                                                , html.Div(
                                                                                            [
                                                                                                dbc.Label(
                                                                                                            "Describe a tu organización en unas cuantas palabras"
                                                                                                            , html_for="form-org_desc-experiencia_2"
                                                                                                            , className="form-label"
                                                                                                            , id="form-org_desc-label-experiencia_2"
                                                                                                        )
                                                                                                , dbc.Input(
                                                                                                            type="text"
                                                                                                            , id="form-org_desc-experiencia_2"
                                                                                                            , placeholder="descripción de organización"
                                                                                                            , className="form-input"
                                                                                                        )
                                                                                            ]
                                                                                            , className = "form-input-div"
                                                                                        )

                                                                                #---------------------------------
                                                                                , html.Div(
                                                                                            [
                                                                                                html.Button(
                                                                                                            "Enviar información"
                                                                                                            , id="btn-form-experiencia_2"
                                                                                                            , n_clicks=0
                                                                                                            )
                                                                                                , dcc.Loading(
                                                                                                            dbc.Row(
                                                                                                                    id="form-result-experiencia_2"
                                                                                                                    )
                                                                                                            , type="circle"
                                                                                                            )
                                                                                            ]
                                                                                            , className = "form-input-div"
                                                                                        )
                                                                            ]
                                                                            , className = "form-div"
                                                                            , id = "form-div-experiencia_2"
                                                                            , style = {"backgroundColor":"white"}
                                                                        )
                                                                ]
                                                            )
                                                    ]
                                                )
                                        ]
                                        , style={"min-width":"25%", 'display':'flex'}
                                    )
                        ]
                        , className = "dash-inside-container"
                    )
    return index

def init_callbacks(dash_app):
    @dash_app.callback(
                        Output('form-result-experiencia_2', 'children')
                        , Input('btn-form-experiencia_2', 'n_clicks')
                        , [
                            State('form-email-experiencia_2', 'value')
                            , State('form-names-experiencia_2', 'value')
                            , State('form-lastnames-experiencia_2', 'value')
                            , State('form-name-experiencia_2', 'value')
                            , State('form-role-experiencia_2', 'value')
                            , State('form-tipo_doc-experiencia_2', 'value')
                            , State('form-doc-experiencia_2', 'value')
                            , State('form-org-experiencia_2', 'value')
                            , State('form-RUC-experiencia_2', 'value')
                            , State('form-org_direc-experiencia_2', 'value')
                            , State('form-org_desc-experiencia_2', 'value')
                        ]
                        , prevent_initial_callback=True
    )
    def send_info(n_clicks, email, names, lastnames, name, role, tipo_doc, doc, org, RUC, org_direc, org_desc):
        print("Start send_info")
        if n_clicks==0:
            return None

        answers = [email, names, lastnames, name, role, tipo_doc, doc, org, RUC, org_direc, org_desc]
        answers_none = [x for x in answers if (x is None) or (x=="")]

        if len(answers_none)>0: return "Parece que te falta llenar un campo, por favor ingresa todos los datos."

        df_new_user = pd.DataFrame(data=[[email, names, lastnames, name, role, 2, tipo_doc, doc]], columns = ["usuario_email", "usuario_nombres", "usuario_apellidos", "usuario_nombre_preferido", "usuario_rol", "usuario_tipo_id", "usuario_tipo_doc", "usuario_doc"])
        print(df_new_user)
        df_new_org = pd.DataFrame(data=[[org, RUC, org_direc, org_desc]], columns = ["organizacion_nombre", "organizacion_RUC", "organizacion_direccion", "organizacion_descripcion"])
        print(df_new_org)

        df_users = utils_google.read_ws_data(utils_google.open_ws("base_1", "usuario"))
        df_users = pd.concat([df_users, df_new_user])
        df_users["usuario_id"] = df_users.reset_index(drop=True).index+1
        utils_google.pandas_to_sheets(df_users, utils_google.open_ws("base_1", "usuario"), clear = True)

        df_orgs = utils_google.read_ws_data(utils_google.open_ws("base_1", "organizacion"))
        df_orgs = pd.concat([df_orgs, df_new_org])
        df_orgs["organizacion_id"] = df_orgs.reset_index(drop=True).index+1
        utils_google.pandas_to_sheets(df_orgs, utils_google.open_ws("base_1", "organizacion"), clear = True)

        return "Has llenado el formulario correctamente, ¡muchas gracias!"