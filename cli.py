import yaml
from core import Power
from cement.core.foundation import CementApp
from cement.ext.ext_argparse import ArgparseController, expose

with open("/Users/pablo/.patron/config.yml", 'r') as ymlfile:
    cfg = yaml.load(ymlfile)

servers = cfg['hosts']

class BaseController(ArgparseController):
    class Meta:
        label = 'base'
        description = "Power, Tool for turning on/off machines using wakeonlan/ssh"
        ignore_unknown_arguments = True

    def default(self):
        self.app.args.print_help()

class PowerController(ArgparseController):
    class Meta:
        label = 'power'
        stacked_on = 'base'
        stacked_type = 'embedded'

    @expose(arguments=[
                (['--hosts', '-hosts'], {'help': 'Turn on machines by hostname', 'action':'store'}),
                (['--tags', '-t'], {'help': 'Turn on machines by tags', 'action': 'store'})
            ],
            help="Turn on machines"
    )
    def on(self):
        if self.app.pargs.hosts or self.app.pargs.tags:
            if self.app.pargs.hosts:
                print(self.app.pargs.hosts)
            elif self.app.pargs.tags:
                print(self.app.pargs.tags)
        else:
            Power.turn_on(servers)
            self.app.log.info('Turning on all machines')

    @expose(arguments=[
                (['--hosts', '-hosts'], {'help': 'Turn off machines by hostname', 'action':'store'}),
                (['--tags', '-t'], {'help': 'Turn off machines by tags', 'action': 'store'})
            ],
            help="Turn off machines"
    )
    def off(self):
        if self.app.pargs.hosts or self.app.pargs.tags:
            print('he')
        else:
            Power.turn_off(servers)
            self.app.log.info('Turning of all machines')

class PowerCLI(CementApp):
    class Meta:
        label = 'wol'
        handlers = [BaseController, PowerController]