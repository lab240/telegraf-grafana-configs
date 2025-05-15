def apply(metric):
    parts = metric.tags["topic"].split("/")

    old_sensors = ["temp_out", "temp_in", "temp_out2", "temp_odd", "current"]

    # for turn off checking for debug

    enable_check = True

    # lets find category sensors 
    # gather /prj/devXX/out/sensors/rXX

    old_sensor_found = False
    for s in old_sensors:
        if s in parts:
            old_sensor_found = True

    if enable_check and "sensors" in parts or old_sensor_found:

        prj = parts[1]
        dev = parts[2]
        category = "sensors"
        # sensor name
        sensor_name = parts[-1]

        metric.tags["dev"] = dev
        metric.tags["prj"] = prj
        #        metric.tags["name"] = sensor_name
        metric.name = category

        # cancel some specific topics
        if "json" in sensor_name or sensor_name == "pzem004":
            metric.fields.clear()
            return metric

        # get raw value
        sensor_value = float(metric.fields["value"])

        # set default multiplier
        mult = 1

        # set type tag and multiplier
        if "temp" in sensor_name:
            metric.tags["type"] = "temp"
            mult = 100
        elif "curr" in sensor_name or "sct" in sensor_name:
            metric.tags["type"] = "current"
            mult = 100
        elif "sec" in sensor_name:
            metric.tags["type"] = "count"
        elif "power" in sensor_name:
            metric.tags["type"] = "current"
        elif "energy" in sensor_name:
            metric.tags["type"] = "current"
        elif "volt" in sensor_name:
            metric.tags["type"] = "current"
            mult = 100
        else:
            metric.tags["type"] = "undef"

        # set tag multiplier
        metric.tags["mult"] = str(mult)

        # set value field
        # sensor_name = metric.fields.get("sensor_name")

        metric.fields[sensor_name] = int(sensor_value * mult)
        metric.fields.pop("value", None)
        # metric.fields.pop("sensor_name", None)

        # delete topic tag
        metric.tags.pop("topic", None)
        return metric

    # lets find category relay 
    # gather /prj/devXX/out/relays/rXX

    if enable_check and "relays" in parts:

        prj = parts[1]
        dev = parts[2]
        category = "relays"
        # sensor name
        sensor_name = parts[-1]

        # get raw value
        sensor_value = float(metric.fields["value"])

        metric.tags["dev"] = dev
        metric.tags["prj"] = prj
        metric.name = category
        metric.fields[sensor_name] = int(sensor_value)
        metric.tags.pop("topic", None)
        return metric

    # lets find time info
    # gather /prj/devXX/out/time_up
    # gather /prj/devXX/out/time_comm
    # gather /prj/devXX/out/time_down

    if enable_check and "time_up" in parts or "time_comm" in parts or "time_down" in parts:

        prj = parts[1]
        dev = parts[2]
        category = "time"

        # time name
        field_name = parts[-1]

        # get raw value
        time_string = metric.fields["value"]

        metric.tags["dev"] = dev
        metric.tags["prj"] = prj
        metric.name = category
        metric.fields[field_name] = time_string
        metric.tags.pop("topic", None)
        return metric

    if enable_check and "b1" in parts or "b2" in parts or "r1" in parts or "r2" in parts:

        prj = parts[1]
        dev = parts[2]
        category = "relays"
        # sensor name
        sensor_name = parts[-1]

        sensor_name = "r1" if sensor_name == "b1" else sensor_name
        sensor_name = "r2" if sensor_name == "b2" else sensor_name

        # get raw value
        sensor_value = float(metric.fields["value"])

        metric.tags["dev"] = dev
        metric.tags["prj"] = prj
        metric.name = category
        metric.fields[sensor_name] = int(sensor_value)
        metric.tags.pop("topic", None)
        return metric

    # gather /prj/devXX/out/sensorXX (old format)

    # old_sensors=["temp_out", "temp_in", "temp_out2"]
    # if any(sensor in parts for sensor in old_sensors):
    #     prj = parts[1]
    #     dev = parts[2]
    #     category = "sensors"

    #     # sensor name
    #     old_sensor_name = parts[-1]

    #     metric.tags.pop("topic", None)
    #     return metric

    metric.fields.clear()
    return metric
