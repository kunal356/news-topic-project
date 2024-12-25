def read_config():
    config = {}
    try: 
        with open("client.properties") as fh:
            for line in fh:
                line = line.strip()
                if len(line) != 0 and line[0] != "#":
                    parameter, value = line.split('=', 1)
                    config[parameter] = value.strip()
    except Exception as e:
        print(f"Error while reading configs: {e}")
    return config
