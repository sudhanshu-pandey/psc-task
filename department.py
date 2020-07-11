from flask import make_response, abort
from difflib import get_close_matches

# Data to serve with our API
DEPARTMENT_LIST = {
    "Computer Science": {
        "dname": "Computer Science",
        "dep_description": "Department of computer science",
    },
    "Electronics": {
        "dname": "Electronics",
        "dep_description": "Department of computer science",
    },
    "Social Sciences": {
        "dname": "Social Sciences",
        "dep_description": "Department of social science",
    },
    "Social Studies": {
        "dname": "Social Studies",
        "dep_description": "Department of social Studies",
    },
    "Computer Engineering": {
        "dname": "Computer Engineering",
        "dep_description": "Department of computer Engineering",
    },
    "Advanced Engineering": {
        "dname": "Advanced Engineering",
        "dep_description": "Department of Advanced Engineering",
    },

}

DEP_NAMES_LIST = [x.lower() for x in list(DEPARTMENT_LIST)]

# function to find similar department name


def closeMatches(patterns, word):
    return get_close_matches(word, patterns, n=5, cutoff=0.2)


# functions that respond to api calls

# read all departments
def read_all():
    """
    This function responds to a request for /api/department
    with the complete lists of Department
    :return:        json string of list of Department
    """
    # Create the list of DEPARTMENT_LIST from our data
    return [DEPARTMENT_LIST[key] for key in sorted(DEPARTMENT_LIST.keys())]


# read one department according to name specified
def read_one(dname):
    """
    This function responds to a request for /api/department/{dname}
    with one matching department from DEPARTMENT_LIST
    :param dname:   name of department to find
    :return:        department matching name
    """
    # Does the department exist in DEPARTMENT_LIST?
    if dname in DEPARTMENT_LIST:
        dname = DEPARTMENT_LIST.get(dname)

    # otherwise, nope, not found
    else:
        abort(
            404, "Department with name {dname} not found".format(dname=dname)
        )

    return dname


def read_matching_dep(dqry):
    """
    This function responds to a request for /api/department/get_department/{dqry}
    with list of matching departments from DEPARTMENT_LIST
    :param dqr:   name of department to find
    :return:      departments with matching name
    """
    # Does the similar department exist in DEPARTMENT_LIST?

    dqry = dqry.lower()
    close_match_names = closeMatches(DEP_NAMES_LIST, dqry)
    close_match_names = [close_match_names.title() for close_match_names in close_match_names]

    if len(close_match_names) > 0:
        return [DEPARTMENT_LIST[key] for key in sorted(close_match_names)]
    # otherwise, nope, not found
    else:
        abort(
            404, "Departments with name {dqry} not found".format(dqry=dqry)
        )
