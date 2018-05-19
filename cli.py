import yaml
import filter_by
from core import Power
from cement.core.foundation import CementApp
from cement.ext.ext_argparse import ArgparseController, expose

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
                (['--hosts', '-hosts'], {'help': 'Turn on machines by hostname', 'action':'store', 'nargs': '*'}),
                (['--tag', '-t'], {'help': 'Turn on machines by a tag', 'action': 'store'})
            ],
            help="Turn on machines"
    )
    def on(self):
        if self.app.pargs.hosts or self.app.pargs.tag:
            if self.app.pargs.hosts:
                self.app.log.info('Turning on machines')
                for host in self.app.pargs.hosts:
                    server = filter_by.host(host)
                    if bool(server) == False:
                        self.app.log.fatal("Servers {} not found".format(host))        
                    else:
                        Power.turn_on(server)
            elif self.app.pargs.tag:
                servers = filter_by.tag(self.app.pargs.tag)
                if bool(servers) == False:
                    self.app.log.fatal("Servers with a tag {} not found".format(self.app.pargs.tag))        
                else:
                    self.app.log.info('Turning on machines')
                    Power.turn_on(servers)
        else:
            self.app.log.info('Turning on all machines')
            Power.turn_on(filter_by.SERVERS)

    @expose(arguments=[
                (['--hosts', '-hosts'], {'help': 'Turn off machines by hostname', 'action':'store', 'nargs': '*'}),
                (['--tag', '-t'], {'help': 'Turn off machines by tag', 'action': 'store'})
            ],
            help="Turn off machines"
    )
    def off(self):
        if self.app.pargs.hosts or self.app.pargs.tag:
            if self.app.pargs.hosts:
                self.app.log.info('Turning on machines')
                for host in self.app.pargs.hosts:
                    server = filter_by.host(host)
                    if bool(server) == False:
                        self.app.log.fatal("Servers {} not found".format(host))        
                    else:
                        Power.turn_off(server)
            elif self.app.pargs.tag:
                servers = filter_by.tag(self.app.pargs.tag)
                if bool(servers) == False:
                    self.app.log.fatal("Servers with a tag {} not found".format(self.app.pargs.tag))        
                else:
                    self.app.log.info('Turning off machines')
                    Power.turn_off(servers)
        else:
            self.app.log.info('Turning of all machines')
            Power.turn_off(filter_by.SERVERS)

class PowerCLI(CementApp):
    class Meta:
        label = 'power'
        handlers = [BaseController, PowerController]