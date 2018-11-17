from read_config_json import read_config


d = read_config('albums.json')

print(d)

print(
    d['Neutral Milk Hotel']['On Avery Island']['year'],
    d['Neutral Milk Hotel']['On Avery Island']['record company'],
)

print(
    d['Big Star'],
)


project_files = read_config('config.json')

print(project_files)

for i in project_files.items():
    print(i)