all = 0
for entity_id in hass.states.entity_ids('automation'):
    state = hass.states.get(entity_id)
    if state.state != '':
        all = all + 1

hass.states.set('sensor.automation_all', all, {'unit_of_measurement': 'all'})