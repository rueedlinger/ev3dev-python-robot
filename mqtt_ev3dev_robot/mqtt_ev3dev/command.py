# -*- coding: utf-8 -*-
class CommandExecutor:

    MSG_COMMAND = 'command'
    MSG_ARGS = 'args'

    def __init__(self, cmd):
        """

        :param cmd:
        """
        strategies = {}

        methods = [method for method in dir(cmd) if callable(getattr(cmd, method))]

        for m in methods:

            if not m.startswith('_'):
                strategies[m] = m

        self.strategies = strategies
        self.dispatcher = cmd

    def exec(self, msg):
        """
        :param msg: the command as msg (dict) which should be executed ({command: 'foo', args = []})
        :return:
        """
        if not msg:
            raise RuntimeError('Wrong format "None"!')

        if not hasattr(msg, "__getitem__"):
            raise RuntimeError('Wrong format, property "command" has no value!')

        if self.MSG_COMMAND in msg:

            command = msg[self.MSG_COMMAND]

            if command in self.strategies:
                if self.MSG_ARGS in msg:
                    # command has args
                    getattr(self.dispatcher, command)(*msg[self.MSG_ARGS])

                else:
                    # command has no args
                    getattr(self.dispatcher, command)()

            else:
                raise NameError('The command "%s" was not found in strategies!' % command)

        else:
            raise RuntimeError('Wrong format, property "command" not found!')