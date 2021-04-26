from controllers import registroacudeinteUserControllers, LoginUserControllers, datosUserControllers, datosinstitucionUserControllers

user = {
    "datos_user": "/api/v01/user/datos", "datos_user_controllers": datosUserControllers.as_view("datos_api"),
    "registroacudiente_user": "/api/v01/user/registroacudiente", "registroacudiente_user_controllers": registroacudeinteUserControllers.as_view("registro_api"),
    "login_user": "/api/v01/user/login", "login_user_controllers": LoginUserControllers.as_view("login_api"),
    "datosinstitucion_user": "/api/v01/user/datosinstitucion", "datosinstitucion_user_controllers": datosinstitucionUserControllers.as_view("datosinstitucion_api"),
    }
