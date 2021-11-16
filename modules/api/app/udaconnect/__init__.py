from app.udaconnect.models import Connection, Location, Person  # noqa
from app.udaconnect.schemas import ConnectionSchema, LocationSchema, PersonSchema  # noqa
from modules.location_srv.app.udaconnect.models import Location
from modules.location_srv.app.udaconnect.schemas import LocationSchema


def register_routes(api, app, root="api"):
    from app.udaconnect.controllers import api as udaconnect_api
    from modules.location_srv.app.udaconnect.controllers import loc as location_loc 

    api.add_namespace(udaconnect_api, path=f"/{root}")
    
