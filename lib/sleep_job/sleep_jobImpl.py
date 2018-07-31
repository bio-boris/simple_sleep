# -*- coding: utf-8 -*-
#BEGIN_HEADER
#END_HEADER


class sleep_job:
    '''
    Module Name:
    sleep_job

    Module Description:
    A KBase module: sleep_job
    '''

    ######## WARNING FOR GEVENT USERS ####### noqa
    # Since asynchronous IO can lead to methods - even the same method -
    # interrupting each other, you must be *very* careful when using global
    # state. A method could easily clobber the state set by another while
    # the latter method is running.
    ######################################### noqa
    VERSION = "0.0.1"
    GIT_URL = ""
    GIT_COMMIT_HASH = "HEAD"

    #BEGIN_CLASS_HEADER
    #END_CLASS_HEADER

    # config contains contents of config file in a hash or None if it couldn't
    # be found
    def __init__(self, config):
        #BEGIN_CONSTRUCTOR
        #END_CONSTRUCTOR
        pass


    def simple_sleep(self, ctx, params):
        """
        :param params: instance of type "SimpleParams" -> structure:
           parameter "input_sleep" of Long, parameter "workspace_name" of
           String
        :returns: instance of Long
        """
        # ctx is the context object
        # return variables are: output
        #BEGIN simple_sleep

        import time
        input_sleep = params['input_sleep']

        if input_sleep < 120:
            input_sleep = 120

        print("About to sleep for " + str(input_sleep) + " seconds")
        time.sleep(input_sleep)
        output = {'new_number': 1}

        #END simple_sleep

        # return the results
        return [output]
    def status(self, ctx):
        #BEGIN_STATUS
        returnVal = {'state': "OK",
                     'message': "",
                     'version': self.VERSION,
                     'git_url': self.GIT_URL,
                     'git_commit_hash': self.GIT_COMMIT_HASH}
        #END_STATUS
        return [returnVal]
