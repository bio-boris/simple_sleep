/*
A KBase module: sleep_job
*/

module sleep_job {

    typedef structure {
        int input_sleep;
        string workspace_name;
    } SimpleParams;

    typedef structure {
        int new_number;
    } SimpleResults;


    funcdef simple_sleep(SimpleParams params)
        returns (SimpleResults output) authentication required;
};
