import AOE_API_constants as ct
import Avatars as avt

root = ct.AOE2

# function to Validate the Platform ( Xbox or Steam)
def eval_platform(platform):

    plt = platform.casefold()

    if (plt=='xbox')or(plt=='steam'):
        return plt
    else:
        return 'error'


# ________________________________________________________________

