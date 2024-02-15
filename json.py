import json

# Reading and writing an object to a file as json
# This gets around non-serializable custom classes as long as the class
# is relatively simple and we really just want it's attributes.
# For more complex objects and scenarios this article is a decnt start
# https://stackoverflow.com/questions/3768895/...
# ...how-to-make-a-class-json-serializable


# NOTE - indent=2 writes an easy to read indented file.
# Leave this out to get a single line blob
json_file = '.'.join(['myfile', 'json'])
with open(json_file, 'w', newline='') as f:
  json.dump(r['trades'], f, indent=2, default=vars)

# Reading a json file into a dict/list:
# TODO does this work the same with both indented and blob files?

with open(json_file) as f:
    my_thing = json.load(f)
