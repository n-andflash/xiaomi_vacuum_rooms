entity_id = data.get("entity_id")
rooms_list = data.get("rooms")

params = []
rooms_map = { a: a.split("_")[-1] for a in rooms_list }

for room, number in rooms_map.items():
    if hass.states.get(room).state == "on":
        params.append(int(number))

service_data = {
    "command": "app_segment_clean",
    "entity_id": entity_id,
    "params": params,
}

logger.info("app_segment_clean: {} {}".format(entity_id, params))
hass.services.call("vacuum", "send_command", service_data)
