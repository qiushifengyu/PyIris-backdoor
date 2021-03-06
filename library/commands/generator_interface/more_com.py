import library.modules.config as config

config.main()

tmp_win = config.win_components.values()
for i in tmp_win:
    exec ('import components.' + i.replace('/', '.') + ' as ' + i.replace('/', '_'))
print config.pos + 'Loaded all windows components info - OK'
tmp_lin = config.lin_components.values()
for i in tmp_lin:
    exec ('import components.' + i.replace('/', '.') + ' as ' + i.replace('/', '_'))
print config.pos + 'Loaded all linux components info - OK'



def main(command):
    try:
        load_on = command.split(' ', 1)[1]
        if config.scout_values['Windows'][0] == 'True':
            sample_space = list(set(tmp_win + config.loaded_components.values()))
            if load_on in sample_space:
                exec (load_on.replace('/', '_') + '.main("info")')
            else:
                load_on = dict(config.win_components.items() + config.loaded_components.items())[load_on]
                exec (load_on.replace('/', '_') + '.main("info")')
        else:
            sample_space = list(set(tmp_lin + config.loaded_components.values()))
            if load_on in sample_space:
                exec (load_on.replace('/', '_') + '.main("info")')
            else:
                load_on = dict(config.lin_components.items() + config.loaded_components.items())[load_on]
                exec (load_on.replace('/', '_') + '.main("info")')
    except (IndexError, KeyError):
        print config.neg + 'Please specify a valid component to show more info for'
