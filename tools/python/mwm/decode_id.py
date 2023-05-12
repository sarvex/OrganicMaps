import re

from mwm.ft2osm import OsmIdCode
from mwm.ft2osm import unpack_osmid


def decode_id(id):
    if id.isdigit():
        osm_id = unpack_osmid(int(id))
        type_abbr = {"n": "node", "w": "way", "r": "relation"}
        return f"https://www.openstreetmap.org/{type_abbr[osm_id[0]]}/{osm_id[1]}"
    else:
        if not (m := re.search(r"/(node|way|relation)/(\d+)", id)):
            return None
        type_name = m[1]
        oid = int(m[2])
        if type_name == "node":
            oid |= OsmIdCode.NODE
        elif type_name == "relation":
            oid |= OsmIdCode.RELATION
        elif type_name == "way":
            oid |= OsmIdCode.WAY
        return oid
